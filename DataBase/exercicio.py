import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = ''
)

cursor = db.cursor()
cursor.execute("SHOW DATABASES")

for c in cursor:
    print(c)

INSERT INTO