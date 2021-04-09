from flask import Blueprint, render_template, request, redirect
from flask.helpers import url_for
from flaskblog.models import Post

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(
        Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)


@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/apartamento')
def apartamento():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Apartamento')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route('/amoblado')
def amoblado():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Amoblado')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route('/bodega')
def bodega():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Bodega')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/casa')
def casa():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Casa')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/casa_finca')
def casa_finca():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Casa Finca')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/consultorio')
def consultorio():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Consultorio')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/comercial')
def comercial():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Comercial')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/edificios')
def edificios():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Edificios')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/finca')
def finca():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Finca')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/local')
def local():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Local')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/lote')
def lote():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.filter(Post.tipo.endswith('Lote')).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)

@main.route('/menor_mayor')
def menor_mayor():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.precio.asc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)
    
@main.route('/mayor_menor')
def mayor_menor():
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.precio.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', posts=posts)