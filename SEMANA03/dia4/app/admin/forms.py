from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import StringField,SubmitField,TextAreaField,SelectField,DecimalField

from app import dbConn

def obtenerDatosCatalogo(strSql):
    cursor = dbConn.cursor()
    cursor.execute(strSql)
    data = cursor.fetchall()
    cursor.close()
    return data

class CatalogoForm(FlaskForm):
    descripcion = StringField('Descripción',validators=[DataRequired()])
    submit = SubmitField('Guardar')
    
class EmpresaForm(FlaskForm):
    nombre = StringField('Nombre Empresa',validators=[DataRequired()])
    descripcion = StringField('Descripcion')
    logo = StringField('Logo')
    beneficios = StringField('Beneficios')
    submit = SubmitField('Guardar')
    
class OfertaForm(FlaskForm):
    titulo = StringField('Titulo',validators=[DataRequired()])
    descripcion = TextAreaField('Descripción')
    requerimientos = TextAreaField('Requerimientos')
    salario = DecimalField(places=2, rounding=None, validators=[DataRequired()])
    url = StringField('Url',validators=[DataRequired()])
    empresa = SelectField('Empresa',choices=obtenerDatosCatalogo('select empresa_id as id,empresa_nombre as descripcion from tbl_empresa'))
    categoria = SelectField('Categoria',choices=obtenerDatosCatalogo('select categoria_id as id,categoria_descripcion as descripcion from tbl_categoria'))
    experiencia = SelectField('Experiencia',choices=obtenerDatosCatalogo('select experiencia_id as id,experiencia_descripcion as descripcion from tbl_experiencia'))
    jornada = SelectField('Jornada',choices=obtenerDatosCatalogo('select jornada_id as id,jornada_descripcion as descripcion from tbl_jornada'))
    modalidad = SelectField('Modalidad',choices=obtenerDatosCatalogo('select modalidad_id as id,modalidad_descripcion as descripcion from tbl_modalidad'))
    submit = SubmitField('Guardar')