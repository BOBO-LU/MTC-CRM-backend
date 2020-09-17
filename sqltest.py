import pyodbc
import os



def insert(CONFIG):
    print('start insert')
    with pyodbc.connect('DRIVER='+SQLAZURECONNSTR_Drive+';SERVER='+SQLAZURECONNSTR_Server+';PORT=1433;DATABASE='+SQLAZURECONNSTR_Database+';UID='+SQLAZURECONNSTR_Username+';PWD=' + SQLAZURECONNSTR_Password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO test_table_1 (testcourse) VALUES (?)", '1630')
            cursor.commit()

    print('finish insert')

def insert_test(CONFIG):
    print('start insert_test')
    with pyodbc.connect('DRIVER='+CONFIG.Drive+';SERVER='+CONFIG.Server+';PORT=1433;DATABASE='+CONFIG.Database+';UID='+CONFIG.Username+';PWD=' +CONFIG.Password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO test_table_1 (testcourse) VALUES (?)", '1630')
            cursor.commit()

    print('finish insert_test')