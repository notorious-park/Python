# 피보나치 수열을 위한 모듈 불러오기

from packages import fibo        # Case1) pacakages 안에 넣을 경우, from 뒤에 자동으로 변경됨

from packages import *           # Case2) *로 할 시, 해당 라이브러리에 있는 함수값 전부 다 불러옴

from packages import fibo as f1  # Case3) 지정 - 나중에 함수명 변경 시, 좋음


new_fib1 = fibo.fib
new_fib1(30)

new_fib2 = f1.fib
new_fib2(30)
