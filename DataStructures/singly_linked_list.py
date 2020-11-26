class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next


class SingleLinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def get_size(self):
        return self.size

    def get_first(self):
        return self.first

    def get_last(self):
        return self.last

    def insert_first(self, obj):
        node = Node(obj, self.first)
        self.first = node
        if self.last == None:
            self.last = node
        self.size += 1

    def remove_first(self):
        if self.first == None:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first
        self.first = self.first.next
        tmp.next = None
        self.size -= 1

    def insert_last(self, obj):
        node = Node(obj, None)
        if self.last == None:
            self.first = node
            self.last = node
            self.size += 1
            return
        self.last.next = node
        self.last = node
        self.size += 1

    def remove_last(self):
        if self.size == 0:
            return
        if self.size == 1:
            self.first = None
            self.last = None
            self.size -= 1
            return
        tmp = self.first

        while tmp.next != self.last:
            tmp = tmp.next

        tmp.next = None
        self.last = tmp
        self.size -= 1

    def find(self, obj):
        if self.size == 0:
            print("There are no Nodes to find")
            return
        current = self.first
        while current != self.last:
            if current.data == obj or (current.next == self.last and current.next.data == obj):
                return obj
            current = current.next
        print("Not in List")
        return None

    def insert_before(self, obj, new_obj):
        if self.size == 0:
            print("There are no Nodes to insert before.")
            return
        current = self.first
        if self.first == obj:
            self.insert_first(new_obj)
        while current != self.last:
            if current.next.data == obj or (current.next == self.last and current.next.data == obj):
                node = Node(new_obj)
                after_insert = current.next
                node.next = after_insert
                current.next = node
                self.size += 1
                return
            current = current.next
        print("The node you want to insert before doesn't exist.")
        return None

    def insert_after(self, obj, new_obj):
        if self.size == 0:
            print("There are no Nodes to insert after.")
            return
        current = self.first
        while current != None:
            if current.data == obj:
                node = Node(new_obj)
                node.next = current.next
                current.next = node
                self.size += 1
                return
            current = current.next
        print("The node you want to insert before doesn't exist.")
        return None

    def remove_by_value(self, obj):
        if self.size == 0:
            print("The list has no element to delete")
            return
        if self.first.data == obj:
            self.first = self.first.next
            self.size -= 1
            return
        current = self.first
        while current.next is not None:
            if current.next.data == obj:
                current.next = current.next.next
                self.size -= 1
                return
            current = current.next
        print("Not found in the list")


    def insert_at_index(self, index, data):
        if index == 1:
            node = Node(data)
            node.next = self.first
            self.first = node
            self.size += 1
        i = 1
        current = self.first
        while i < index - 1 and current is not None:
            current = current.next
            i = i + 1
        if current is None:
            print("Index out of bound")
        else:
            node = Node(data)
            node.next = current.next
            current.next = node

    def remove_by_index(self, index):
        if index == 1:
            self.first = self.first.next
            self.size -= 1
            return
        i = 1
        current = self.first
        while i < index - 1 and current.next is not None:
            current = current.next
            i = i + 1
        if index > self.size:
            print("Index out of bound")
        else:
            current.next = current.next.next
            self.size -= 1

    def emplty_llist(self):
        self.first.next = None
        self.last = None
        self.first = None
        self.size = 0

    def reverse_linked_list(self):
        prev = None
        current = self.first
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.first = prev

    def print_list(self):
        print("Printing Linked List Elements")
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

