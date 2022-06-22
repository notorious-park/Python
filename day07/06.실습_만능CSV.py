def read_csv(filename):
    # 1. 파일 가져오기
    file = open("data/JB_Finance_Group.csv", "r", encoding="UTF-8")
    data = file.read()
    file.close()

    elements = []  # 최종 리턴하기 위한 리스트 변수

    rows = data.split('\n')  # 데이터를 한줄씩 구분하여 리스트로 담기


    # Test
    fields = rows[0].split(', ')  # 한줄 데이터를 콤마로 구분하여 리스트 담기
    a = fields[0].strip()
    print(a)
    b = fields[1].strip()
    print(b)



    for row in rows[:]:
        fields = row.split(', ')  # 한줄 데이터를 콤마로 구분하여 리스트 담기

        var1 = fields[row].strip()

        element = {
            fields[row] : var1
        }

        elements.append(element)  # 한줄 데이터를 dict()형으로 변환후 리스트에 추가

    return elements
#
filename = './data/요온최종파일.csv'   # CSV파일명
JB = read_csv(filename)
#
for x in JB:
    print(x)







    # name = fields[0].strip()  # 앞뒤의 빈공백을 없앤후 변수에 담기
    # school = fields[1].strip()
    # email = fields[2].strip()
#     element = {
#         '이름': name,
#         '학교': school,
#         '메일': email
#     }
#
#     elements.append(element)  # 한줄 데이터를 dict()형으로 변환후 리스트에 추가
#
# return elements
