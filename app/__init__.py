from flask import Flask
from app.models.book import db

def create_app():
    app = Flask(__name__)
    # 可用这个方法导入配置文件
    app.config.from_object('app.secure_config')
    app.config.from_object('app.setting_config')
    register_blueprint(app)

    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app

# blueprint register
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
