from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from wtforms.fields import StringField,SubmitField

class CatalogoForm(FlaskForm):
    descripcion = StringField('Descripción',validators=[DataRequired()])
    submit = SubmitField('Guardar')