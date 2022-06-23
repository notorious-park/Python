# 정보은닉(Data hiding) 및 캡슐화(Encapsulation)

class MyFavorite:
    __pitcher = '양현종'
    __batter  = '최형우'

    def kia_pitcher(self):
        return self.__pitcher

    def kia_batter(self):
        return self.__batter

    def set_kia_pitcher(self,pitcher):
        self.__pitcher = pitcher

    def set_kia_batter(self,batter):
        self.__batter = batter

myInfo = MyFavorite()
my_pitcher = myInfo.kia_pitcher()
my_batter = myInfo.kia_batter()
print('예전엔 투수 {}를 좋아하고, 타자 {}를 좋아했습니다.'.format(my_pitcher,my_batter))

myInfo.set_kia_pitcher('이의리')
myInfo.set_kia_batter('나성범')
my_pitcher = myInfo.kia_pitcher()
my_batter = myInfo.kia_batter()
print('지금은 투수 {}를 좋아하고, 타자 {}를 좋아합니다'.format(my_pitcher,my_batter))