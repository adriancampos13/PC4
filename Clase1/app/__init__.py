import pymysql

db = pymysql.connect("localhost", "root", "Admin01", "Empleado")
#db = pymysql.connect(host='localhost', port=3306, user='admin', passwd='Admin01', db='employees')
cursor = db.cursor()

# Prueba de Instalacion de MYSQL

#cursor.execute("select version()")
#data = cursor.fetchone()
#print("version de MySQL: %s" % data)
#db.close()

#-------------

# Eliminacion / creacion de tablas

#cursor.execute("DROP TABLE IF EXISTS empleado")
#sql = """CREATE TABLE EMPLEADO (NOMBRE VARCHAR(20) NOT NULL, APELLIDO VARCHAR(20), EDAD INT,  SEXO CHAR(1), SALARIO FLOAT);"""

#db.close()

#---------------
# Insertar datos a la tabla

#sql = """INSERT INTO EMPLEADO(NOMBRE,APELLIDO,EDAD,SEXO,SALARIO)
#VALUES('Petra', 'Petrov', 32, 'F',7000)"""
#try:
#    cursor.execute(sql)
#    db.commit()
#except:
#    db.rollback()

#db.close()

#----------------
# Leer datos de la tabla de empleados

e = int(input("Edad de Petra> "))
salarios = []
sql = "Select * from empleado where edad > '%d'" % e

try:
    cursor.execute(sql)
    resultados = cursor.fetchall()
    for registro in resultados:
        salario = registro[4]
        salarios.append(salario)
except:
    print("Error al obtener datos! ")
db.close()

if len(salarios) > 0:
    print("El Salario mas alto de Petra fue de $" + str(max(salarios)))
else:
    print("No hay Salario de Petra para ese rango de edad")


#----------------

# Actualizar datos

#sql = "UPDATE EMPLEADO SET EDAD = EDAD + 1 WHERE SEXO = 'F'"

#try:
#    cursor .execute(sql)
#    db.commit()
#except:
#    db.rollback()
#db.close()

# Borrar datos

#sql = "DELETE FROM EMPLEADO WHERE EDAD < 18"

#try:
#    cursor .execute(sql)
#    db.commit()
#except:
#    db.rollback()
#db.close()