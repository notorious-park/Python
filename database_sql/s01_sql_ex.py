import pymysql

dbcon_param = {
    'host'    : 'localhost',
    'port'    : 3306,
    'user'    : 'root',
    'passwd'  : 'password',
    'db'      : 'bpcdb',
    'charset' : 'utf8',
    'autocommit' : True
}

# Open database connection
conn = pymysql.connect(**dbcon_param)

# prepare a cursor object using cursor() method
cursor = conn.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print(type(data), len(data))
print(data[0])

conn.close()