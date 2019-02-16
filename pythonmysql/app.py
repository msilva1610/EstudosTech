import pymysql

db = pymysql.connect("192.168.90.20","vagrant","vagrant","testedb" )
cursor = db.cursor()
cursor.execute("select version()")

data = cursor.fetchone()

print("Versão do database mysql: {}".format(data))

# Resultado
# Versão do database mysql: ('5.5.62-0ubuntu0.14.04.1',)

db.close()