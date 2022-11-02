from asyncio.windows_events import NULL #Para poder usar NULL en la DB
import sqlite3 as sq3
con = sq3.connect('python_sql/mi_db.db')
cur = con.cursor()

#DDL (Crear estructura)
instruccion1 = '''CREATE TABLE IF NOT EXISTS alumno(
    _id INTEGER PRIMARY KEY,
    nombre VARCHAR(50)
)'''

#con.execute(instruccion1)


#DML(Agregar Datos)
lista1 = [(1,'Silvia'),(2,'Oscar')]
lista2 = [(1,'alumno1'),(2,'alumno2')]
'''
cur.executemany('INSERT INTO persona VALUES(?,?)',lista1) # ? segun Cantidad de tuplas a agregar
cur.executemany('INSERT INTO alumno VALUES(?,?)',lista2) # ? segun Cantidad de tuplas a agregar
'''
#(ojo con NULL no existe, sino NONE)

#Consulta de datos

consulta1 = '''
    SELECT persona.nombre, alumno.nombre 
    FROM persona
    LEFT JOIN alumno ON persona._id = alumno._id
    '''
for registro in cur.execute(consulta1):
    print(registro)

con.commit()
con.close()