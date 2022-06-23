# 객체생성, 인스턴스화
class MyClass:
    name = str()

    def sayHello(self): # self
        hello = "Hello, " + self.name + "\t It's Good day !"
        print(hello)

myClass = MyClass()
myClass.name = '준영'
myClass.sayHello()
