from dbfpy import dbf
import sqlite3
from decimal import *

file = './data.dbf'
dbfFile = dbf.Dbf(file)

connection = sqlite3.connect('../robame_bbdd')
ado = connection.cursor()

# Se va a usar los campos de modo que se ajusten al modelo definido en Django para la tabla Ciudad
# - CODCP (5) --> codigoCiudad
# - XGD (14) --> latitudCiudad
# - YGD (15) --> longitudCiudad
# - NOMCP (6) --> nombreCiudad
# - DEP (2) --> departamento
# - PROV (3) --> provincia
# - DIST (4) --> distrito

for item in range(len(dbfFile)):
	sql = "INSERT INTO robame_ciudad(codigoCiudad, latitudCiudad, longitudCiudad, nombreCiudad, departamento, provincia, distrito) VALUES ('%s',%f,%f,'%s','%s','%s','%s')" % (dbfFile[item][4], dbfFile[item][13], dbfFile[item][14], dbfFile[item][5].replace("'", ""), dbfFile[item][1], dbfFile[item][2], dbfFile[item][3])
	ado.execute(sql)
connection.commit()
connection.close()
