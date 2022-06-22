# Case1) 인스턴스간 공유 X
class Dog:
    tricks = [] # 클래스 변수 선언   /   # 동일한 구조

    def __init__(self,name):
        self.name = name

    def add_trick(self,trick):
        self.tricks.append(trick)

dog1 = Dog('마음이')
dog2 = Dog('진돌이')

dog1.add_trick('구르기')
dog2.add_trick('두발로서기')
dog2.add_trick('죽은척하기')

print(dog1.name,':',dog1.tricks)
print(dog2.name,':',dog2.tricks)