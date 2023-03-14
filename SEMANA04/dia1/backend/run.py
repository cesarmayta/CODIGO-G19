from app import create_app
from utils.db import db
from flask_migrate import Migrate

app = create_app()

with app.app_context():
    db.init_app(app)
    migrate = Migrate(app,db)