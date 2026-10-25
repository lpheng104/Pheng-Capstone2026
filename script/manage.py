"""Cross-platform setup, start, lint, test and deterministic build verbs."""
import argparse
import compileall
import hashlib
import os
from pathlib import Path
import secrets
import subprocess
import sys
import venv
import zipfile

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT), str(ROOT)]
PYTHON = ROOT/'.venv'/('Scripts/python.exe' if os.name == 'nt' else 'bin/python')


def check_runtime():
    wanted = (ROOT/'.python-version').read_text().strip()
    actual = '.'.join(map(str, sys.version_info[:3]))
    if wanted != actual:
        raise RuntimeError(f'Python {wanted} is required; this interpreter is {actual}.')


def load_config():
    from dotenv import load_dotenv
    load_dotenv(ROOT/'.env')


def setup(no_install=False):
    check_runtime()
    if not no_install:
        if not PYTHON.exists():
            venv.EnvBuilder(with_pip=True).create(ROOT/'.venv')
        subprocess.run([str(PYTHON), '-m', 'pip', 'install', '--require-hashes',
                        '-r', str(ROOT/'requirements.lock')], check=True, cwd=ROOT)
        # Continue in the lock-installed environment, including on a clean machine.
        subprocess.run([str(PYTHON), str(Path(__file__)), 'setup', '--no-install'],
                       check=True, cwd=ROOT)
        return
    from dotenv import dotenv_values
    path = ROOT/'.env'
    values = dotenv_values(path) if path.exists() else dotenv_values(ROOT/'.env.example')
    defaults = {
        'SECRET_KEY': secrets.token_urlsafe(48),
        'ADMIN_SETUP_TOKEN': secrets.token_urlsafe(32),
        'SKELETON_PASSWORD': 'Demo!'+secrets.token_urlsafe(24),
    }
    # Preserve existing values; replace only empty example fields.
    for name, value in defaults.items():
        if not values.get(name):
            values[name] = os.environ.get(name) or value
    if any('\n' in str(v) or '\r' in str(v) for v in values.values()):
        raise ValueError('Configuration values must be single-line.')
    path.write_text(''.join(f'{k}={v or ""}\n' for k,v in values.items()), encoding='utf-8')
    load_config()
    from migrations.run import apply, load_manifest
    from src.maintenance import seed
    from src.persistence import connect
    client, db = connect(os.environ['MONGODB_URI'], os.environ['MONGODB_DATABASE'])
    try:
        # Guard before schema changes, not only before seeding.
        if not (db.name.endswith('_skeleton') or db.name.startswith('test_')):
            raise ValueError('Setup requires a dedicated *_skeleton or test_* database.')
        manifest, digest = load_manifest()
        print(apply(db, manifest, digest))
        unit_id = seed(db, os.environ['SKELETON_PASSWORD'])
        print('SEEDED synthetic unit, member, message, event and attendance response.')
        print('START with script/start; sign in as skeleton_member using SKELETON_PASSWORD from .env.')
        print('UNIT /units/'+unit_id)
    finally:
        client.close()


def build():
    check_runtime()
    assert compileall.compile_dir(ROOT/'src', quiet=1)
    from jinja2 import Environment, FileSystemLoader, select_autoescape
    env = Environment(loader=FileSystemLoader(ROOT/'src/templates'),
                      autoescape=select_autoescape())
    for name in env.list_templates():
        env.get_template(name)
    target = ROOT/'dist/accountabilibuddy-skeleton.zip'
    target.parent.mkdir(exist_ok=True)
    files = list((ROOT/'src').rglob('*'))
    files += list((ROOT/'migrations').glob('*.py')) + list((ROOT/'migrations').glob('*.json'))
    files += [ROOT/'requirements.lock', ROOT/'.python-version']
    with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as archive:
        for source in sorted(files):
            if not source.is_file() or '__pycache__' in source.parts or source.suffix == '.pyc':
                continue
            name = str(source.relative_to(ROOT)).replace('\\','/')
            info = zipfile.ZipInfo(name, date_time=(2026,1,1,0,0,0))
            info.compress_type = zipfile.ZIP_DEFLATED
            archive.writestr(info, source.read_bytes())
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    print('BUILD PASS: '+target.name+' SHA256 '+digest)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('verb', choices=['setup','start','lint','test','build'])
    parser.add_argument('--no-install', action='store_true')
    parser.add_argument('--port', type=int, default=5000)
    args = parser.parse_args()
    os.chdir(ROOT)
    if args.verb == 'setup':
        setup(args.no_install)
    elif args.verb == 'start':
        load_config()
        from src.app import create_app
        create_app().run(host='127.0.0.1', port=args.port, debug=False, use_reloader=False)
    elif args.verb == 'lint':
        subprocess.run([sys.executable,'-m','ruff','check','src','script',
                        'tests/test_skeleton.py'],check=True)
    elif args.verb == 'test':
        subprocess.run([sys.executable,'-m','pytest','-q'],check=True)
    else:
        build()


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        # Never print a URI, password, raw driver error or form content.
        print('COMMAND FAILED: '+type(error).__name__, file=sys.stderr)
        raise SystemExit(1) from None
