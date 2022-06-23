# 디렉토리 생성하기
import os

newfolder = input('새로 생성할 디렉토리 이름을 입력하세요: ')

try :
    os.mkdir(newfolder)
    print('{} 디렉토리를 새로 생성했습니다.'.format(newfolder))
except Exception as e:
    print(e)