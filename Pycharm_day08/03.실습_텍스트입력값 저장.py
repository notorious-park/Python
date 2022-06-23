def write_txt(filepath):
    # 텍스트 파일에 한줄씩 쓰기
    count = 1
    data = []
    print('파일에 내용을 저장하려면 내용을 입력하지 말고 [Enter]를 누르세요!')

    while True:
        text = input('[%d] 파일에 저장할 내용을 입력하세요: ' % count)
        if text == '':
            break
        data.append(text + '\n')
        count += 1

    f = open(filepath,'w')
    f.writelines(data)
    f.close

    ret = 'TEXT 파일을 생성하였습니다'
    return ret

# 파일 생성
filepath = './data/mydata.txt'
write_txt(filepath)

# 파일 읽기
f = open(filepath,'r')
data = f.read()
f.close()

print(data)