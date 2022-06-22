# 파일 이름 바꾸기
from os import  rename

folder_path = './data/'
target_file = folder_path + 'mydata.txt'
newname = input('{}에 대한 새로운 파일 이름을 입력하세요'.format(target_file))

new_file = newname
rename(target_file,new_file)
print('{} -> {}로 파일 이름을 변경하였습니다.'.format(target_file,new_file))
