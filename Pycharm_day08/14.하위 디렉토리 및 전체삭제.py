# 하위 디렉토리 및 파일 전체 삭제하기
# ★★★★★★★ 가급적이면 사용하지 말것!!!!!! - 전체 파일 다 날라 갈수도 있음 ★★★★★★★

import shutil
import os

target_folder = './aaa'   # 파일 경로 지정 잘해야함!!!
print('{} 하위 모든 디렉토리 파일을 삭제합니다.'.format(target_folder))

for file in os.listdir(target_folder):
    print(file)
k = input('{}를 삭제하시겠습니까? (y/n) '.format(target_folder))

if k == 'y':
    try:
        shutil.rmtree(target_folder)
        print('{}의 모든 하위 디렉토리 파일들을 삭제했습니다.'.format(target_folder))
    except Exception as e:
        print(e)