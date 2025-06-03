from flask import Blueprint, render_template, request, redirect, url_for
from app import db
from app.models import Nota

nota_bp = Blueprint('notas', __name__)

@nota_bp.route('/')
def listar_notas():
    notas = Nota.query.all()
    return render_template('index.html', notas=notas)

@nota_bp.route('/nuevo', methods=['GET', 'POST'])
def nueva_nota():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descripcion = request.form['descripcion']
        
        nuevo = Nota(titulo=titulo, descripcion=descripcion)
        db.session.add(nuevo)
        db.session.commit()
        return redirect(url_for('notas.listar_notas'))
    return render_template('form.html')

@nota_bp.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar_nota(id):
    nota = Nota.query.get_or_404(id)
    if request.method == 'POST':
        nota.titulo = request.form['titulo']
        nota.descripcion = request.form['descripcion']
        db.session.commit()
        return redirect(url_for('notas.listar_notas'))
    return render_template('form.html', nota=nota)

@nota_bp.route('/eliminar/<int:id>')
def eliminar_nota(id):
    contacto = Nota.query.get_or_404(id)
    db.session.delete(contacto)
    db.session.commit()
    return redirect(url_for('notas.listar_notas'))