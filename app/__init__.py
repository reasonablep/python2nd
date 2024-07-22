from flask import Flask
from app.routes import home
from app.routes import dashboard, home, api
from app.db import init_db
from app.utils import filters


def create_app(test_config=None):
#setup app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    # register util filters to jinja templates to correct format

    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    @app.route('/hello')
    def hello():
        return 'hello world'
    
    app.register_blueprint(home)

    app.register_blueprint(dashboard)

    app.register_blueprint(api)

#passing app to init_db ensures that with db init, we dont have any hanging connections
    init_db(app)

    return app