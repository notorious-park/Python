from day99.database import common as dbcomm
from day99.database import common2 as dbcomm2
import pandas as pd

def find_books_by_title(db_name, title):
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
        db_sql += " WHERE title like '%{}%' ".format(title)
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[6] 책 제목으로 검색하여 불러오기')
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

    is_success, books_df = find_books_by_title(db_name, title = '빅데이터')
    if is_success:
         print('조건에 맞는 데이터는 총 %d 건 입니다.'%len(books_df))
    else :
         print('데이터를 조회하지 못했습니다')

    print(books_df)




def find_books_of_title(db_name, title):
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
        db_sql += " WHERE title = '%{}%' ".format(title)
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        # print('[7] 책 제목으로 검색하여 불러오기')
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

    is_success, books_df = find_books_of_title(db_name, title = '빅데이터 마케팅')
    if is_success:
         print('조건에 맞는 데이터는 총 %d 건 입니다.'%len(books_df))
    else :
         print('데이터를 조회하지 못했습니다')

    print(books_df)