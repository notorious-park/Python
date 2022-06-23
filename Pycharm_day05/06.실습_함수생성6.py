# Arbitrary arguments - 가변인자

# * (1개) : 리스트형 or 튜플형
# **(2개) : 사전형(dict)

def introduceMyDep(my_name,*dep_names,**dep_info):
    print('안녕하세요! 저는 {}입니다.'.format(my_name))
    print('-'*100)
    print('저희 부서를 소개하겠습니다!')
    for name in dep_names:
        print('- {}'.format(name),end = '\t')
    else:
        print()
    print('-'*100)
    for key in dep_info.keys():
        print('-{} : {}'.format(key,dep_info[key]))

introduceMyDep('요온','태우','별나','성실','지혜','아영','소연','용갑','창용','덕은',
               부장님 = '허경아', 부서위치 = '본점 7층', 부서신규일자 = '2020.08')