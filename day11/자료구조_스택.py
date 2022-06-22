class Stack:

    def __init__(self):
        self.stack_items = []
        # print(len(self.stack_items))

    def pop(self):
        # pop 기능 구현
        # self.stack_items.pop(-1)
        empty = bool()
        if len(self.stack_items) == 0:
            empty = False
            print('Stack is empty!')
            print(empty)
        else:
            del self.stack_items[-1]
        pass

    def push(self, x):
        # push 기능 구현
        self.stack_items.append(x)
        # print(len(self.stack_items))
        pass

    def is_empty(self):
        # isEmpty 기능 구현
        empty = bool()
        if len(self.stack_items) == 0:
            empty = True
            print(empty)
        else:
            empty = False
            print(empty)
        pass

    def chk_stack(self):
        print("Stack = {}".format(self.stack_items))

stack = Stack()
stack.chk_stack()

stack.is_empty()

stack.push(1)
stack.chk_stack()

stack.push(3)
stack.chk_stack()

stack.push(5)
stack.push(7)
stack.push(9)
stack.chk_stack()

stack.pop()
stack.chk_stack()

stack.pop()
stack.chk_stack()

stack.pop()
stack.pop()
stack.pop()
stack.chk_stack()

stack.is_empty()

stack.pop()