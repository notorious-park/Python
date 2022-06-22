def exception_test5(file_path):
    try:
        f = open(file_path,'r')

    except IOError:
        print('cannot open', file_path)
    else:
        print('File has',len(f.readline()), 'lines')   # 파일 라인 수 출력
        f.close()
    finally:   # 예외 상관 없이 무조건 실행
        print('I just tried to read this file.', file_path)

# 정상 상황
exception_test5('README.TXT')

# 없는 파일을 찾을때
exception_test5('README-XXX.txt')