import psycopg2

conn = psycopg2.connect("user=postgres password=example")
cur = conn.cursor()

cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = 'xal_db'")
exists = cur.fetchone()
if not exists:
    cur.execute('CREATE DATABASE xal_db')
# rest of the script

#Create cust-dept database
cur.execute(
    '''
    CREATE TABLE customer (cust_id integer primary key,
                            first_name varchar,
                            last_name varchar,
                            company_name varchar,
                            address varchar,
                            city varchar,
                            state varchar,
                            zip integer,
                            phone1 varchar,
                            phone2 varchar,
                            email varchar);
    ''')
#Create cust-dept database
cur.execute(
    '''
    CREATE TABLE dept (dept_id integer primary key, department varchar);
    ''')

#Create cust-dept database
cur.execute(
    '''
    CREATE TABLE cust-dept (cust_id integer references customer(cust_id), 
                            dept_id integer references dept(dept_id));
    ''')

#Creating a database
print("Databases created successfully........")

#Closing the connection
conn.close()