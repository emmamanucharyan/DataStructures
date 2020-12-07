class Node:
    def __init__(self, key, data, next=None):
        self.key = key
        self.value = data
        self.next = next


class HashMap:
    imported_to_json = False

    def __init__(self, capacity):
        self.capacity = capacity
        self.hashtable = [None] * capacity
        self.size = 0
        self.name_json = None

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
        index = self._hash(self._elem.value)
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

    def _hash(self, element):
        return hash(element) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        if self.hashtable[index] == None:
            self.hashtable[index] = Node(key, value)
            self.size += 1
        else:
            tmp = self.hashtable[index]
            while tmp.next != None:
                tmp = tmp.next
            if tmp.key == key:
                # print("Such key already exists")
                return
            n = Node(key, value)
            tmp.next = n
            self.size += 1
        if HashMap.imported_to_json:
            HashMap.update_json_file(self, self.name_json, key, value)

    def remove(self, key):
        if not HashMap.has_key(self, key):
            print("Not in set")
            return
        index = self._hash(key)
        n = self.hashtable[index]
        p = None
        while n != None:
            if n.key == key:
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

    def update(self, key, value):
        if HashMap.has_key(self, key):
            HashMap.remove(self, key)
            HashMap.put(self, key, value)
        else:
            print("No such entry with that key")

    def get(self, key):
        index = self._hash(key)
        n = self.hashtable[index]
        while (n != None):
            if (n.key == key):
                return n.value
            n = n.next
        return None

    def has_key(self, key):
        index = self._hash(key)
        n = self.hashtable[index]
        while (n != None):
            if (n.key == key):
                return True
            n = n.next
        return False

    def has_value(self, value):
        j = 0
        for e in self.hashtable:
            while e != None:
                if e.value == value:
                    j += 1
                e = e.next
        if j == 0:
            return False
        else:
            return True, j

    def size(self):
        return self.size

    def iterate(self):
        for e in self.hashtable:
            while e != None:
                print(e.key, ":", e.value)
                e = e.next

    def level_order_iterator(self):
        my_queue = []
        for e in self.hashtable:
            if e is not None:
                my_queue.append(e)
        while len(my_queue) > 0:
            print(my_queue[0].key, ":", my_queue[0].value)
            if my_queue[0].next is not None:
                my_queue.append(my_queue[0].next)
            my_queue.pop(0)

    def import_to_json(self, name):
        if not HashMap.imported_to_json:
            import json
            saved_data_dict = {}
            for e in self.hashtable:
                while e != None:
                    saved_data_dict[e.key] = e.value
                    e = e.next
            x = name
            y =".json"
            z = x + y
            file_2 = open(z, "w")
            file_2.write(json.dumps(saved_data_dict, indent=2))
            file_2.close()
            self.name_json = name
            HashMap.imported_to_json = True
        else:
            pass
            # print("already imported")

    def import_from_json(self, name):
        for e in self.hashtable:
            while e != None:
                HashMap.remove(self, e.key)
                e = e.next
        import json
        with open(name) as open_file:
            file = json.load(open_file)
            open_file.close()
        for key, value in file.items():
            self.put(key, value)

    def update_json_file(self, name, key, value):
        import json
        x = name
        y = ".json"
        z = x + y
        with open(z) as open_file:
            file = json.load(open_file)
        file[key] = value
        json.dump(file, open(z, "w"), indent=2)
        open_file.close()



