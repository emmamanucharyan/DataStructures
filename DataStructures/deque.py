class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class Deque:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def insert_front(self, obj):
        if self.size == 0:
            node = Node(obj)
            self.first = node
            self.first.previous = None
            self.last = node
            self.last.next = None
            self.size += 1
            return
        node = Node(obj)
        self.size += 1
        node.next = self.first
        self.first.previous = node
        self.first = node
        self.first.previous = None

    def remove_front(self):
        if self.first is None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        self.first.previous = None
        tmp.next = None
        self.size -= 1

    def remove_end(self):
        if self.size == 0:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.last.previous
        tmp.next = None
        self.last = tmp
        self.size -= 1

    def insert_end(self, obj):
        node = Node(obj, None)
        if self.size == 0:
            self.first = node
            self.first.previous = None
            self.last = node
            self.last.next = None
            self.size += 1
            return
        temp = self.last
        self.last.next = node
        self.last = node
        self.last.previous = temp
        self.last.next = None
        self.size += 1

    def get_first(self):
        if self.size == 0:
            print("Empty")
            return
        return self.first.data

    def get_last(self):
        if self.size == 0:
            print("Empty")
            return
        return self.last.data

    def print(self):
        print("Printing Dequeue Elements")
        current = self.first
        while current is not None:
            print(str(current.data))
            current = current.next
        print()

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


class CyclicArrayDeque:
    def __init__(self):
        self.queue = [None, None]
        self.size = 0
        self.front = -1
        self.rear = -1

    def resize(self):
        initial_length = len(self.queue)
        temp = []
        j = 0
        for i in self.queue:
            while j < len(self.queue):
                temp.append(self.queue[self.front])
                self.front = (self.front + 1) % initial_length
                j += 1
        j = 0
        while j < initial_length:
            temp.append(None)
            self.queue = temp
            j += 1
        # print("Resize:", self.queue, "\n")
        self.front = 0
        self.rear = initial_length-1


    def insert_front(self, obj):
        if self.size == len(self.queue):
            self.resize()
        if self.size == 0:
            self.front = 0
            self.rear = 0
            self.queue[self.front] = obj
            self.size = 1
            return
        self.front = (self.front - 1) % len(self.queue)
        self.queue[self.front] = obj
        self.size += 1

    def remove_front(self):
        if self.size == 0:
            print("Empty")
            return
        if self.size == 1:
            self.front = self.rear
            self.queue[self.front] = None
            self.size -= 1
            return
        self.queue[self.front] = None
        self.front = (self.front + 1) % len(self.queue)
        self.size -= 1

    def remove_end(self):
        if self.size == 0:
            print("Empty")
            return
        if self.size == 1:
            self.front = self.rear
            self.queue[self.rear] = None
            self.size -= 1
            return
        self.queue[self.rear] = None
        self.rear = (self.rear - 1) % len(self.queue)
        self.size -= 1

    def insert_end(self, obj):
        if self.size == len(self.queue):
            self.resize()
        if self.size == 0:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = obj
            self.size = 1
            return
        self.rear = (self.rear + 1) % len(self.queue)
        self.queue[self.rear] = obj
        self.size += 1

    def get_first(self):
        if self.size == 0:
            print("Empty")
            return
        return self.queue[self.front]

    def get_last(self):
        if self.size == 0:
            print("Empty")
            return
        return self.queue[self.rear]

    def display_queue(self):
        i = self.front
        print("List is ")
        while i != self.rear:
            print(self.queue[i])
            i = (i + 1) % len(self.queue)
        print(self.queue[self.rear])
        print()

    def print_current_queue(self):
        print(self.queue)

    def check_list(self, my_list):
        check = True
        n = 0
        i = self.front
        while i != self.rear:
            if self.queue[i] != None:
                if self.queue[i] != my_list[n]:
                    check = False
                    return check
                n += 1
            i = (i + 1) % len(self.queue)
        return check

