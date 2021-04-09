from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, SelectField, SubmitField,TextAreaField, IntegerField, FloatField
from wtforms import validators
from wtforms.validators import DataRequired, Email, Length
from wtforms.widgets.core import TextArea


class PostForm(FlaskForm):
    title = StringField('Titulo', validators=[DataRequired(), Length(
        max=50)], render_kw={"placeholder": "Titulo"})
    picture_casa = FileField('Subir Foto del Inmueble', validators=[
                             FileAllowed(['jpg', 'png', 'jpeg']), DataRequired()])
    picture_casa2 = FileField('Subir Foto del Inmueble', validators=[
        FileAllowed(['jpg', 'png', 'jepg']), DataRequired()])
    picture_casa3 = FileField('Subir Foto del Inmueble', validators=[
        FileAllowed(['jpg', 'png', 'jpeg']), DataRequired()])
    picture_casa4 = FileField('Subir Foto del Inmueble', validators=[
        FileAllowed(['jpg', 'png', 'jpeg']), DataRequired()])
    picture_planos = FileField('Subir imagen de los planos', validators=[
                               FileAllowed(['jpg', 'png', 'jpeg'], DataRequired())])
    direccion = StringField('Direccion', validators=[DataRequired(), Length(
        max=50)], render_kw={"placeholder": "Direccion"})
    antiguedad = StringField('Antiguedad', validators=[DataRequired()], render_kw={
        "placeholder": "Ej. 12 años"})
    cuartos = IntegerField('No. Cuartos', validators=[DataRequired()], render_kw={
                           "placeholder": "Ej. 4 "})
    baños = IntegerField('No. Baños', validators=[
                         DataRequired()], render_kw={"placeholder": "Ej. 2"})
    select_estrato = [(' 1', ' 1'), (' 2', '2'), ('3', ' 3'),
                      ('4', '4'), ('5', ' 5'), ('6', ' 6')]
    estrato = SelectField(u'Estrato', choices=select_estrato)
    select_garaje = [('Sí', 'Sí'), ('Sí', 'No')]
    garaje = SelectField(u'Garaje', choices=select_garaje)
    select_sector = [('Norte', 'Norte'), ('Sur', 'Sur'),
                     ('Este', 'Este'), ('Oeste', 'Oeste')]
    sector = SelectField(u'Sector', choices=select_sector)
    select_tipo = [('Apartamento', 'Apartamento'), ('Amoblado', 'Amoblado'), ('Bodega', 'Bodega'),
                   ('Casa', 'Casa'), ('Casa Finca', 'Casa Finca'), ('Consultorio', 'Consultorio'), ('Comercial', 'Comercial'), ('Edificios', 'Edificios'), ('Finca', 'Finca'), ('Local', 'Local'), ('Lote', 'Lote')]
    tipo = SelectField(u'Categoria', choices=select_tipo)
    select_poner = [('Venta', 'Venta'), ('Arriendo',
                                         'Arriendo'), ('Alquiler', 'Alquiler')]
    poner = SelectField(u'Poner', choices=select_poner)

    precio = StringField('Precio $', validators=[
                         DataRequired() ], render_kw={"placeholder": "COP"})
    descripcion = TextAreaField('Descripcion', validators=[DataRequired()], render_kw={
                                "placeholder": "Escriba una breve descripcion del inmueble"})
    submit = SubmitField('Publicar')


