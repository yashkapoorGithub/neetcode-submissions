class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class MyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0    

    def getIndex(self, index):
        curr = self.head.next
        for i in range(index):
            curr = curr.next
        return curr

    def get(self, index: int) -> int:
        if index >= self.size:
            return -1
        return self.getIndex(index).val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.tail
        newNode.prev = self.tail.prev

        self.tail.prev.next = newNode
        self.tail.prev = newNode
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        newNode = Node(val)
        curr = self.getIndex(index)

        newNode.next = curr
        newNode.prev = curr.prev

        curr.prev.next = newNode
        curr.prev = newNode
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.size:
            return
        curr = self.getIndex(index)
        curr.next.prev = curr.prev
        curr.prev.next = curr.next
        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)