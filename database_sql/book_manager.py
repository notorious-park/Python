from sect15_database.database import common as dbcomm
from sect15_database import s03_reg_book  as bookmgr_C
from sect15_database import s04_read_data as bookmgr_R
from sect15_database import s05_upd_data  as bookmgr_U
from sect15_database import s06_del_data  as bookmgr_D

import pandas as pd

if __name__=="__main__":
    db_name = 'bpcdb'
    title = '인더스트리 2.0'

    is_success, books_df1 = bookmgr_R.find_books_of_title(db_name, title)

    if bookmgr_U.update_recommendation(db_name, recommendation=0, title=title):
        print('데이터가 성공적으로 수정되었습니다.')
    else:
        print('데이터가 수정되지 않았습니다')

    is_success, books_df2 = bookmgr_R.find_books_of_title(db_name, title)

    books_df = pd.concat([books_df1, books_df2], axis=0)
    books_df['update'] = ['수정전', '수정후']
    books_df.set_index('update', inplace=True)
    print(books_df)
    print('-'*80)

    col_name = 'title'
    col_val  = '사물인터넷 전망'
    if bookmgr_D.delete_books(db_name, col_name, col_val):
        print('데이터가 성공적으로 삭제되었습니다.')
    else :
        print('데이터가 삭제되지 않았습니다')

    is_success, books_df = bookmgr_R.find_books_by_title(db_name, title=col_val)
    print(books_df)

