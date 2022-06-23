from datetime import datetime   # 현재 날짜 및 시간 계산

module_name = 'FileName'

def exception_test2():
    method_name = 'exception_test2()'
    print("[1] Can you add 2 and '2' in python?")

    try:
        print("[2] Try it~!",2 + '2')

    except Exception as err:
        # print('[E1]', err.__str__())
        # print('[E2]', err.__class__)
        print('-'*100)

        cur_time = datetime.now()   # 현재 날짜 및 시간
        log_time = 'cur_time : {}'.format(str(cur_time)[:19])
        # print('log_time : ',log_time)

        err_msg = '\n{} {}.{} 에러 발생 \n{} :: {}'.format(
            log_time,module_name,method_name,
            err.__class__,err
        )
        print('log 파일에 저장되는 부분 : {}'.format(err_msg))

        print("[3] It's not possible to add integer and string together.")

exception_test2()