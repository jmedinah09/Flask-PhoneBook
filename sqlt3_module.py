import sqlite3

class sqlite_CRUD:
	def __init__(self):
		self.conn = conn = sqlite3.connect('agenda_telefonica.db')
		self.c = conn.cursor()

	def crear_tabla(self):
		sql = ''' 
			CREATE TABLE agenda (
			id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
			fullname VARCHAR (25) NOT NULL,
			phone VARCHAR (25) NOT NULL,
			email VARCHAR (15) NOT NULL)'''
		self.c.execute(sql)

	def listar_contactos(self):
		sql = "SELECT * FROM agenda"
		self.c.execute(sql)
		return self.c.fetchall()

	def listar_contactos_por_nombre(self, buscar_por):
		self.c.execute('SELECT * FROM agenda WHERE fullname=?', 
										(buscar_por,))
		return self.c.fetchall()

	def listar_contactos_por_tel(self, buscar_por):
		self.c.execute('SELECT * FROM agenda WHERE phone=?', 
										(buscar_por,))
		return self.c.fetchall()

	def listar_contactos_por_email(self, buscar_por):
		self.c.execute('SELECT * FROM agenda WHERE email=?', 
										(buscar_por,))
		return self.c.fetchall()

	def insertar_contactos(self, nombre_completo, telefono, email):
		self.c.execute("""
			INSERT INTO agenda (fullname, phone, email) 
			VALUES (?,?,?)""", 
			(nombre_completo, telefono, email))
		self.conn.commit()
		self.conn.close()

	def editar_contactos(self, id):
		self.c.execute("""SELECT * FROM agenda WHERE id = ?""",
			 (id, ))
		return self.c.fetchall()

	def actualizar_contactos(self, nombre_completo, telefono, email, id):
		self.c.execute("""
		UPDATE agenda 
		SET fullname = ?,
			phone   = ?,
			email   = ?
		WHERE id	= ?
		""", (nombre_completo, telefono, email, id))
		self.conn.commit()
		self.conn.close()
		
	def borrar_contactos(self, id):
		self.c.execute('DELETE FROM agenda WHERE id = ?', (id, ))
		self.conn.commit()
		self.conn.close()


	