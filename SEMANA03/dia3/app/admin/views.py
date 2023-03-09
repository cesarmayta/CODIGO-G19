from flask import Flask,render_template,request

from . import admin

@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/categoria')
def categoria():
    return render_template('admin/categoria.html')

@admin.route('/modalidad')
def modalidad():
    return render_template('admin/modalidad.html')

@admin.route('/jornada')
def jornada():
    return render_template('admin/jornada.html')

@admin.route('/empresa')
def empresa():
    return render_template('admin/empresa.html')

@admin.route('/oferta')
def oferta():
    return render_template('admin/oferta.html')