from flask import Flask,render_template,request

from . import admin

#importamos connDb para mysql
from app import dbConn

#importamos formularios
from .forms import CatalogoForm,EmpresaForm

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

@admin.route('/modalidad',methods=['GET','POST'])
def modalidad():
    
    modalidadForm = CatalogoForm()
    
    if(modalidadForm.validate_on_submit()):
        descripcion = modalidadForm.descripcion.data
        cursorInsert = dbConn.cursor()
        strSqlInsert = setSqlCatalogo('modalidad',descripcion)
        cursorInsert.execute(strSqlInsert)
        dbConn.commit()
        cursorInsert.close()
    
    cursor = dbConn.cursor(dictionary=True)
    sqlgetData = getSqlCatalogo('modalidad')
    cursor.execute(sqlgetData)
    data = cursor.fetchall()
    cursor.close()
    context = {
        'form':modalidadForm,
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

@admin.route('/empresa',methods=['GET','POST'])
def empresa():
    empresaForm = EmpresaForm()
    
    if empresaForm.validate_on_submit():
        nombre = empresaForm.nombre.data
        descripcion = empresaForm.descripcion.data
        logo = empresaForm.logo.data
        beneficios = empresaForm.logo.data
        strSqlInsert = """
                       insert into tbl_empresa(empresa_nombre,empresa_descripcion,empresa_logo) 
                       values('"""+nombre+"""','"""+descripcion+"""',
                       '"""+logo+"""');
                       """
        cursorInsert = dbConn.cursor()
        cursorInsert.execute(strSqlInsert)
        dbConn.commit()
        
        cursorInsert.close()
        
        
    context = {
        'form':empresaForm
    }
    return render_template('admin/empresa.html',**context)

@admin.route('/oferta')
def oferta():
    return render_template('admin/oferta.html')