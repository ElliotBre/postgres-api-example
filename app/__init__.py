import psycopg2
import os

user = os.environ['USER']
password = os.environ['PASSWORD']
host = os.environ['HOST']
port = os.environ['PORT']
database = os.environ['DATABASE']

conn = psycopg2.connection(
    user=user, password=password, host=host, port=port, database=database)
