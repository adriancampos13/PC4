from sqlalchemy import *

db = create_engine('sqlite:///Clase3.db')
db.echo = False

metadata = MetaData(db)

#--------

# Creacion de Tabla
#usuarios = Table('usuarios', metadata,
#                 Column('id', Integer, primary_key=True),
#                 Column('nombre', String(30)),
#                 Column('edad', Integer),
#                 Column('password',String),
#                 )
#usuarios.create()

# insercion de datos
#i = usuarios.insert()
#i.execute(nombre='Petra', edad='50', password='no_morira')
#i.execute({'nombre': 'Juan', 'edad' : 50},
#          {'nombre': 'Tiene', 'edad' : 35},
#          {'nombre': 'Hambre', 'edad' : 22})
#
# Busqueda de datos
#s = usuarios.select()
#rs = s.execute()
#fila = rs.fetchone()
#print("ID   |", fila[0])
#print("Nombre   |", fila['nombre'])
#print("Edad   |", fila.edad)
#print("Password   |", fila[usuarios.c.password])

#for fila in rs:
#    print(fila.nombre, "tiene", fila.edad, " años.")

#--------

#usuarios = Table('usuarios', metadata, autoload=True)

#def ejecutar(stnc):
#    rs = stnc.execute()
#    for fila in rs:
#        print(fila)

#s = usuarios.select(usuarios.c.nombre == 'Juan')
#ejecutar(s)
#s = usuarios.select(usuarios.c.edad < 30)
#ejecutar(s)
#s = usuarios.select(and_(usuarios.c.edad < 35, usuarios.c.nombre != 'Tiene'))
#ejecutar(s)
#s = usuarios.select(or_(usuarios.c.edad < 35, usuarios.c.nombre != 'Petra'))
#ejecutar(s)
#s = usuarios.select((usuarios.c.edad < 35) & (usuarios.c.nombre != "Hambre"))
#ejecutar(s)
#s = usuarios.select((usuarios.c.edad < 35) | (usuarios.c.nombre != "Hambre"))
#ejecutar(s)
#s = usuarios.select(usuarios.c.nombre.startswith('P'))
#ejecutar(s)
#s = usuarios.select(usuarios.c.edad.between(15,30))
#ejecutar(s)
#s = select([func.count("*")], from_obj=[usuarios])
#ejecutar(s)

#--------

usuarios = Table('usuarios', metadata,
     Column('usuario_id', Integer, primary_key=True),
     Column('nombre', String(30)),
     Column('edad', Integer),
 )
#usuarios.create()

correos = Table('correos', metadata,
     Column('correo_id', Integer, primary_key=True),
     Column('direccion', String),
     Column('usuario_id', Integer, ForeignKey('usuarios.usuario_id')),
 )
# correos.create()
#
# i = usuarios.insert()
# i.execute(
#     {'nombre': 'Petra', 'edad': 50},
#     {'nombre': 'Juana', 'edad': 45},
#     {'nombre': 'Xenoiba', 'edad': 17},
#     {'nombre': 'Tinoca', 'edad': 35}
# )
# i = correos.insert()
# i.execute(
#     # There's a better way to do this, but we haven't gotten there yet
#     {'direccion': 'petra@ph.com', 'usuario_id': 1},
#     {'direccion': 'juana@nidea.com', 'usuario_id': 2},
#     {'direccion': 'john@ejemplo.com', 'usuario_id': 2},
#     {'direccion': 'xnb@ph.com', 'usuario_id': 4},
# )


def ejecutar(stnc):
    rs = stnc.execute()
    for fila in rs:
        print(fila)


#s = select([usuarios, correos])
#ejecutar(s)

s = select([usuarios, correos], correos.c.usuario_id == usuarios.c.usuario_id)
ejecutar(s)

s = select([usuarios.c.nombre, correos.c.direccion],
           correos.c.usuario_id == usuarios.c.usuario_id)
ejecutar(s)

#s = join(usuarios, correos).select()
#ejecutar(s)


#s = outerjoin(usuarios, correos).select()
#ejecutar(s)