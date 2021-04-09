from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError
from flask_login import current_user
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Nombre de Usuario', validators=[
                           DataRequired(), Length(min=4, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[
                             DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
                                     DataRequired(), EqualTo('password'), Length(min=6)])
    submit = SubmitField('Registrarse')

    def validate_username(self, username):

        user = User.query.filter_by(username=username.data).first()

        if user:
            raise ValidationError(
                'El nombre de usuario no está disponible :(, selecciona otro diferente :)')

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError(
                'El correo no está disponible :(, selecciona otro diferente :)')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Contraseña', validators=[DataRequired()])
    remember = BooleanField('Recordarme')
    submit = SubmitField('Inicar Sesion')


class UpdateAccountFlaskForm(FlaskForm):
    username = StringField('Nombre de Usuario',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Actualizar Foto de Perfil', validators=[
                        FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Actualizar')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    'El nombre de usuario no está disponible, intenta con otro.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    'El Email no está disponible, intenta con otro.')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()

        if user is None:
            raise ValidationError(
                'No hay una cuenta con este email. Deberias registrarlo primero')

    submit = SubmitField('Solicitar Cambio de Contraseña')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Contraseña', validators=[
                             DataRequired(), Length(min=6)])
    confirm_password = PasswordField('Confirmar Contraseña', validators=[
                                     DataRequired(), EqualTo('password'), Length(min=6)])
    submit = SubmitField('Cambiar Contraseña')
    
