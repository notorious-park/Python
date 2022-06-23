from day99.database import common as dbcomm
from day99.database import common2 as dbcomm2
import pandas as pd

# 1개 데이터 출력하기
def select_one_books(db_name):
    """
    최상단 하나의 데이터를 조회하는 함수
    Args:
    db_name : Database Name
    number : Count of data to query
    Returns :
    is_success : Boolean
    ret_df : DataFrame of books
    """
    ret_df = pd.DataFrame()
    is_success = True

    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomm.get_connection(db_name)
        cur = conn.cursor()

        # 조회용 SQL 실행
        db_sql = "SELECT * FROM book_mgr"
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[2] 데이터 일부 출력하기')
        book = cur.fetchone()
        books = [book]

        ret_df = dbcomm2.getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        # 데이터베이스 커넥션 닫기
        conn.close()

    return is_success, ret_df

if __name__ == "__main__":

    db_name = 'jbfgtest'

    is_success, books_df = select_one_books(db_name)
    if is_success:
         print('하나의 데이터를 성공적으로 조회하였습니다.')
    else :
         print('데이터를 조회하지 못했습니다')

    print(books_df)