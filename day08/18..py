class Person:
    name = str()
    age  = int()
    hometown = str()

    def __init__(self,name,age,hometowm):
        self.name = name
        self.age = age
        self.hometown = hometowm

    def to_string(self):
        str = '{}의 나이는 {}살이고, 고향은 {}입니다.'.format(self.name,self.age,self.hometown)
        return str

theif1 = Person('홍길동',20,'율도국');   # 끝에 ; 필요한가
theif2 = Person('임꺽정',20,'구월산');

print(theif1.to_string())
print(theif2.to_string())

