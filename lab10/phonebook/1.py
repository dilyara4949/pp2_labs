import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = '12345'
)

sql = '''
create table PhoneBook1(
    user_name  text,
    phone   text
)
'''

cursor = conn.cursor()
try:
    cursor.execute(sql)
except:
    pass

conn.commit()
cursor.close()
conn.close()

