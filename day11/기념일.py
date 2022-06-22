from common_comma import cs_num
from datetime import datetime

def getMemorialDay(year, month, day, mem_day = '기념일', is_msg = True):
    if is_msg:
        start_day = datetime(year,month,day)
        end_day = datetime.today()
        elapsed = end_day - start_day

        elapsed_day = elapsed.days
        elapsed_month = int(elapsed_day / 30)
        elapsed_year = int(elapsed_day / 365)

        if is_msg:
            print('오늘은 {}으로부터 {}일 경과되었고, 달 수로는 {}개월째, 연 수로는 {}년째 되었습니다!'.format(mem_day, cs_num(elapsed_day), cs_num(elapsed_month),cs_num(elapsed_year)))

        return elapsed_year, elapsed_month, elapsed_day

getMemorialDay(2000,1,1, '밀레니엄일')
getMemorialDay(2014,4,16, '세월호침몰사고일')
getMemorialDay(2020,1,20, '국내 최초 코로나 발생일')

# _y, _m, elapsed_day = getMemorialDay(2019, 12, 25, '크리스마스', False)
# '크리스마스까지는 %d일 남았습니다!!' % -elapsed_day

