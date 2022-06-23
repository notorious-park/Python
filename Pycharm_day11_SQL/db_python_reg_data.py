from day99.database import common as dbcomm

def insert_books(db_name,db_sql):
    is_success = True
    try:
        # 데이터베이스 커넥션 생성
        conn = dbcomm.get_connection(db_name)
        # 커서 확보
        cur = conn.cursor()
        # 데이터 입력 SQL1
        # db_sql = "INSERT INTO my_books VALUES ('메가트랜드', '2002.03.02','A',200, 0)"
        cur.execute(db_sql)
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
    db_sql  = "INSERT INTO book_mgr VALUES ('메가트랜드', '2002.03.02','A',200, 0)"

    is_success = insert_books(db_name, db_sql)

    if is_success:
        print('데이터가 성공적으로 등록되었습니다.')
    else:
        print('데이터가 등록되지 않았습니다')



