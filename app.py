
from flask import Flask, render_template, request, flash
from sqlt3_module import sqlite_CRUD

app = Flask(__name__)
app.secret_key = 'hOo0laMundo'

@app.route('/', methods=['GET'])
def Index():
	db = sqlite_CRUD()
	data = db.listar_contactos()
	db.close()
	return render_template('index.html', contacts = data)

@app.route('/listar', methods=['POST'])
def show_contacts():
	db = sqlite_CRUD()
	data = db.listar_contactos()
	db.close()
	return render_template('index.html', contacts = data)

@app.route('/listar_por', methods=['GET', 'POST'])
def listar_por():
	if request.method == 'POST':
		buscar_por = request.form['buscar_por']
		select = request.form.get('dato')
		db = sqlite_CRUD()
		if select == 'nombre_completo':
			data = db.listar_contactos_por_nombre(buscar_por)
		elif select == 'telefono':
			data = db.listar_contactos_por_tel(buscar_por)
		elif select == 'email':
			data = db.listar_contactos_por_email(buscar_por)
		db.close()
		return render_template('index.html', contacts = data)

@app.route('/agregar_contacto', methods=['POST'])
def agregar_contacto():
	if request.method == 'POST':
		nombre_completo = request.form['nombre_completo']
		telefono = request.form['telefono']
		email = request.form['email']
		db = sqlite_CRUD()
		db.insertar_contactos(nombre_completo, telefono, email)
		data = db.listar_contactos()
		db.close()
		flash('Contacto Agregado Satisfactoriamente!')
		return render_template('index.html', contacts = data)

@app.route('/editar/<id>')
def editar_contact(id):
	db = sqlite_CRUD()
	data = db.editar_contactos(id)
	db.close()
	return render_template('editar_contacto.html', contact = data[0])

@app.route('/actualizar/<id>', methods = ['POST'])
def update_contact(id):
	if request.method == 'POST':
		nombre_completo = request.form['nombre_completo']
		telefono = request.form['telefono']
		email = request.form['email']
	db = sqlite_CRUD()
	db.actualizar_contactos(nombre_completo, telefono, email, id)
	data = db.listar_contactos()
	db.close()
	flash('Contacto Actualizado Satisfacoriamente')
	return render_template('index.html', contacts = data)

@app.route('/borrar_contacto/<string:id>')
def borrar_contacto_contact(id):
	db = sqlite_CRUD()
	db.borrar_contactos(id)
	data = db.listar_contactos()
	db.close()
	flash('Contacto Removido Satisfactoriamente')
	return render_template('index.html', contacts = data)
	
if __name__ == '__main__':
	app.run(debug = True)