# 스타크래프트 예제
import time

# unit 부모 클래스 선언
class Unit:
    def __init__(self,name,energy,is_fly):
        self.name = name
        self.energy = energy
        self.is_fly = is_fly
        self.is_alive = True

    def get_tribe(self):
        print(self.name + 'is a basic tribe!')

    def get_energy(self):
        if self.energy > 0:
            print(self.name + '의 현재 에너지는', self.energy, '입니다.')
        else:
            self.is_alive = False
            print(self.name + '유닛은 전사했습니다ㅠㅠㅠ')

# 테란종족 클래스
class Terran(Unit):
    def get_tribe(self):
        print(self.name + 'is a Terran!')

    def be_attactted(self):
        self.energy -= 15

# 프로토스종족 클래스
class Protoss(Unit):
    def get_tribe(self):
        print(self.name + 'is a Protoss')

    def be_attactted(self):
        self.energy -= 20

# 저그종족 클래스
class Zerg(Unit):
    def get_tribe(self):
        print(self.name + 'is a Zerg')

    def be_attacted(self):
        self.energy -= 8

# 종족별 유닛 생성
Tank = Terran('탱크',150,False)
Dragon = Protoss('드라군',200,False)
Hydra = Zerg('히드라',100,False)

# print('{}와 {}와 {}의 1대1대1 경기를 시작합니다.'.format())

for x in range(1,30):
    Tank.be_attactted()
    Dragon.be_attactted()
    Hydra.be_attacted()

    print('\n', x, '차 공격받은 후의 에너지!!! \n------------------------')
    Tank.get_energy();   time.sleep(1)
    Dragon.get_energy(); time.sleep(1)
    Hydra.get_energy();  time.sleep(1)

    if(Tank.is_alive & Dragon.is_alive & Hydra.is_alive):
        time.sleep(1)
    else:
        break

print('='*50, '\n게임이 종료되었습니다.')
