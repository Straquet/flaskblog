from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)
from flask_login import current_user, login_required
from flaskblog import db
from flaskblog.models import Post
from flaskblog.posts.forms import  PostForm
from flaskblog.posts.util import save_picture_casa, save_picture_casa2, save_picture_casa3, save_picture_casa4, save_picture_plano


posts = Blueprint('posts', __name__)


@posts.route('/post/new', methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        if form.picture_casa.data and form.picture_casa2.data and form.picture_casa3.data and form.picture_casa4.data:
            picture_file = save_picture_casa(form.picture_casa.data)
            picture_file2 = save_picture_casa2(form.picture_casa2.data)
            picture_file3 = save_picture_casa3(form.picture_casa3.data)
            picture_file4 = save_picture_casa4(form.picture_casa4.data)
        if form.picture_planos.data:
            picture_file5 = save_picture_plano(form.picture_planos.data)
        post = Post(title=form.title.data, image_casa=picture_file, image_casa2=picture_file2, image_casa3=picture_file3, image_casa4=picture_file4, image_plano=picture_file5,
                    direccion=form.direccion.data, antiguedad=form.antiguedad.data, cuartos=form.cuartos.data, baños=form.baños.data, estrato=form.estrato.data, garaje=form.garaje.data, sector=form.sector.data, tipo=form.tipo.data, poner=form.poner.data, precio=form.precio.data, descripcion=form.descripcion.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Se ha creado tu publicacion', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='Nueva Publicacion', form=form, legend='Nueva Publicacion')


@posts.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
        
    return render_template('post.html', title=post.title, post=post)


@posts.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit:
        if form.picture_casa.data and form.picture_casa2.data and form.picture_casa3.data and form.picture_casa4.data:
            post.picture_file = save_picture_casa(form.picture_casa.data)
            post.picture_file2 = save_picture_casa(form.picture_casa.data)
            post.picture_file3 = save_picture_casa(form.picture_casa.data)
            post.picture_file4 = save_picture_casa(form.picture_casa.data)
        if form.picture_planos.data:
            post.picture_file5 = save_picture_plano(form.picture_planos.data)
            post.title = form.title.data
            post.direccion = form.direccion.data
            post.antiguedad = form.antiguedad.data
            post.cuartos = form.cuartos.data
            post.baños = form.baños.data
            post.estrato = form.estrato.data
            post.garaje = form.garaje.data
            post.sector = form.sector.data
            post.tipo = form.tipo.data
            post.poner = form.poner.data
            post.precio = form.precio.data
            post.descripcion = form.descripcion.data
            db.session.commit()
            flash('La publicacion ha sido actualizada!', 'success')

            return redirect(url_for('posts.post', post_id=post.id))
    elif request.method == 'GET':

        form.title.data = post.title
        form.direccion.data = post.direccion
        form.antiguedad.data = post.antiguedad
        form.cuartos.data = post.cuartos
        form.baños.data = post.baños
        form.estrato.data = post.estrato
        form.garaje.data = post.garaje
        form.sector.data = post.sector
        form.tipo.data = post.tipo
        form.poner.data = post.poner
        form.precio.data = post.precio
        form.descripcion.data = post.descripcion
    return render_template('create_post.html', title='Actualizar Publicacion', form=form, legend='Actualizar Post')


@posts.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Tu publicacion ha sido borrada!', 'success')
    return redirect(url_for('main.home'))

