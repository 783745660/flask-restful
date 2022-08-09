# 需要安装flask_restful 扩展  pip install flask-restful
from flask_script import Manager
from flask_migrate import MigrateCommand
from App import create_app

app = create_app()
manager = Manager(app=app)
manager.add_command('db',MigrateCommand)
manager.run()