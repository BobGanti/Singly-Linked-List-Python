# addFirst()
# addLast()
# deleteFirst()
# deleteLast()
# contains()
# indexOf()

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,):
        self.first = None
        self.last = None


    def printLinkedList(self):
        if self.first is self.last is None:
            print("linked list is empty")
        else:
            current = self.first
            while current is not None:
                print(current.value, "=>", end=" ")
                current = current.next

    def addFirst(self, item):
        newNode = Node(item)
        if self.__isEmptyList():
            self.first = self.last = newNode
        else:
            newNode.next = self.first
            self.first = newNode

    def addLast(self, item):
        newNode = Node(item)
        if self.__isEmptyList():
            self.first = self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode

    def addAfter(self, nodeInfront, nodeToAdd):
        current = self.first
        while current is not None:
            if current.value == nodeInfront:
                break
            current = current.next
        if current is None:
            print(f"Node {nodeInfront} is not found in the list")
        else:
            newNode = Node(nodeToAdd)
            newNode.next = current.next
            current.next = newNode

    def indexOf(self, item):
        index = 0
        current = self.first
        while current is not None:
            if current.value == item:
                return index
            current = current.next
            index += 1
        return -1

    def contains(self,item):
        return self.indexOf(item) != -1

    def removeFirst(self):
        if self.__isEmptyList():
            print("The list is empty!")
            return -1
        if self.first == self.last:
            self.first = self.last = None
            return
        secondNode = self.first.next
        self.first.next = None
        self.first = secondNode

    def removeLast(self):
        if self.__isEmptyList():
            print("The list is empty!")
            return -1
        if self.first == self.last:
            self.first = self.last = None
            return
        previous = self.__getPrevious(self.last)
        last = previous
        last.next = None

    def __getPrevious(self, node):
        current = self.first
        while current is not None:
            if current.next == node:
                return current
            current = current.next

    def __isEmptyList(self):
        return self.first == None

ll1 = LinkedList()
ll1.addLast(5)
ll1.addLast(10)
ll1.addFirst(1)
ll1.addLast(20)
ll1.addFirst(100)
ll1.addAfter(100, 25)
ll1.printLinkedList()
print(f"\nContains {15}: ", ll1.contains(15))
print(f"Index Of {10}: ", ll1.indexOf(10))
ll1.removeFirst()
ll1.removeLast()

ll1.printLinkedList()
