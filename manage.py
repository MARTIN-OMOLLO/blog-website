from app import create_app, db
from app.models import User
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
app = create_app('production')

manager = Manager(app)

manager.add_command('server', Server)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)
