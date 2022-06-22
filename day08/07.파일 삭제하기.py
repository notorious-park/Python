# 파일 삭제하기
from os import remove

target_file = './images/전북은행_로고_copy.jpg'
k = input('{} 파일을 삭제하시겠습니까? ([y],n)'.format(target_file))

if k == 'y' or k == '':
    remove(target_file)
    print('{} 파일을 삭제하였습니다'.format(target_file))