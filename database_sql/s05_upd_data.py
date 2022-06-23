# import pymysql
# from database import common as dbcomm
from sect15_database.database import common as dbcomm
from sect15_database import s04_read_data as bookmgr_R
import pandas as pd

def update_books(db_name):
    """
    데이터를 수정하는 함수
    Args:
        db_name : Database Name
    Returns :
        is_success : Boolean
    """
    is_success = True


    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomm.get_connection(db_name)

        # 커서 확보
        cur = conn.cursor()

        # 데이터 수정 SQL ( 제목이 ? 인 책의 추천 유무를 ? 로 변경하라 )
        db_sql = "UPDATE book_mgr SET recommendation=%s WHERE title=%s "

        # 수정 SQL 실행
        cur.execute(db_sql, (1, '메가트랜드'))

    except:
        is_success = False
        print("Database Error!")

    finally:
        if is_success:
            # 데이터베이스 반영
            conn.commit()
        else:
            # 데이터베이스 철회
            conn.rollback()

        # 데이터베이스 커넥션 닫기
        conn.close()

    return is_success


def update_recommendation(db_name, title, recommendation):
    """
    데이터를 수정하는 함수
    Args:
        db_name : Database Name
    Returns :
        is_success : Boolean
    """
    is_success = True


    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomm.get_connection(db_name)

        # 커서 확보
        cur = conn.cursor()

        # 데이터 수정 SQL ( 제목이 ? 인 책의 추천 유무를 ? 로 변경하라 )
        db_sql = "UPDATE book_mgr SET recommendation=%s WHERE title=%s "

        # 수정 SQL 실행
        cur.execute(db_sql, (recommendation, title))

    except Exception as err:
        is_success = False
        print("Database Error : {}".format(err))
        print('Query : {}'.format(db_sql))

    finally:
        if is_success:
            # 데이터베이스 반영
            conn.commit()
        else:
            # 데이터베이스 철회
            conn.rollback()

        # 데이터베이스 커넥션 닫기
        conn.close()

    return is_success


if __name__=="__main__":
    db_name = 'bpcdb'
    is_success, books_df1 = bookmgr_R.select_one_book(db_name)

    if update_books(db_name):
        print('데이터가 성공적으로 수정되었습니다.')
    else:
        print('데이터가 수정되지 않았습니다')

    is_success, books_df2 = bookmgr_R.select_one_book(db_name)

    books_df = pd.concat([books_df1, books_df2], axis=0)
    books_df['update'] = ['수정전', '수정후']
    books_df.set_index('update', inplace=True)
    print(books_df)

    # is_success, books_df = bookmgr.select_all_books(db_name)
    # if is_success:
    #     print('조회된 데이터는 총 %d 건 입니다.'%len(books_df))
    # else :
    #     print('데이터를 조회하지 못했습니다')
    #
    # print(books_df)
