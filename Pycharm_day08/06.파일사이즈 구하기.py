# 파일 크기 구하기
from os.path import getsize

file1 = './data/mydata.txt'
file2 = './images/전북은행_로고.jpg'
file3 = './images/전북은행_로고_copy.jpg'

file_size1 = getsize(file1)
file_size2 = getsize(file2)
file_size3 = getsize(file3)

print('File Name : {} \t File Size : {} byte'.format(file1,file_size1))
print('File Name : {} \t File Size : {} byte'.format(file2,file_size2))
print('File Name : {} \t File Size : {} byte'.format(file3,file_size3))