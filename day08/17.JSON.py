import json

json_data = {
    'firstname'  : '길동',
    'lastname'   : '홍',
    'age'        : 20,
    'country'    : '율도국'
}

# json_code = json.JSONEncoder().encode(json_data)   # 한글인식 X

json_code = json.JSONEncoder(ensure_ascii=False).encode(json_data)

print(json_code)
print(type(json_code))

json_code = json.JSONDecoder().decode(json_code)    # 문자열을 dict형으로 디코딩
print(json_code)
print(type(json_code))


print('-'*100)
text = "{}{}은 {}살이고, {}에 살고 있습니다.".format(
    json_code['lastname'],
    json_code['firstname'],
    json_code['age'],
    json_code['country']
)
print(text)