import json

data = '''
{
    "name" : "홍길동",
    "dog"  : {
        "name" : "순둥이",
        "toys"  : [
                {"name" : "뽀로로"},
                {"name" : "토마스"}
        ]
   }
}
'''

with open('data/person.json','w') as fp:
    fp.write(data)

with open('data/person.json') as data_file:
    person = json.load(data_file)

print(person)
print(type(person))

print('-'*100)

# print(person['name'])
# print(person['dog']['name'])
# print(person['dog']['toys'][0]['name'])
# print(person['dog']['toys'][1]['name'])


# 출력 : 홍길동의 개 순둥이의 장난감은 뽀로로, 토마스입니다.
text = '{}의 개 {}의 장난감은 {},{}입니다.'.format(
    person['name'],
    person['dog']['name'],
    person['dog']['toys'][0]['name'],
    person['dog']['toys'][1]['name']
)
print(text)