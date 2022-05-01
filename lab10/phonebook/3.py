import psycopg2

conn = psycopg2.connect(    
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = '12345'
    )
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTs PhoneBook1 (name text unique, phone text)')

inp = input('select the value you want update...\n')

if inp == 'name':
    name = input('enter name you want update..\n')
    new_name = input('enter new name...\n')
    try:
        update = f'update Phonebook1 set name = \'{new_name}\' where name = \'{name}\''
        cursor.execute(update)
    except:
        print('old name is not exist')
elif inp == 'phone':
    name = input('enter name whose phone you want update..\n')
    new_phone = input('enter new phone...\n')
    try:
        update = f'update Phonebook1 set phone = \'{new_phone}\' where name = \'{name}\''
        cursor.execute(update)
    except:
        print('old phone is not exist')




cursor.execute('select * from PhoneBook1')
print(cursor.fetchall())
conn.commit()
cursor.close()
conn.close()

