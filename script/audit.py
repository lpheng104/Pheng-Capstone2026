"""Audit all Git history and tracked/unignored source with pinned Gitleaks."""
import argparse
import hashlib
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
VERSION = '8.30.1'


def install():
    platform = 'windows_x64.zip' if os.name == 'nt' else 'linux_x64.tar.gz'
    name = f'gitleaks_{VERSION}_{platform}'
    base = f'https://github.com/gitleaks/gitleaks/releases/download/v{VERSION}/'
    with urllib.request.urlopen(base+f'gitleaks_{VERSION}_checksums.txt',timeout=60) as r:
        sums = r.read().decode()
    with urllib.request.urlopen(base+name,timeout=60) as r:
        data = r.read()
    expected = next(line.split()[0] for line in sums.splitlines() if line.endswith(name))
    if hashlib.sha256(data).hexdigest() != expected:
        raise ValueError('Gitleaks checksum mismatch')
    dest = ROOT/'.runtime/tooling'
    dest.mkdir(parents=True,exist_ok=True)
    archive = dest/name
    archive.write_bytes(data)
    binary = dest/('gitleaks.exe' if os.name == 'nt' else 'gitleaks')
    if os.name == 'nt':
        with zipfile.ZipFile(archive) as z:
            binary.write_bytes(z.read('gitleaks.exe'))
    else:
        with tarfile.open(archive) as z:
            binary.write_bytes(z.extractfile('gitleaks').read())
        binary.chmod(0o700)
    return binary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--install',action='store_true')
    args = parser.parse_args()
    binary = ROOT/'.runtime/tooling'/('gitleaks.exe' if os.name == 'nt' else 'gitleaks')
    if args.install or not binary.exists():
        binary = install()
    subprocess.run([str(binary),'git','--redact','--no-banner','--log-opts=--all',str(ROOT)],check=True)
    # Deliberately stage only Git-tracked/unignored source, never .env or runtime data.
    names = subprocess.check_output(['git','ls-files','--cached','--others','--exclude-standard','-z'],cwd=ROOT)
    staged = ROOT/'.runtime/secret-audit-source'
    # Do not recursively delete any path: a fresh isolated stage per audit invocation.
    import tempfile
    staged.mkdir(parents=True,exist_ok=True)
    with tempfile.TemporaryDirectory(dir=staged,prefix='scan-') as temporary:
        dest = Path(temporary)
        assert dest.resolve().is_relative_to(staged.resolve())
        assert staged.resolve().is_relative_to(ROOT.resolve())
        for name in set(names.decode('utf-8').split('\0'))- {''}:
            source = ROOT/name
            if source.is_file() and not source.is_symlink():
                target = dest/name
                target.parent.mkdir(parents=True,exist_ok=True)
                shutil.copyfile(source,target)
        subprocess.run([str(binary),'dir','--redact','--no-banner',str(dest)],check=True)
    print('SECRET AUDIT PASS: complete Git history and tracked/unignored source; no findings.')


if __name__ == '__main__':
    try:
        main()
    except Exception as error:
        print('SECRET AUDIT FAILED: '+type(error).__name__,file=sys.stderr)
        raise SystemExit(1) from None
