import time
count = 1

try:
    while True:
        print(count)
        count += 1
        time.sleep(1)
except KeyboardInterrupt:   # Ctrl + C 입력 시, 중단
    print('사용자에 의해 프로그램이 중단되었습니다!')
