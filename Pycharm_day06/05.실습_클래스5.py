# 클래스 생성과 소멸
class MyClass:

    def __init__(self):
        print('MyClass 인스턴트 객체가 생성되어 메모리에 올라갑니다.')

    def getClassName(self):
        return 'MyClass'

    def __del__(self):   # 다 돌고나서 마지막에 제거됨(맨 마지막) Ex) DOS
        print('MyClass 인스턴트 객체가 메모리에서 제거됩니다.')

# 객체 생성
obj = MyClass()
ret = obj.getClassName()
print(ret)

for i in range(5):
    print(i)

print('프로그램을 종료합니다.')