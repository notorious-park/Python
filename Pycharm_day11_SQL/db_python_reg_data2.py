from day99.database import common as dbcomm

def insert_books2(db_name,db_sql):
    is_success = True
    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomm.get_connection(db_name)
        # 커서 확보
        cur = conn.cursor()
        # 데이터 입력 SQL1
        db_sql = 'INSERT INTO book_mgr VALUES (%s,%s,%s,%s,%s)'
        cur.execute(db_sql, book_info)
        # cur.execute(db_sql,('인더스트리4.0', '2016.07.09', 'B', 584, 1))

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

        conn.close()

    return is_success


if __name__ == "__main__":

    db_name = 'jbfgtest'
    book_info = ('인더스트리4.0', '2016.07.09', 'B', 584, 1)
    db_sql = 'INSERT INTO book_mgr VALUES (%s,%s,%s,%s,%s)'

    is_success = insert_books2(db_name, db_sql)

    if is_success:
        print('데이터가 성공적으로 등록되었습니다.')
    else:
        print('데이터가 등록되지 않았습니다')




