# 파일인지 디렉토리인지 혹인
import os
from os.path import exists, isdir, isfile

files = os.listdir()
print('files :',files)

for file in files:
    if isdir(file):
        print('<DIR> {}'.format(file))

for file in files:
    if isfile(file):
        print('<FILE> {}'.format(file))