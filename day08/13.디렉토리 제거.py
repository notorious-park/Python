# 디렉토리 제거하기
import os

target_folder = 'new_folder'

k = input('{} 디렉토리를 삭제하시겠습니까? (y/n)'.format(target_folder))
if k == 'y':
    try:
        os.rmdir(target_folder)
        print('{} 디렉토리를 삭제했습니다.'.format(target_folder))
    except Exception as e:
        print(e)