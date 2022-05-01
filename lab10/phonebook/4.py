import psycopg2

conn = psycopg2.connect(    
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = '12345'
    )
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTs PhoneBook1 (name text unique, phone text unique)')

get = input('what kind of query you need...\n')

if get == 'name':
    phone = input('enter phone...\n')
    try:
        cursor.execute(f'SELECT name from phonebook1 where phone = \'{phone}\';')
        ans = cursor.fetchone()
        print(ans[0])
    except:
        print('name with this phone does not exist')
elif get == 'phone':
    name = input('write name...\n')
    try:
        cursor.execute(f'SELECT phone from phonebook1 where name = \'{name}\';')
        ans = cursor.fetchone()
        print(ans[0])
    except:
        print('phone with this name does not exist')   


cursor.execute('select * from PhoneBook1')
print(cursor.fetchall())
conn.commit()
cursor.close()
conn.close()

