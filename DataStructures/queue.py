class Node:
    def __init__(self, data, priority=2):
        self.data = data
        self.next = None
        self.previous = None
        self.priority = priority


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def empty(self):
        self.first.next = None
        self.last = None
        self.first = None
        self.size = 0

    def enqueue(self, obj):
        node = Node(obj)
        if self.last == None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def dequeue(self):
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

    def get_first(self):
        return (str(self.first.data))

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


class PriorityQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        self.priority_size = 0

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def empty(self):
        self.first.next = None
        self.last = None
        self.first = None
        self.size = 0

    def enqueue(self, obj, priority=2):
        if priority != 2:
            self.priority_size += 1
            node = Node(obj, 1)
        else:
            node = Node(obj)
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

    def dequeue(self):
        if self.first == None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        if self.priority_size == 0:
            self.first = self.first.next
            self.first.previous = None
            tmp.next = None
            self.size -= 1
        else:
            while tmp.priority != 1:
                tmp = tmp.next
            tmp.previous.next = tmp.next
            tmp.next.previous = tmp.previous
            self.size -= 1
            self.priority_size -= 1

    def get_first(self):
        if self.priority_size == 0:
            return self.first.data
        tmp = self.first
        while tmp.priority != 1:
            tmp = tmp.next
        return tmp.data

    def check_list(self, my_list):
        check = True
        current = self.first
        p = 0
        n = self.priority_size
        if self.priority_size != 0:
            while p < self.priority_size:
                tmp = self.first
                while tmp is not None:
                    if tmp.priority == 1:
                        if tmp.data != my_list[p]:
                            check = False
                            return check
                        p += 1
                    tmp = tmp.next

        while n < len(my_list):
            if current.priority == 2:
                if current.data != my_list[n]:
                    check = False
                    return check
            current = current.next
            n += 1

        return check
