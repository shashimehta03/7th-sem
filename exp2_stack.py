class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage
stack = Stack()
print("Is stack empty?", stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack size:", stack.size())
print("Top element :", stack.peek())
print("Popped element:", stack.pop())
print("Top element after pop:", stack.peek())
print("Is stack empty?", stack.is_empty())
