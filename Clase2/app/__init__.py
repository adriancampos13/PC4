import sqlite3

#db = sqlite3.connect(':memory') # solo en memoria
#db = sqlite3.connect('data/prueba') # si esta guardando en un archivo

#cursor = db.cursor()

    # para crear data data

#cursor.execute('''
#    CREATE TABLE usuario(id INTEGER PRIMARY KEY, nombre TEXT,
#                       telefono TEXT, email TEXT unique, password TEXT)
#''')
#db.commit()

    # para borrar table

#cursor.execute('''DROP TABLE usuario''')
#db.commit()

    # para Insertar data

#nombre = input("Nombre: ")
#telefono = input("Telefono: ")
#email = input("Email: ")
#password = input("Password: ")

#cursor.execute('''INSERT INTO usuario(nombre, telefono, email, password)
#                    VALUES(?,?,?,?)''', (nombre, telefono, email, password))

#cursor.execute('''INSERT INTO usuario(nombre, telefono, email, password)
#                    VALUES(:nombre,:telefono,:email,:password)''',
#               {'nombre':nombre, 'telefono':telefono, 'email':email, 'password':password})

    # para Consultar data

#cursor.execute('''SELECT nombre, email, telefono FROM usuario''')
#resultado = cursor.fetchall()
#for fila in resultado:
#    print("{0} : {1}, {2}".format(fila[0], fila[1], fila[2]))

    # para Actualizar data

#cursor.execute('''SELECT id, nombre FROM usuario''')
#resultado = cursor.fetchall()
#for fila in resultado:
#    print("{0} : {1}".format(fila[0], fila[1]))

#id = input("ID de usuario a modificar: ")
#for fila in resultado:
#    if int(id) == int(fila[0]):
#        nuevo_nombre = input("Nombre Nuevo: ")
#        cursor.execute('''UPDATE usuario SET nombre = ? WHERE
#                            id = ?''', (nuevo_nombre, id))

    #Para borrar data

#cursor.execute('''SELECT id, nombre FROM usuario''')
#resultado = cursor.fetchall()
#for fila in resultado:
#    print("{0} : {1}".format(fila[0], fila[1]))

#id = input("ID de usuario a eliminar: ")
#for fila in resultado:
#    if int(id) == int(fila[0]):
#        nuevo_nombre = input("Nombre Nuevo: ")
#        cursor.execute('''DELETE FROM usuario WHERE
#                            id = ?''', (id))


###  Funciones

import hashlib

def cifrar_password(password):
    cifrado = hashlib.sha3_512(password.encode('utf-8')).hexdigest()
    return cifrado

db = sqlite3.connect('data/prueba') # Base de datos en un archivo
db.create_function('cifrar', 1, cifrar_password)
cursor = db.cursor()
cursor.execute('''CREATE TABLE clave(id INTEGER PRIMARY KEY, email TEXT, password TEXT)''')
usuario = input("Correo: ")
password = input("Password: ")
cursor.execute('''INSERT into clave(email, password) VALUES
                    (?, cifrar(?))''', (usuario, password))

db.commit()
db.close() #cierra la DB

