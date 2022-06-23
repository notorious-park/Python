import pymysql

dbcon_param = {
    'host' : 'localhost',
    'port' : 3306,
    'user' : 'root',
    'passwd' : 'password',
    'db' : 'jbfgtest',
    'charset' : 'utf8',
    'autocommit' : True
}

conn = pymysql.connect(**dbcon_param)

cursor = conn.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

print(type(data), len(data))
print(data[0])

conn.close()