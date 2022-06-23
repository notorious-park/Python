import logging

def do_something():
    logging.info('Doing something')
    print('check')

if __name__ == '__main__':
    do_something()

# do_something() # 그냥 이걸로 쓰면 두번 호출 됨