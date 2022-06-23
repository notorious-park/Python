try:
    print('안녕하세요!')
    print('반갑습니다!')
    #print(오류발생)      # 오류발생 / Error 존재 시, 다음 코드가 정상이더라도 바로 except로 넘어감
    print('안녕히 가세요!')

except Exception as err:   # 예외 발생 시, 실행
    print('예외가 발생했습니다!')
    print('Error : ',err)

else:   # try문 안에 다 정상일 경우, else 구문 찍힘
    print('예외가 발생하지 않았습니다!')

finally:   # Error 유무와 관계없이 무조건 실행하는 코드
    print('Error 유무와 관계없이 무조건 실행하는 코드!!!')