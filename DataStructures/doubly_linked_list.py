class Node:
    def __init__(self, data, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous


class DoubleLinkedList:
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

    def print_list(self):
        print("Printing Linked List Elements")
        current = self.first
        while current is not None:
            print(str(current.data))
            current = current.next
        print()

    def insert_first(self, obj):
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
        self.first.previous = None
        tmp.next = None
        self.size -= 1

    def remove_last(self):
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

    def insert_last(self, obj):
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

    def insert_after(self, obj, new_obj):
        if self.size == 0:
            print("List is empty")
            return
        else:
            current = self.first
            while current is not None:
                if current.data == obj:
                    break
                current = current.next
            if current is None:
                print("item not in the list")
            else:
                node = Node(new_obj)
                node.previous = current
                node.next = current.next
                if current.next is not None:
                    current.next.previous = node
                current.next = node
                self.size += 1

    def insert_before(self, obj, new_obj):
        if self.size == 0:
            print("List is empty")
            return
        else:
            current = self.first
            while current is not None:
                if current.data == obj:
                    break
                current = current.next
            if current is None:
                print("item not in the list")
            else:
                node = Node(new_obj)
                node.next = current
                node.previous = current.previous
                if current.previous is not None:
                    current.previous.next = node
                current.previous = node
                self.size += 1

    def remove_before(self, obj):
        if self.size == 0:
            print("List is empty")
            return
        elif self.first.data == obj:
            print("No elements before this one")
        elif self.size == 2:
            self.first = None
            self.first = self.last
            self.size -= 1
        elif self.first.next.data == obj:
            temp = self.first
            self.first = None
            self.first = temp.next
        else:
            current = self.first.next.next
            while current is not None:
                if current.data == obj:
                    break
                current = current.next
            if current is None:
                print("item not in the list")
            else:
                current.previous = current.previous.previous
                current.previous.next = current

    def index_of(self, obj):
        if self.size == 0:
            print("List is empty")
            return
        position = 1
        current = self.first
        while current != None:
            if current.data == obj:
                print("index is", position)
                return position
            position += 1
            current = current.next
        print("Item not found in list")

    def remove_by_value(self, obj):
        if self.size == 0:
            print("The list has no element to delete")
            return
        if self.first.next is None:
            if self.first.data == obj:
                self.first = None
                self.last = None
                self.size -= 1
            else:
                print("Item not found")
            return

        if self.first.data == obj:
            self.first = self.first.next
            self.first.previous = None
            self.size -= 1
            return

        current = self.first
        while current.next is not None:
            if current.data == obj:
                break
            current = current.next
        if current.next is not None:
            current.previous.next = current.next
            current.next.previous = current.previous
            self.size -= 1
        else:
            if current.data == obj:
                self.last = self.last.previous
                self.last.next = None
                self.size -= 1
            else:
                print("Element not found")

    def reverse_list(self):
        if self.size == 0:
            print("The list has no elements to reverse")
            return
        if self.size == 1:
            return
        temp = self.first
        current = self.first
        after_current = current.next
        current.next = None
        current.previous = after_current
        while after_current is not None:
            after_current.previous = after_current.next
            after_current.next = current
            current = after_current
            after_current = after_current.previous
        self.first = current
        self.last = temp

    def remove_numeric_nodes(self):
        if self.size == 0:
            print("The list has no element to delete")
            return
        if self.size == 1:
            if self.first.data.isnumeric() == True:
                self.first = None
                self.size -= 1
            else:
                print("No numeric node")
                return

        if str(self.first.data).isnumeric() == True:
            self.first = self.first.next
            self.first.previous = None
            self.size -= 1

        current = self.first
        while current.next is not None:
            if str(current.data).isnumeric() == True:
                current.previous.next = current.next
                current.next.previous = current.previous
                self.size -= 1
            current = current.next
        if current.next is None:
            if str(current.data).isnumeric() == True:
                current.previous.next = None
                self.size -= 1


    def remove_nodes_at_even_position(self):
        if (self.size % 2) == 0:
            self.last = self.last.previous
            self.last.next = None
        current = self.first.next
        while current is not None:
            self.remove_by_value(current.data)
            if current.next is not None:
                current = current.next.next
            else:
                break

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