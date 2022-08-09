# 主要用于扩展文件
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
# 导入flask_restful 扩展中的 Api类
from flask_restful import Api

migrate = Migrate()
db = SQLAlchemy()
api = Api()

def init_exts(app):
    db.init_app(app=app)
    migrate.init_app(app=app)
    api.init_app(app=app)
