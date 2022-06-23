import pymysql


def get_connection(db_name):
    dbcon_param = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',
        'passwd': 'password',
        'db': db_name,
        'charset': 'utf8',
        'autocommit': True
    }

    try:
        # conn = pymysql.connect(db=db_name, **dbcon_param)
        conn = pymysql.connect(**dbcon_param)
    except Exception as err:
        print('데이터베이스에 접속을 할 수 없습니다.')
        print('DB Connection Error : {}'.format(err))

    return conn