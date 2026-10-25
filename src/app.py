# AI-generated 2026-09-17; see docs/ai-usage.md. Review before capstone submission.
import os
import re
import secrets
from datetime import datetime, timedelta, timezone
from functools import wraps

from bson import ObjectId
from dotenv import load_dotenv
from flask import Flask, abort, flash, g, redirect, render_template, request, session, url_for
from pymongo import ASCENDING, DESCENDING
from pymongo.errors import DuplicateKeyError, PyMongoError
from werkzeug.security import check_password_hash, generate_password_hash
from src.identity import resolve_user
from src.persistence import Store, connect, verify_schema
from src.unit_access import AccessDenied, UnitNotFound
from src.web import render_unit


def create_app(config=None, database=None):
    load_dotenv()
    app = Flask(__name__)
    app.config.update(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        ADMIN_USERNAME=os.getenv('ADMIN_USERNAME', '').strip().lower(),
        ADMIN_SETUP_TOKEN=os.getenv('ADMIN_SETUP_TOKEN', ''),
        SESSION_COOKIE_HTTPONLY=True,
        SESSION_COOKIE_SAMESITE='Lax',
        SESSION_COOKIE_SECURE=os.getenv('COOKIE_SECURE', 'false').lower() == 'true',
        PERMANENT_SESSION_LIFETIME=timedelta(hours=8),
        MAX_CONTENT_LENGTH=64 * 1024,
    )
    if config:
        app.config.update(config)
    injected_database = database is not None
    if not app.config['SECRET_KEY']:
        raise RuntimeError('Set SECRET_KEY in your environment or .env file.')
    if database is None:
        uri = os.getenv('MONGODB_URI')
        if not uri:
            raise RuntimeError('Set MONGODB_URI in your environment or .env file.')
        client, database = connect(uri, os.getenv('MONGODB_DATABASE', 'accountabilibuddy'))
        verify_schema(database)
        app.extensions['mongo_client'] = client
    db = database
    app.extensions['db'] = db
    store = Store(db)
    app.extensions['store'] = store
    if injected_database:
        # Unit-test fixture only. Real deployments apply the versioned migration.
        db.users.create_index('username', unique=True)
        db.memberships.create_index([('unit_id', ASCENDING), ('user_id', ASCENDING)], unique=True)
        db.messages.create_index([('unit_id', ASCENDING), ('created_at', DESCENDING)])
        db.events.create_index([('unit_id', ASCENDING), ('starts_at', ASCENDING)])
        db.responses.create_index([('event_id', ASCENDING), ('user_id', ASCENDING)], unique=True)
        db.login_attempts.create_index('expires_at', expireAfterSeconds=0)
        db.sessions.create_index('token', unique=True)
        db.sessions.create_index('expires_at', expireAfterSeconds=0)

    def oid(value):
        if not ObjectId.is_valid(value):
            abort(404)
        return ObjectId(value)

    def field(name, maximum=200, required=True):
        value = request.form.get(name, '').strip()
        if (required and not value) or len(value) > maximum:
            abort(400, description=f'{name} is required and must be at most {maximum} characters.')
        return value

    def password_valid(password):
        return (8 <= len(password) <= 128 and re.search('[a-z]', password)
                and re.search('[A-Z]', password) and re.search('[!@#$%]', password))

    def login_required(view):
        @wraps(view)
        def wrapped(*args, **kwargs):
            if not g.user:
                return redirect(url_for('login'))
            return view(*args, **kwargs)
        return wrapped

    def membership(unit_id, leader=False):
        unit = db.units.find_one({'_id': oid(unit_id)})
        if not unit:
            abort(404)
        member = db.memberships.find_one({'unit_id': unit['_id'], 'user_id': g.user['_id']})
        if not member or (leader and member['role'] not in ('owner', 'leader')):
            abort(403)
        return unit, member

    @app.before_request
    def authenticate_and_csrf():
        g.user = None
        # Health must not spend its budget resolving an unrelated stale cookie.
        if request.endpoint == 'health':
            return None
        token = session.get('auth_token')
        g.user = resolve_user(store, token)
        if 'csrf' not in session:
            session['csrf'] = secrets.token_urlsafe(32)
        if request.method == 'POST':
            supplied = request.form.get('csrf', '')
            if not secrets.compare_digest(session['csrf'].encode(), supplied.encode()):
                abort(400, description='Form expired. Reload the page and try again.')

    @app.context_processor
    def template_globals():
        return {'csrf': session.get('csrf'), 'current_user': g.user,
                'is_admin': bool(g.user and g.user['username'] == app.config['ADMIN_USERNAME'])}

    @app.after_request
    def security_headers(response):
        response.headers['X-Content-Type-Options'] = 'nosniff'
        response.headers['X-Frame-Options'] = 'DENY'
        response.headers['Content-Security-Policy'] = "default-src 'self'; style-src 'self'; form-action 'self'; frame-ancestors 'none'"
        if request.endpoint != 'static':
            response.headers['Cache-Control'] = 'no-store'
        return response

    @app.errorhandler(PyMongoError)
    def database_error(error):
        app.logger.error('Database operation failed: %s', type(error).__name__)
        return render_template('error.html', message='Database unavailable. Please try again shortly.'), 503

    @app.route('/health')
    def health():
        store.ping()
        return {'status': 'ok'}

    @app.errorhandler(AccessDenied)
    def access_denied(error):
        return render_template('error.html', message='You do not have access to this unit.'), 403

    @app.errorhandler(UnitNotFound)
    def unit_not_found(error):
        return render_template('error.html', message='Unit not found.'), 404

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            username = field('username', 32).lower()
            password = request.form.get('password', '')
            if not re.fullmatch(r'[a-z0-9_]{3,32}', username):
                flash('Username must contain 3–32 letters, numbers, or underscores.')
            elif username == app.config['ADMIN_USERNAME'] and (not app.config['ADMIN_SETUP_TOKEN'] or not secrets.compare_digest(app.config['ADMIN_SETUP_TOKEN'].encode(), request.form.get('setup_token', '').encode())):
                flash('The administrator account requires the configured setup token.')
            elif not password_valid(password):
                flash('Password needs 8–128 characters, uppercase, lowercase, and one of !@#$%.')
            else:
                try:
                    db.users.insert_one({'username': username, 'name': field('name', 80),
                                         'password_hash': generate_password_hash(password)})
                    flash('Account created. Please sign in.')
                    return redirect(url_for('login'))
                except DuplicateKeyError:
                    flash('Username already in use.')
        return render_template('auth.html', registering=True)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            username = field('username', 32).lower()
            now = datetime.now(timezone.utc)
            # Shared database counter works across Gunicorn workers; expires after 15 minutes.
            attempt = db.login_attempts.find_one_and_update(
                {'_id': username}, {'$inc': {'count': 1}, '$setOnInsert': {'expires_at': now + timedelta(minutes=15)}},
                upsert=True, return_document=True)
            if attempt['expires_at'].replace(tzinfo=timezone.utc) <= now:
                db.login_attempts.update_one({'_id': username}, {'$set': {'count': 1, 'expires_at': now + timedelta(minutes=15)}})
            elif attempt['count'] > 10:
                abort(429, description='Too many sign-in attempts. Try again in 15 minutes.')
            user = db.users.find_one({'username': username})
            password = request.form.get('password', '')
            if user and len(password) <= 128 and check_password_hash(user['password_hash'], password):
                if session.get('auth_token'):
                    db.sessions.delete_one({'token': session['auth_token']})
                session.clear()
                session.permanent = True
                session['auth_token'] = secrets.token_urlsafe(32)
                db.sessions.insert_one({'token': session['auth_token'], 'user_id': user['_id'],
                                        'expires_at': now + timedelta(hours=8)})
                db.login_attempts.delete_one({'_id': username})
                return redirect(url_for('dashboard'))
            flash('Invalid username or password.')
        return render_template('auth.html', registering=False)

    @app.post('/logout')
    @login_required
    def logout():
        db.sessions.delete_one({'token': session.get('auth_token')})
        session.clear()
        return redirect(url_for('login'))

    @app.get('/')
    @login_required
    def dashboard():
        memberships = list(db.memberships.find({'user_id': g.user['_id']}))
        units = list(db.units.find({'_id': {'$in': [m['unit_id'] for m in memberships]}}))
        return render_template('dashboard.html', units=units)

    @app.post('/units')
    @login_required
    def create_unit():
        if g.user['username'] != app.config['ADMIN_USERNAME']:
            abort(403)
        unit_id = db.units.insert_one({'name': field('name', 80), 'echelon': field('echelon', 30),
                                       'created_by': g.user['_id']}).inserted_id
        db.memberships.insert_one({'unit_id': unit_id, 'user_id': g.user['_id'], 'role': 'owner', 'rank': ''})
        return redirect(url_for('unit_page', unit_id=unit_id))

    @app.get('/units/<unit_id>')
    @login_required
    def unit_page(unit_id):
        return render_unit(store, unit_id, g.user['_id'])

    @app.post('/units/<unit_id>/members')
    @login_required
    def add_member(unit_id):
        unit, _ = membership(unit_id, leader=True)
        user = db.users.find_one({'username': field('username', 32).lower()})
        if not user:
            flash('That user must register first.')
        else:
            db.memberships.update_one({'unit_id': unit['_id'], 'user_id': user['_id']},
                                      {'$setOnInsert': {'role': 'member', 'rank': ''}}, upsert=True)
            flash('Member added.')
        return redirect(url_for('unit_page', unit_id=unit_id))

    @app.post('/units/<unit_id>/members/<user_id>')
    @login_required
    def edit_member(unit_id, user_id):
        unit, actor = membership(unit_id, leader=True)
        target = db.memberships.find_one({'unit_id': unit['_id'], 'user_id': oid(user_id)})
        if not target:
            abort(404)
        if target['role'] == 'owner' or actor['role'] != 'owner':
            abort(403)
        role = field('role', 10)
        if role not in ('leader', 'member'):
            abort(400)
        db.memberships.update_one({'_id': target['_id']}, {'$set': {'role': role, 'rank': field('rank', 30, False)}})
        return redirect(url_for('unit_page', unit_id=unit_id))

    @app.post('/units/<unit_id>/messages')
    @login_required
    def send_message(unit_id):
        unit, _ = membership(unit_id)
        db.messages.insert_one({'unit_id': unit['_id'], 'author_id': g.user['_id'],
                                'author': g.user['name'], 'body': field('body', 2000), 'created_at': datetime.now(timezone.utc)})
        return redirect(url_for('unit_page', unit_id=unit_id))

    @app.post('/units/<unit_id>/events')
    @login_required
    def create_event(unit_id):
        unit, _ = membership(unit_id, leader=True)
        try:
            starts = datetime.fromisoformat(field('starts_at', 40))
            if starts.tzinfo is None:
                raise ValueError()
            starts = starts.astimezone(timezone.utc)
        except ValueError:
            abort(400, description='Enter an ISO date and time with UTC offset, such as 2026-10-01T06:00-05:00.')
        db.events.insert_one({'unit_id': unit['_id'], 'title': field('title', 100), 'starts_at': starts,
                              'location': field('location', 200), 'uniform': field('uniform', 100, False),
                              'details': field('details', 2000, False), 'created_by': g.user['_id']})
        return redirect(url_for('unit_page', unit_id=unit_id))

    @app.post('/units/<unit_id>/events/<event_id>/respond')
    @login_required
    def respond(unit_id, event_id):
        unit, _ = membership(unit_id)
        event = db.events.find_one({'_id': oid(event_id), 'unit_id': unit['_id']})
        if not event:
            abort(404)
        status = field('status', 20)
        if status not in ('attending', 'not attending'):
            abort(400)
        db.responses.update_one({'event_id': event['_id'], 'user_id': g.user['_id']}, {'$set': {'status': status}}, upsert=True)
        return redirect(url_for('unit_page', unit_id=unit_id))

    return app
