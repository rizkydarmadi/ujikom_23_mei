from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost:3308/simpan_pinjam'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    migrate = Migrate(app, db) # for migrate https://flask-migrate.readthedocs.io/en/latest/

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    from .anggota import anggota as anggota_blueprint
    app.register_blueprint(anggota_blueprint)
    from .kasir import kasir as kasir_blueprint
    app.register_blueprint(kasir_blueprint)
    from .simpan import simpan as simpan_blueprint
    app.register_blueprint(simpan_blueprint)
    from .pinjam import pinjam as pinjam_blueprint
    app.register_blueprint(pinjam_blueprint)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    return app