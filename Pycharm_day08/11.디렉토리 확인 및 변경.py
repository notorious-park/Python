# 현재 디렉토리 확인하고 바꾸기
import os
import time as t

pdir = os.getcwd();
print(pdir)
t.sleep(1)

os.chdir('data');
print(os.getcwd())
t.sleep(1)

os.chdir('..');
print(os.getcwd())
t.sleep(1)

os.chdir(pdir);
print(os.getcwd())