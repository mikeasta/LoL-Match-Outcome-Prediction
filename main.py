import psycopg2
import subprocess
from server import PostgreSQLServer

def main():
    try:
        # пытаемся подключиться к базе данных
        connection = psycopg2.connect(
            dbname='league_of_legends_match_database', 
            user='postgres', 
            password='123456', 
            host='localhost', 
            port="5432"
        )

        # Open a cursor to perform database operations
        with connection.cursor() as cursor:
            # Execute a query
            cursor.execute("SELECT * FROM test;")

            # Retrieve query results
            records = cursor.fetchall()
            print(records)
    except Exception as e:
        # в случае сбоя подключения будет выведено сообщение в STDOUT
        print(f'Can`t establish connection to database, due to error {e}')
    finally:
        connection.close()
        print("[INFO]: Connection closed")

server = PostgreSQLServer()
subprocess.Popen(server.run())