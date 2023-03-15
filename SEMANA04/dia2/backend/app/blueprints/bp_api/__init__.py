from flask import Blueprint

bp_api = Blueprint('bp_api',__name__,url_prefix='/')

from . import resources