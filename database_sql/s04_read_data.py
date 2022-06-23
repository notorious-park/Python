from sect15_database.database import common as dbcomm
import pandas as pd

def getBooksDF(books):
    ret_df = pd.DataFrame()

    title = list()
    published_date = list()
    publisher = list()
    pages = list()
    recommendation = list()

    column_name = ['title', 'published_date', 'publisher', 'pages', 'recommendation']
    for book in books:
        title.append(book[0])
        published_date.append(book[1])
        publisher.append(book[2])
        pages.append(book[3])
        recommendation.append(book[4])

    data = {
        'title': title,
        'published_date': published_date,
        'publisher': publisher,
        'pages': pages,
        'recommendation': recommendation
    }

    ret_df = pd.DataFrame(data, columns=column_name)

    return ret_df

def select_all_books(db_name):
    """
    전체 데이터를 조회하는 함수
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
        db_sql = "SELECT * FROM book_mgr"
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[1] 전체 데이터 출력하기')
        books = cur.fetchall()

        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        # 데이터베이스 커넥션 닫기
        conn.close()

    return is_success, ret_df


# 일부 조회용 함수
def select_some_books(db_name, number):
    """
    일부 데이터를 조회하는 함수
    Args:
        db_name : Database Name
        number  : Count of data to query
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

        # 조회한 데이터 일부 불러오기
        print('[2] 데이터 일부 출력하기')
        books = cur.fetchmany(number)

        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        conn.close()

    return is_success, ret_df




# 1개 조회용 함수
def select_one_book(db_name):
    """
    최상단 하나의 데이터를 조회하는 함수
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

        # 커서 확보
        cur = conn.cursor()

        # 조회용 SQL 실행
        db_sql = "SELECT * FROM book_mgr "
        cur.execute(db_sql)

        # 데이터 한개 출력하기
        print('[3] 1개 데이터 출력하기')
        book = cur.fetchone()
        books = [book]
        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        conn.close()

    return is_success, ret_df



# 쪽수 많은 책 조회용 함수
def find_big_books(db_name):
    """
    조건에 맞는 데이터를 조회하는 함수
    조건 : 페이지수가 300쪽보다 큰 데이터
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
        print('[4] 페이지 많은 책 출력하기')
        books = cur.fetchall()
        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        conn.close()

    return is_success, ret_df



# 쪽수 많은 책 조회용 함수
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
        db_sql  = " SELECT * FROM book_mgr "
        db_sql += " WHERE publisher = '{}' ".format(publisher)
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[5] 출판사별 책 출력하기')
        books = cur.fetchall()
        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        conn.close()

    return is_success, ret_df


# 책제목에 의한 조회용 함수
def find_books_by_title(db_name, title):
    """
    조건에 맞는 데이터를 조회하는 함수
    조건 : 책제목별 조회
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
        db_sql  = " SELECT * FROM book_mgr "
        db_sql += " WHERE title like '%{}%' ".format(title)
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[6] 제목으로 검색된 책 출력하기')
        books = cur.fetchall()
        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        conn.close()

    return is_success, ret_df

# 책제목에 의한 조회용 함수
def find_books_of_title(db_name, title):
    """
    조건에 맞는 데이터를 조회하는 함수
    조건 : 책제목별 조회
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
        db_sql  = " SELECT * FROM book_mgr "
        db_sql += " WHERE title = '{}' ".format(title)
        cur.execute(db_sql)

        # 조회한 데이터 불러오기
        print('[6] 제목으로 검색된 책 출력하기')
        books = cur.fetchall()
        ret_df = getBooksDF(books)

    except:
        is_success = False
        print("Database Error!")

    finally:
        conn.close()

    return is_success, ret_df




if __name__=="__main__":

    db_name = 'bpcdb'

    # is_success, books_df = select_all_books(db_name)
    # if is_success:
    #     print('조회된 데이터는 총 %d 건 입니다.'%len(books_df))
    # else :
    #     print('데이터를 조회하지 못했습니다')
    #
    # print(books_df)


    # is_success, books_df = select_some_books(db_name, number=3)
    # if is_success:
    #     print('조회된 데이터는 총 %d 건 입니다.'%len(books_df))
    # else :
    #     print('데이터를 조회하지 못했습니다')
    #
    # print(books_df)

    # is_success, books_df = select_one_book(db_name)
    # if is_success:
    #     print('하나의 데이터를 성공적으로 조회하였습니다.')
    # else :
    #     print('데이터를 조회하지 못했습니다')
    #
    # print(books_df)

    # is_success, books_df = find_big_books(db_name)
    # if is_success:
    #     print('조건에 맞는 데이터는 총 %d 건 입니다.(조건:pages>300)'%len(books_df))
    # else :
    #     print('데이터를 조회하지 못했습니다')
    #
    # print(books_df['title'])

    # is_success, books_df = find_books_of_publisher(db_name, publisher='B')
    # if is_success:
    #     print('조건에 맞는 데이터는 총 %d 건 입니다.'%len(books_df))
    # else :
    #     print('데이터를 조회하지 못했습니다')
    #
    # print(books_df)

    is_success, books_df = find_books_by_title(db_name, title='2')
    if is_success:
        print('조건에 맞는 데이터는 총 %d 건 입니다.'%len(books_df))
    else :
        print('데이터를 조회하지 못했습니다')

    print(books_df)