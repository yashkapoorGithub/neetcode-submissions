class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
class Deque:
    
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = Node(value)
        newNode.prev = self.tail.prev
        newNode.next = self.tail

        self.tail.prev.next = newNode
        self.tail.prev = newNode
        
    def appendleft(self, value: int) -> None:
        newNode = Node(value)
        newNode.prev = self.head
        newNode.next = self.head.next

        self.head.next.prev = newNode
        self.head.next = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        curr = self.tail.prev
        curr.prev.next = self.tail
        self.tail.prev = curr.prev

        return curr.value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        
        curr = self.head.next
        self.head.next = curr.next
        curr.next.prev = self.head

        return curr.value
