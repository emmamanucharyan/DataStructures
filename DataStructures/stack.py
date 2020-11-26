##linked list implementation##
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def get_size(self):
        return self.size

    def pop(self):
        if self.first == None:
            return
        if self.size == 1:
            self.first = None
            self._last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.size -= 1

    def push(self, obj):
        node = Node(obj, self.first)
        self.first = node
        if self.last == None:
            self.last = node
        self.size += 1

    def top(self):
        return self.first

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False

    def empty(self):
        self.first.next = None
        self.last = None
        self.first = None
        self.size = 0

    def print(self):
        print("Printing Stack Elements")
        current = self.first
        while current is not None:
            print(str(current.data))
            current = current.next

    def check_list(self, my_list):
        check = True
        current = self.first
        n = 0
        while n < len(my_list):
            if current.data != my_list[n]:
                check = False
                return check
            n += 1
            current = current.next
        return check

## python list implementation ##

class ListStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        if self.items == []:
            return True
        else:
            return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def empty(self):
        self.items = []

    def print(self):
        print("Printing Stack Elements")
        for i in range(len(self.items)-1, -1, -1):
            print(self.items[i])





