def read_csv(filename):

    fp = open(filename, "r", encoding="utf-8")
    data = fp.read()
    fp.close()

    elements = []

    rows = data.split("\n")
    print('rows : ',rows)

    keys = rows[0].split(",")                         # 첫번째줄을 콤마로 구분하여 리스트에 담기. 컬럼명이 키값으로 사용하기 위함
    print('keys : ', keys)
    keys = [ key.replace(" ", "") for key in keys ]   # 리스트에 담긴 컬럼값들의 빈칸을 공백으로 바꾼다
    print("kyes = ", keys)

    for row in rows[1:]:                   # 2번째줄부터가 데이터이므로
        fields = row.split(",")
        print(fields)
        if len(keys) != len(fields):
            continue

        element = {}

        for idx in range(len(keys)):
            key = keys[idx]
            field = fields[idx].strip()
            element[key] = field

        elements.append(element)

    return elements




print('-'*100)
filename = "./data/company.csv"
filename = "./data/JB_Finance_Group.csv"
all_data = read_csv(filename)

print('-'*100)
for each_data in all_data:
    print(each_data)
