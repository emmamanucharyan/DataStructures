class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class HashSet:
    def __init__(self, capacity):
        self.hashtable = [None] * capacity
        self.capacity = capacity
        self.size = 0

    def _hash(self, element):
        # return hash(element) % self.capacity
        return ord(element[0]) % self.capacity

    def add(self, element):
        index = self._hash(element)
        if HashSet.contains(self, element):
            print("Object already in set")
            return
        if self.hashtable[index] == None:
            self.hashtable[index] = Node(element)
            self.size += 1
        else:
            tmp = self.hashtable[index]
            while tmp.next != None:
                tmp = tmp.next
            n = Node(element)
            tmp.next = n
            self.size += 1

    def contains(self, element):
        index = self._hash(element)
        n = self.hashtable[index]
        while (n != None):
            if (n.data == element):
                return True
            n = n.next
        return False

    def remove(self, element):
        if not HashSet.contains(self, element):
            print("Not in set")
            return
        index = self._hash(element)
        n = self.hashtable[index]
        p = None
        while n != None:
            if n.data == element:
                if p == None:
                    self.hashtable[index] = n.next
                else:
                    p.next = n.next
                    n.next = None
                    self.size -= 1
                    return n
            p = n
            n = n.next
        return None

    def size(self):
        return self.size

    def intersection(self, s):
        newSet = HashSet(100)
        for e in self.hashtable:
            while (e != None):
                if (s.contains(e.data)):
                    newSet.add(e.data)
                e = e.next
        return newSet

    def intersection_update(self, s):
        for e in self.hashtable:
            while (e != None):
                if not s.contains(e.data):
                    r = e
                    e = e.next
                    self.remove(r.data)
                    continue
                else:
                    e = e.next

    def union(self, s):
        new_set = HashSet(100)
        for e in s.hashtable:
            while (e != None):
                new_set.add(e.data)
                e = e.next
        for e in self.hashtable:
            while (e != None):
                if not s.contains(e.data):
                    new_set.add(e.data)
                e = e.next
        return new_set

    def union_update(self, s):
        for e in s.hashtable:
            while (e != None):
                if not self.contains(e.data):
                    self.add(e.data)
                e = e.next

    def subtraction(self, s):
        for e in s.hashtable:
            while (e != None):
                if self.contains(e.data):
                    self.remove(e.data)
                e = e.next

    def __iter__(self):
        for e in self.hashtable:
            if (e != None):
                self._elem = e
                break
        return self

    def __next__(self):
        if self._elem == None:
            raise StopIteration
        tmp = self._elem
        index = self._hash(self._elem.data)
        if (self._elem.next != None):
            self._elem = self._elem.next
            return tmp.data
        else:
            self._elem = None
        for i in range(index + 1, len(self.hashtable)):
            if (self.hashtable[i] != None):
                self._elem = self.hashtable[i]
                break
        return tmp.data



    def iterate(self):
        for e in self.hashtable:
            while e != None:
                print(e.data)
                e = e.next

    def level_order_iterator(self):
        my_queue = []
        for e in self.hashtable:
            if e != None:
                my_queue.append(e)
        while len(my_queue) > 0:
            print(my_queue[0].data)
            if my_queue[0].next != None:
                my_queue.append(my_queue[0].next)
            my_queue.pop(0)


