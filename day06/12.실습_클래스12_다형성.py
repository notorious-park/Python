# Developer 부모 클래스 선언
class Developer:
    def __init__(self,name):
        self.name = name

    def coding(self):
        print('{}는 코딩을 좋아합니다.'.format(self.name))
        print(self.name + 'is developer!')

# 자식 클래스 선언
class PythonDeveloper(Developer):
    def coding(self):
        print('{}는 Python 코딩을 좋아합니다.'.format(self.name))

class JavaDeveloper(Developer):
    def coding(self):
        print('{}는 Java 코딩을 좋아합니다.'.format(self.name))

class CPPDeveloper(Developer):
    def coding(self):
        print('{}는 C++ 코딩을 좋아합니다.'.format(self.name))

class RDeveloper(Developer):
    def coding(self):
        print('{}는 R 코딩을 좋아합니다.'.format(self.name))

pDeveloper = PythonDeveloper('찬영이')
jDeveloper = JavaDeveloper('준영이')
cDeveloper = CPPDeveloper('채영이')
rDeveloper = RDeveloper('경남이')

pDeveloper.coding()
jDeveloper.coding()
cDeveloper.coding()
rDeveloper.coding()
