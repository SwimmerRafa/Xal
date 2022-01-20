# Xal
_Python Flask project that ceats API to retrieve and manipulate postgresql database, made the ingestion from a csv file_

## Getting started 🚀
_This are the steps we need to follow to run our application_

1. Locate yourself in your user of the CENTOS server.
2. Once you are in your user, clone this repository.
3. Locate yourself in the API directory, and run the following command to install the libraries needed for the project
```
PATH/Xal/API-Server$ pip install -r requirements.txt
```
4. If its the first time running the application, you will need to run the file schema_utils.py, in order to create the tables inside the postgres database and to make the bulk ingestion from the csvs. The files 'cust_dept.csv', 'customer.cs', 'dept.csv', were previously created using pandas, with console line.
```
/PATH/Xal/API-Server$ python schema_utils.py
```
## Run the server 🚀
_To run the application you need to have initiated your postgres server and being located on the path where you have the project_
```
/PATH/Xal/API-Server$ python run.p
```
## E-R
_This is the E-R created to normilize the csv entry_
![alt text](https://github.com/SwimmerRafa/Xal/blob/main/E-R.png)
