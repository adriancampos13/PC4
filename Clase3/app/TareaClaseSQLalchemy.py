from sqlalchemy import *

#import sqlite3

# Tarea - Biblioteca - SQLite & Python
# Adrian Campos - 25/09/2017

# Conexion con Base de Datos Sqlite3

#db = sqlite3.connect('data/Biblioteca')
#cursor = db.cursor()

db = create_engine('sqlite:///TareaSQLaclchemy.db')
db.echo = False

metadata = MetaData(db)


# # Comprueba si la tabla existe, en caso de no existir la crea
# #cursor.execute("""CREATE TABLE IF NOT EXISTS libros (autor TEXT, titulo TEXT, publicacion TEXT)""")
# #cursor.close()
#creacion de tabla
# libros = Table('libros', metadata,
#                Column ('autor', String),
#                Column ('titulo', String),
#                Column ('publicacion', String),
# )
# libros.create()
#
# # insercion de datos
#
# i = libros.insert()
# i.execute(autor='Adrian',titulo='El Hombre de la Mancha',publicacion=' Septiembre 2011')
# i.execute(  {'autor': 'Juan', 'titulo':'El pantanal', 'publicacion': ' Abril 2009'},
#             {'autor': 'Fernando', 'titulo':'Economia', 'publicacion': 'Agosto 2013'},
#             {'autor': 'Ricardo', 'titulo':'Ciencias Navales', 'publicacion': ' Enero 1999'},
#           )

# #Busqueda de Datos
#
# s = libros.select()
# rs = s.execute()
# fila = rs.fetchone()
# print("Autor | ", fila['autor'])
# print("Titulo | ", fila['titulo'])
# print("Publicacion | ", fila['publicacion'])

 def agregar():
    """Agrega un nuevo libro a la Biblioteca"""

     print(
     "Agregar Libro")
     print(
     "----------------")
     print(
     "")

 #    db = sqlite3.connect('data/Biblioteca')
#     cursor = db.cursor()
#
     Autor = input("Autor: ")
     Titulo = input("Titulo: ")
     Publicacion = input("Publicacion: ")
#




#     cursor.execute("insert into libros (autor, titulo, publicacion) values ('%s','%s','%s')" % (
#     Autor, Titulo, Publicacion))
#
#     db.commit()
#
#     print(
#     "Los datos fueron agregados correctamente")
#
#     cursor.close()
#     main()
#
#
# def consultar():
#     """Lista todos los libros de la Biblioteca"""
#
#     print(
#     "Lista de publicacion")
#     print(
#     "------------------")
#     print(
#     "")
#
#     db = sqlite3.connect('data/Biblioteca')
#     cursor = db.cursor()
#
#     cursor.execute("SELECT * FROM libros")
#     resultado = cursor.fetchall()
#
#     for fila in resultado:
#          print("Autor: {0}, Titulo: {1}, Publicacion: {2}".format(fila[0], fila[1], fila[2]))
#
#     cursor.close()
#
#     print(
#     "")
#     input("Presione una tecla para continuar...")
#     main()
#
#
# def buscar():
#     """Busca un libro en la Biblioteca y lo lista"""
#
#     print(
#     "Buscar Libro")
#     print(
#     "---------------")
#     print(
#     "")
#
#     db = sqlite3.connect('data/Biblioteca')
#     cursor = db.cursor()
#
#     buscar = input("Libro a buscar: ")
#
#     #cursor.execute("SELECT * FROM libros WHERE titulo = '%s'" '('%'' (buscar))
#     cursor.execute("select * from libros where titulo like ?", ('%'+buscar+'%',))
#     x = cursor.fetchall()
#
#     for i in x:
#          print("Autor: {0}, Titulo: {1}, Publicacion: {2}".format(i[0], i[1], i[2]))
#
#     cursor.close()
#
#     print(
#     "")
#     input("Presione una tecla para continuar...")
#     main()
#
#
# def eliminar():
#     """Elimina un Libro de la Biblioteca"""
#
#     print(
#     "Eliminar Libro")
#     print(
#     "-----------------")
#     print(
#     "")
#
#     db = sqlite3.connect('data/Biblioteca')
#     cursor = db.cursor()
#
#     eliminar = input("Nombre del Libro a eliminar: ")
#
#     #cursor.execute("DELETE FROM libros WHERE titulo='%s'" % (eliminar))
#     cursor.execute("DELETE FROM libros WHERE titulo like ?", ('%' + eliminar + '%',))
#
#     db.commit()
#
#     cursor.close()
#
#     print(
#     "Libro eliminado correctamente...")
#     input()
#     main()
#
#
# def main():
#     """Funcion principal de la Biblioteca o Menu"""
#
#     print(
#     "-----------------------------------------")
#     print(
#     "   Bibliteca UIP 2017 ")
#     print(
#     "-----------------------------------------")
#     print(
#     """
# 	[1] Agregar Libros
# 	[2] Listar Libros
# 	[3] Buscar Libros
# 	[4] Quitar Libros
# 	[0] Salir
# 	""")
#
#     opcion = input("Ingresa una opción -> ")
#
#     if opcion != "1" and opcion != "2" and opcion != "3" and opcion != "4" and opcion != "5" and opcion != "0":
#         print(
#         "Opcion incorrecta")
#         input()
#         main()
#     elif opcion == "1":
#
#         agregar()
#     elif opcion == "2":
#
#         consultar()
#     elif opcion == "3":
#
#         buscar()
#     elif opcion == "4":
#
#         eliminar()
#     elif opcion == "0":
#         print(
#         "")
#         print(
#         "Bye...")
#         print(
#         "")
#         print(
#         "")
#
#         exit()
#
# main()