import logging

t_debug  = logging.debug('분석')
t_info   = logging.info('확인')
t_warn   = logging.warning('경고')
t_error  = logging.error('에러')
t_critic = logging.critical('심각')

print('{} : {}'.format('1단계', t_debug))
print('{} : {}'.format('2단계', t_info))
print('{} : {}'.format('3단계', t_warn))
print('{} : {}'.format('4단계', t_error))
print('{} : {}'.format('5단계', t_critic))