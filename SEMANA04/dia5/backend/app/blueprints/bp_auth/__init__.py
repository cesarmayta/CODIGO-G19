from flask import Blueprint

bp_auth = Blueprint('bp_auth',__name__,url_prefix='/auth')

from .resources import usuario