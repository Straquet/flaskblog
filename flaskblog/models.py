from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flaskblog import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(
        db.String(100), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    image_casa = db.Column(
        db.String(100), nullable=False, default='default.jpg')
    image_casa2 = db.Column(
        db.String(100), nullable=False, default='default.jpg')
    image_casa3 = db.Column(
        db.String(100), nullable=False, default='default.jpg')
    image_casa4 = db.Column(
        db.String(100), nullable=False, default='default.jpg')
    image_plano = db.Column(
        db.String(100), nullable=False, default='default.jpg')
    direccion = db.Column(db.String(100), nullable=False)
    antiguedad = db.Column(db.String(100), nullable=False)
    cuartos = db.Column(db.Integer, nullable=False)
    baños = db.Column(db.Integer, nullable=False)
    estrato = db.Column(db.String(50), nullable=False)
    garaje = db.Column(db.String(50), nullable=False)
    sector = db.Column(db.String(50), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    poner = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False,
                            default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.image_casa}', '{self.image_cas2}','{self.image_casa3}','{self.image_casa4}','{self.image_plano}','{self.direccion}','{self.antiguedad}','{self.cuartos}','{self.baños}','{self.estrato}','{self.garaje}','{self.sector}','{self.tipo}','{self.poner}','{self.precio}', '{self.descripcion}', '{self.date_posted}')"
