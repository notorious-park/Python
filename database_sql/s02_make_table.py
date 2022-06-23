# import pymysql
from sect15_database.database import common as dbcomm

def create_table(db_name, db_sql):
    is_success = True

    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomm.get_connection(db_name)

        # 커서 확보
        cur = conn.cursor()

        # 테이블 생성
        cur.execute(db_sql)

    except Exception as err:
        is_success = False
        print("Error : {}".format(err))

    finally:
        if is_success:
            # 데이터베이스 반영
            # print("테이블을 성공적으로 생성하였습니다.")
            conn.commit()
        else:
            # 데이터베이스 철회
            # print("테이블을 생성하지 못했습니다.")
            conn.rollback()

        # 데이터베이스 커넥션 닫기
        conn.close()

    return is_success

db_name = 'bpcdb'
db_sql  = '''
CREATE TABLE book_mgr (
    title text,
    published_date text,
    publisher text,
    pages integer,
    recommendation integer
)
'''

if __name__=="__main__":

    is_success = create_table(db_name, db_sql)

    if is_success:
        print('테이블이 성공적으로 생성되었습니다.')
    else:
        print('테이블이 생성되지 않았습니다.')
