"""
WELCOME: app constructor & factory - glave/app/__init__.py
"""
from flask import Flask, render_template, current_app
from werkzeug.local import LocalProxy

from .extensions import moment, csrf

# relay for logger
logger = LocalProxy(lambda: current_app.logger)

def crash_page(e):
    return render_template('error_pages/500.html'), 500

def page_not_found(e):
    return render_template('error_pages/404.html'), 404

def page_forbidden(e):
    return render_template('error_pages/403.html'), 403

# sort of like an application factory
def create_app(*args): 
    # Initialize Flask and set some config values
    app = Flask(__name__)
    app.config.from_object('settings')

    moment.init_app(app)
    csrf.init_app(app)

    # BLUEPRINTS
    from .views import views as views_blueprint
    app.register_blueprint(views_blueprint)

    
    # error handlers
    app.register_error_handler(500, crash_page)
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(403, page_forbidden)

    return app