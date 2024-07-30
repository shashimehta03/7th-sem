class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_with_value(self, data):
        if not self.head:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=' ')
            current = current.next
        print()

# Example usage
if __name__ == "__main__":
    # Stack operations
    print("Stack operations:")
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    print(s.pop())  # Output: 3
    print(s.peek())  # Output: 2
    print(s.is_empty())  # Output: False
    print(s.size())  # Output: 2

    # Queue operations
    print("\nQueue operations:")
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print(q.dequeue())  # Output: 1
    print(q.front())  # Output: 2
    print(q.is_empty())  # Output: False
    print(q.size())  # Output: 2

    # LinkedList operations
    print("\nLinkedList operations:")
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.prepend(0)
    ll.print_list()  # Output: 0 1 2 3
    ll.delete_with_value(2)
    ll.print_list()  # Output: 0 1 3
