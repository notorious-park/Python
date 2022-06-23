import logging

logging.basicConfig(filename='log/basic_mode.log', encoding='utf-8', level=logging.ERROR)

logging.debug('디버깅모드에서 프로그램 진단')
logging.info('예상대로 작동하는지에 대한 확인')
logging.warning('예상하지 못한 문제가 발생')
logging.error('프로그램 오류로 인해 SW기능이 제대로 수행하지 못함')
logging.critical('심각한 에러로 즉각적인 대응이 요구')