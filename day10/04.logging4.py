import logging

# logging.basicConfig(format='%(asctime)s %(message)s')
# logging.warning('기본형 날짜시간 정보 추가')
#
# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
# logging.warning('포맷형 날짜시간 정보 추가')

# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y,%m,%d %I:%M:%S %p')
# logging.warning('포맷형 날짜시간 정보 추가')

# logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y.%m.%d %I:%M:%S %a')
# logging.warning('포맷형 날짜시간 정보 추가')


# 요온 - 이게 제일 심플한 듯 - 이거 사용
logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%Y,%m,%d %I:%M')
logging.warning('포맷형 날짜시간 정보 추가')