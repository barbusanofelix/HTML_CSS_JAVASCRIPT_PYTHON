from django.db.backends.mysql.validation import DatabaseValidation

from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerField
from wtforms.fields.simple import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired


class ClienteForma(FlaskForm):
    # Incluimos el id pero como campo oculto
    id=HiddenField('id')
    # StringFiled : Texto. validators= Requerido
    nombre=StringField('Nombre',validators=[DataRequired()])
    # No es necesario que sea requerido ( Eso lo define uno)
    apellido = StringField('Apellido', validators=[DataRequired()])
    membresia =IntegerField('Membresia', validators=[DataRequired()])
    guardar=SubmitField('Guardar')