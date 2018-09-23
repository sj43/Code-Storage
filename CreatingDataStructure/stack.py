class myStack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


stack = myStack()
stack.push(100)
stack.push(200)
stack.push(300)
stack.peek()
stack.pop()
stack.peek()
stack.size()
stack.isEmpty()
