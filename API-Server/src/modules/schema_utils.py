import psycopg2
from pandas import read_csv
from sqlalchemy import create_engine

conn = psycopg2.connect("dbname=postgres user=postgres password=example")
conn.autocommit = True

cur = conn.cursor()

cur.execute('DROP DATABASE IF EXISTS postgres')
cur.execute('CREATE DATABASE postgres')   

try:
    cur.execute(
        '''
        CREATE TABLE customer (cust_id integer primary key,
                                first_name varchar,
                                last_name varchar,
                                company_name varchar,
                                address varchar,
                                city varchar,|
                                state varchar,
                                zip varchar,
                                phone1 varchar,
                                phone2 varchar,
                                email varchar);
        ''')
except:
    print("Customer table already exists...")

try:
    cur.execute(
        '''
        CREATE TABLE dept (dept_id integer primary key, department varchar);
        ''')
except:
    print("Department table already exists...")

try:
    cur.execute(
        '''
        CREATE TABLE cust_dept (cust_id integer references customer(cust_id), 
                                dept_id integer references dept(dept_id));
        ''')
except:
    print("Cust_Dept table already exists...")

print("Databases created successfully........")
conn.close()


cust_df = read_csv("API-Server/src/csv/customer.csv")
dept_df = read_csv("API-Server/src/csv/dept.csv")
cust_dept_df = read_csv("API-Server/src/csv/cust_dept.csv")

engine = create_engine('postgresql://postgres:example@127.0.0.1:5432/postgres')

cust_df.to_sql(
    name='customer',
    con=engine,
    if_exists='append',
    index=False
)
dept_df.to_sql(
    name='dept',
    con=engine,
    if_exists='append',
    index=False
)
cust_dept_df.to_sql(
    name='cust_dept',
    con=engine,
    if_exists='append',
    index=False
)

print("Insertion of data successfully....")
