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

    imported_to_json = False

    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        self.priority_size = 0
        self.name_json = None

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def empty(self):
        if self.size != 0:
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
        else:
            temp = self.last
            self.last.next = node
            self.last = node
            self.last.previous = temp
            self.last.next = None
            self.size += 1
        if PriorityQueue.imported_to_json:
            PriorityQueue.update_json_file(self, self.name_json, obj, priority)

    def dequeue(self):
        if self.first == None:
            return
        if self.size == 1:
            if self.priority_size == 1:
                self.priority_size -= 1
            if PriorityQueue.imported_to_json:
                PriorityQueue.remove_from_json_file(self, self.name_json, self.first.data)
            self.first = None
            self.last = None
            self.size -= 1
            return

        if self.priority_size == 0:
            if PriorityQueue.imported_to_json:
                PriorityQueue.remove_from_json_file(self, self.name_json, self.first.data)
            self.first = self.first.next
            self.first.previous = None
            # self.first.next = None
            self.size -= 1
            return
        else:
            tmp = self.first
            while tmp.priority == 2:
                tmp = tmp.next
            if tmp.previous is None:
                if PriorityQueue.imported_to_json:
                    PriorityQueue.remove_from_json_file(self, self.name_json, self.first.data)
                self.first = self.first.next
                self.first.previous = None
                tmp.next = None
                self.size -= 1
                self.priority_size -= 1
                return
            if tmp.next is None:
                if PriorityQueue.imported_to_json:
                    PriorityQueue.remove_from_json_file(self, self.name_json, tmp.previous.next.data)
                tmp.previous.next = None
                self.size -= 1
                self.priority_size -= 1
            else:
                # print(tmp.next.data)
                # print(tmp.data)
                # print(tmp.previous.data)
                if PriorityQueue.imported_to_json:
                    PriorityQueue.remove_from_json_file(self, self.name_json, tmp)
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

    def import_to_json(self, name):
        if self.size != 0:
            if not PriorityQueue.imported_to_json:
                import json
                saved_data_dict = {}
                tmp = self.first
                while tmp.next is not None:
                    saved_data_dict[tmp.data] = tmp.priority
                    tmp = tmp.next
                saved_data_dict[tmp.data] = tmp.priority
                x = name
                y = ".json"
                z = x + y
                file_2 = open(z, "w")
                file_2.write(json.dumps(saved_data_dict, indent=2))
                file_2.close()
                self.name_json = name
                PriorityQueue.imported_to_json = True

    def import_from_json(self, name):
        PriorityQueue.empty(self)
        import json
        with open(name) as file:
            name = json.load(file)
        for key, value in name.items():
            self.enqueue(key, value)
        file.close()

    def update_json_file(self, name, obj, priority):
        import json
        x = name
        y = ".json"
        z = x + y
        with open(z) as open_file:
            name = json.load(open_file)
        name[obj] = priority
        json.dump(name, open(z, "w"), indent=2)
        open_file.close()
        self.name_json = name

    def remove_from_json_file(self, name, obj):
        import json
        x = name
        y = ".json"
        z = x + y
        with open(z) as open_file:
            name = json.load(open_file)
        del name[obj]
        json.dump(name, open(z, "w"), indent=2)
        open_file.close()
        self.name_json = name
