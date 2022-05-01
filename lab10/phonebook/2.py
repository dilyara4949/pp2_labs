import psycopg2, csv

conn = psycopg2.connect(    
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = '12345'
    )
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTs PhoneBook1 (name text unique, phone text)')

inp = input('select way of inserting data: from terminal or csv file...\n')

if inp == 'ter':
    name = input('Enter name...\n')
    phone = input('Enter phone...\n')
    try:
        insert_into = f'INSERT INTO PhoneBook1 values (\'{name}\', \'{phone}\')'
        cursor.execute(insert_into)
    except:
        print('phone number already exis')
elif inp == 'csv':
    with open('data.csv', 'r') as f:
        data = csv.reader(f, delimiter = ',')
        for line in data:
            try:
                cursor.execute('select * from PhoneBook1')
                all_data = cursor.fetchall()
                if (line[0], line[1]) not in all_data:
                    insert_into = f'insert into PhoneBook1 values (\'{line[0]}\', \'{line[1]}\')'
                    cursor.execute(insert_into)
            except:
                print('data from file with this name was already transformed')



cursor.execute('select * from PhoneBook1')
print(cursor.fetchall())
conn.commit()
cursor.close()
conn.close()

