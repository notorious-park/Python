# 파일 존재하는지 체크하기
import os
from os.path import exists

dir_name = input('새로 생성할 디렉토리 이름을 입력하세요: ')

if not exists(dir_name):
    os.mkdir(dir_name)
    print('{} 디렉토리를 생성하였습니다.'.format(dir_name))
else:
    print('{} 은(는) 이미 존재합니다.'.format(dir_name))