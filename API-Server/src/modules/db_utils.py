from json import dumps
from dataclasses import dataclass,field
from psycopg2 import connect
from pandas import read_sql_query, DataFrame


@dataclass(frozen=True)
class DB_API:
    dbname : str = "postgres"
    user : str ="postgres"
    password : str ="example"
    conn_string : str = field(init=False)
    conn : None = field(init=False)
    cur : None = field(init=False)


    def __post_init__(self):
        object.__setattr__(self,'conn_string',f"dbname={self.dbname} user={self.user} password={self.password}")
        object.__setattr__(self,'conn',connect(self.conn_string))
        self.conn.autocommit = True
        object.__setattr__(self,'cur', self.conn.cursor())


    def conn_close(self):
        self.conn.close()


    def get_clients_dept(self) -> tuple:
        query = '''SELECT customer.*,dept.department FROM customer,dept,cust_dept
                   WHERE customer.cust_id = cust_dept.cust_id
                   and dept.dept_id = cust_dept.dept_id
                '''
        df : DataFrame = read_sql_query(query, self.conn)
        json_string = dumps(df.to_dict(orient='records'), indent=4)
        return json_string, 200
    

    def get_client(self, id:str) -> tuple:
        query = f'''SELECT * FROM customer
                   WHERE customer.cust_id = {id}
                '''
        df : DataFrame = read_sql_query(query, self.conn)
        json_string = dumps(df.to_dict(orient='records'), indent=4)
        return json_string, 200
    

    def create_client(self, args) -> tuple:
        client_attr = ["cust_id","first_name","last_name","company_name","address",
                    "city","state","zip","phone1","phone2","email"]
        dict_args = {key:str() for key in client_attr}
        for key, values in args: dict_args[key] = values[0]

        query = f'''INSERT INTO customer(cust_id,first_name,last_name,company_name,address,city,state,zip,phone1,phone2,email)
                    VALUES ({dict_args['cust_id']},{dict_args['first_name']},{dict_args['last_name']},{dict_args['company_name']},
                    {dict_args['address']},{dict_args['city']},{dict_args['state']},{dict_args['zip']},{dict_args['phone1']},{dict_args['phone2']},{dict_args['email']})
                '''
        if len(dict_args['state']) == 2 and dict_args['state'].isalpha() and dict_args['state'].isupper():
            self.cur.execute(query)
            return dumps(dict_args, indent=4), 200
        else:
            return "ERROR on request (state field)", 400


    def update_client_attr(self, id:str, column:str, insert:str) -> tuple:
        client_attr = ["cust_id","first_name","last_name","company_name","address",
                    "city","state","zip","phone1","phone2","email"]
        if not column in client_attr: return "Error on request (bad column name)", 400

        query = f'''UPDATE customer
                    SET {column} = '{insert}'
                    WHERE customer.cust_id = {id}
        '''
        if column == "state" and len(insert) == 2 and insert.isalpha() and insert.upper():
            self.cur.execute(query)
            return self.get_client(id)
        else:
            return "Error on request (state field)", 400


    def delete_client(self, id:str) -> tuple:
        query01 = f'''DELETE FROM customer
                   WHERE customer.cust_id = {id}
                '''
        query02 = f'''DELETE FROM cust_dept
                   WHERE cust_dept.cust_id = {id}
                '''
        self.cur.execute(query02)
        self.cur.execute(query01)
        return f"Client {id} deleted", 200