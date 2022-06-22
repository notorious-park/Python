# Case2) 인스턴스간 공유 O
class Cat:
    def __init__(self,name):
        self.name = name
        self.tricks = []  # ★★★ 인스턴스 변수 선언!!! ★★★
                          # 07.실습의 경우 Class 밖에서 선언으로 동일한 구조로 생성됨

    def add_trick(self,trick):
        self.tricks.append(trick)

cat1 = Cat('하늘이')
cat2 = Cat('야옹이')

cat1.add_trick('구르기')
cat2.add_trick('두발로서기')
cat2.add_trick('죽은척하기')

print(cat1.name,':',cat1.tricks)
print(cat2.name,':',cat2.tricks)