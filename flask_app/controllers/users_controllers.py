from flask_app import app

from flask import Flask, render_template, request, redirect

from flask_app.models.users import User

@app.route('/')
def index():
    users = User.muestra_usuarios()
    return render_template('index.html',user = users)

@app.route('/new')
def new_page():
    
    return render_template('new.html' )

@app.route('/create', methods = ['POST'])
def create():
    
    user = User.save(request.form)  
    
    return redirect ('/show/'+ str(user))

@app.route('/show/<int:id>') 
def show(id): 
    formulario = { 
        "id": id
    }
    user = User.muestra_usuario(formulario)
    return render_template('user.html', usuario = user, id = formulario)


@app.route('/delete/<int:id>') 
def delete(id): 
    formulario = { 
        "id": id
    }
    User.borrar(formulario)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit_page(id):
    formulario = { 
        "id": id
    }
    user = User.muestra_usuario(formulario)
    return render_template('edit_user.html',id = formulario, user = user)


@app.route('/update', methods = ['POST'])
def update():
    
    User.update(request.form)
    id = request.form['id']

    return redirect ('/show/'+ id)
    











