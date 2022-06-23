from sect15_database.database import common as dbcomm

# 데이터 입력 함수
def insert_books_3(db_name, arr_book_info):
    is_success = True

    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomm.get_connection(db_name)

        # 커서 확보
        cur = conn.cursor()

        # 데이터 입력 SQL1
        db_sql = 'INSERT INTO book_mgr VALUES (%s, %s, %s, %s, %s)'
        cur.executemany(db_sql, arr_book_info)

    except Exception as err:
        is_success = False
        print("Database Error : {}".format(err))

    finally:
        if is_success:
            # 데이터베이스 반영
            conn.commit()
        else:
            # 데이터베이스 철회
            conn.rollback()

        conn.close()

    return is_success



if __name__=="__main__":

    db_name = 'bpcdb'
    book_info = ('인더스트리 2.0', '2016.07.09', 'B', 584, 1)

    arr_book_info = [
        ('유니콘 스타트업3', '2011.07.15', 'A', 248, 1),
        ('유니콘 스타트업4', '2011.07.15', 'A', 248, 1),
        ('유니콘 스타트업5', '2011.07.15', 'A', 248, 1),
        ('빅데이터 마케팅4', '2012.08.25', 'A', 296, 1),
        ('빅데이터 마케팅5', '2012.08.25', 'A', 296, 1),
        ('빅데이터 마케팅6', '2012.08.25', 'A', 296, 1),
        ('사물인터넷 전망7', '2013.08.22', 'B', 526, 0),
        ('사물인터넷 전망8', '2013.08.22', 'B', 526, 0),
        ('사물인터넷 전망9', '2013.08.22', 'B', 526, 0)
    ]

    is_success = insert_books_3(db_name, arr_book_info)

    if is_success:
        print('데이터가 성공적으로 등록되었습니다.')
    else:
        print('데이터가 등록되지 않았습니다')

