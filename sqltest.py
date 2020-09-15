import pyodbc


def insert(CONFIG):
    print('start insert')
    with pyodbc.connect('DRIVER='+CONFIG.driver+';SERVER='+CONFIG.server+';PORT=1433;DATABASE='+CONFIG.database+';UID='+CONFIG.username+';PWD=' + CONFIG.password) as conn:
        with conn.cursor() as cursor:
            cursor.execute(
                "INSERT INTO test_table_1 (testcourse) VALUES (?)", '1630')
            cursor.commit()

    print('finish insert')
