from flask import Flask,render_template,request

from . import admin

#importamos connDb para mysql
from app import dbConn

#importamos formularios
from .forms import CatalogoForm

def getSqlCatalogo(tblCatalogo):
    strSqlCatalogo = "select " + tblCatalogo + "_id as id," + tblCatalogo + "_descripcion as descripcion from tbl_" + tblCatalogo
    return strSqlCatalogo

def setSqlCatalogo(tblCatalogo,strDescripcion):
    strSqlInsertCatalogo = "insert into tbl_" + tblCatalogo
    strSqlInsertCatalogo += "("+tblCatalogo+"_descripcion) "
    strSqlInsertCatalogo += "values ('"+strDescripcion+"');"
    
    return strSqlInsertCatalogo

@admin.route('/')
def index():
    
    return render_template('admin/index.html')

@admin.route('/categoria',methods=['GET','POST'])
def categoria():
    
    #crear formulario para el registro de nueva Categoria
    categoriaForm = CatalogoForm()
    
    #Validamos si se envio el formulario para registrar nueva categoria
    if categoriaForm.validate_on_submit():
        #registramos la nueva categoria
        descripcion = categoriaForm.descripcion.data
        cursorInsert = dbConn.cursor()
        strSqlInsert = setSqlCatalogo('categoria',descripcion)
        cursorInsert.execute(strSqlInsert)
        dbConn.commit()
        cursorInsert.close()
    
    
    #lista de categorias
    cursor = dbConn.cursor(dictionary=True)
    sqlgetData = getSqlCatalogo('categoria')
    cursor.execute(sqlgetData)
    data = cursor.fetchall()
    cursor.close()
    
    context = {
        'categorias':data,
        'form':categoriaForm
    }
    return render_template('admin/categoria.html',**context)

@admin.route('/modalidad')
def modalidad():
    cursor = dbConn.cursor(dictionary=True)
    sqlgetData = getSqlCatalogo('modalidad')
    cursor.execute(sqlgetData)
    data = cursor.fetchall()
    cursor.close()
    context = {
        'modalidades':data
    }
    
    return render_template('admin/modalidad.html',**context)

@admin.route('/jornada')
def jornada():
    #lista de categorias
    cursor = dbConn.cursor(dictionary=True)
    sqlgetData = getSqlCatalogo('jornada')
    cursor.execute(sqlgetData)
    data = cursor.fetchall()
    cursor.close()
    
    context = {
        'jornadas':data
    }
    return render_template('admin/jornada.html',**context)

@admin.route('/empresa')
def empresa():
    return render_template('admin/empresa.html')

@admin.route('/oferta')
def oferta():
    return render_template('admin/oferta.html')