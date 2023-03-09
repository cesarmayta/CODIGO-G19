from flask import Flask

#conexión a base de datos
from app.mysql_conn import MysqlDb
mysqlDb = MysqlDb('localhost','root','','db_ofertas_g19')
dbConn = mysqlDb.getConn()

#blueprints
from .portal import portal
from .admin import admin

def create_app():
    app = Flask(__name__)
    app.register_blueprint(portal)
    app.register_blueprint(admin)
    
    return app