from day99.database import common as dbcomm
from day99.database import common2 as dbcomm2
import pandas as pd

# 쪽수 많은 책 조회용 함수
def find_big_books(db_name):
    """
    조건에 맞는 데이터를 조회하는 함수
    조건 : 페이지수가 300 쪽보다 큰 데이터
    Args:
    db_name : Database Name
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
        db_sql = " SELECT * FROM book_mgr "
        db_sql += " WHERE pages > 300 "
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[2] 데이터 일부 출력하기')
        books = cur.fetchall()
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

    is_success, books_df = find_big_books(db_name)
    if is_success:
         print('조건에 맞는 데이터는 총 %d 건 입니다.(조건:pages>300)'%len(books_df))
    else :
         print('데이터를 조회하지 못했습니다')

    print(books_df['title'])




def find_books_of_publisher(db_name, publisher):
    """
    조건에 맞는 데이터를 조회하는 함수
    조건 : 출판사별 조회
    Args:
    db_name : Database Name
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
        db_sql = " SELECT * FROM book_mgr "
        db_sql += " WHERE publisher = '{}' ".format(publisher)
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        # print('[2] 데이터 일부 출력하기')
        books = cur.fetchall()
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

    is_success, books_df = find_books_of_publisher(db_name, publisher = 'A')
    if is_success:
         print('조건에 맞는 데이터는 총 %d 건 입니다.'%len(books_df))
    else :
         print('데이터를 조회하지 못했습니다')

    print(books_df)