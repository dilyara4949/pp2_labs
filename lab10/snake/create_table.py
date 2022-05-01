import psycopg2

conn  = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    port= 5432,
    user = 'postgres',
    password = '12345'
)
cursor = conn.cursor()
cursor.execute('''
     CREATE TABLE snake(
          username VARCHAR(21),
          user_score VARCHAR(12),
          highscore VARCHAR(12),
          level VARCHAR(12)
     );
     '''
)

cursor.close()
conn.commit()
conn.close()
