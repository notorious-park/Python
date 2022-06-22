import logging
import test_lib

logging.basicConfig(filename='log/test_mode.log', level=logging.INFO, encoding='utf-8')

def main():
    logging.info('메인함수 시작')
    test_lib.do_something()
    logging.info('메인함수 종료')

if __name__ == '__main__':
    main()