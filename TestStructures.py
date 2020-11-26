from DataStructures.HashMap import HashMap
from DataStructures.HashSet import HashSet
from DataStructures.deque import Deque, CyclicArrayDeque
from DataStructures.doubly_linked_list import DoubleLinkedList
from DataStructures.queue import Queue, PriorityQueue
from DataStructures.singly_linked_list import SingleLinkedList
from DataStructures.stack import Stack


def main():
    test_single_linked_list()
    test_double_linked_list()
    test_stack()
    test_queue()
    test_priority_queue()
    test_deque()
    test_cyclic_array_deque()
    test_hash_set()
    test_hash_map()

def test_single_linked_list():
    test = True
    llist = SingleLinkedList()
    llist.insert_first(2)
    llist.insert_first(1)
    llist.insert_first(0)
    llist.insert_last(3)
    llist.insert_last(4)
    llist_elements = [0, 1, 2, 3, 4]
    if llist.check_list(llist_elements) == False:
        test = False
    llist.remove_first()
    llist.remove_last()
    llist.insert_after(1, "a")
    llist.insert_before(3, "b")
    llist.insert_after(3, "c")
    llist_elements1 = [1, "a", 2, "b", 3, "c"]
    if llist.check_list(llist_elements1) == False:
        test = False
    llist.remove_by_value(1)
    llist.remove_by_value(2)
    llist.remove_by_value(3)
    llist.reverse_linked_list()
    llist_elements2 = ["c", "b", "a"]
    if llist.check_list(llist_elements2) == False:
        test = False
    llist_elements3 = []
    llist.emplty_llist()
    if llist.check_list(llist_elements3) == False:
        test = False
    if test == True:
        print("SingleLinkedList test passed")
    else:
        print("SingleLinkedList test failed")


def test_double_linked_list():
    test = True
    dllist = DoubleLinkedList()
    dllist.insert_first(2)
    dllist.insert_first(1)
    dllist.insert_first(0)
    dllist.insert_last(3)
    dllist.insert_last(4)

    dllist_elements = [0, 1, 2, 3, 4]
    if dllist.check_list(dllist_elements) == False:
        test = False
    dllist.remove_first()

    dllist.remove_last()
    dllist.insert_after(1, "a")
    dllist.insert_before(3, "b")
    dllist.insert_after(3, "c")

    dllist_elements1 = [1, "a", 2, "b", 3, "c"]
    if dllist.check_list(dllist_elements1) == False:
        test = False

    dllist.remove_by_value(1)

    dllist.remove_numeric_nodes()

    dllist.reverse_list()
    dllist_elements2 = ["c", "b", "a"]
    if dllist.check_list(dllist_elements2) == False:
        test = False
    dllist_elements3 = ["c", "a"]
    dllist.remove_nodes_at_even_position()

    if dllist.check_list(dllist_elements3) == False:
        test = False

    if test == True:
        print("DoubleLinkedList test passed")
    else:
        print("DoubleLinkedList test failed")


def test_stack():
    test = True
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.pop()
    stack.pop()
    stack_elements = [2, 1]
    if stack.check_list(stack_elements) == False:
        test = False
    if stack.top() != 2 and stack.is_empty() == True:
        test = False
    stack.empty()
    if stack.get_size() != 0:
        test = False
    if test == True:
        print("Stack test passed")
    else:
        print("Stack test failed")


def test_queue():
    test = True
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.dequeue()
    queue.dequeue()
    queue_elements = [3, 4]
    if queue.check_list(queue_elements) == False:
        test = False
    if queue.get_first() != 3 and queue.is_empty() == True:
        test = False
    queue.empty()
    if queue.get_size() != 0:
        test = False
    if test == True:
        print("Queue test passed")
    else:
        print("Queue test failed")


def test_priority_queue():
    test = True
    pqueue = PriorityQueue()
    pqueue.enqueue(1)
    pqueue.enqueue(2)
    pqueue.enqueue(3)
    pqueue.enqueue("p1", 1)
    pqueue.enqueue("p2", 1)
    pqueue.enqueue("p3", 1)
    pqueue.dequeue()
    pqueue.dequeue()
    queue_elements = ["p3", 1, 2, 3]
    if pqueue.check_list(queue_elements) == False:
        test = False
    if pqueue.get_first() != "p3" and pqueue.is_empty() == True:
        test = False
    pqueue.empty()
    if pqueue.get_size() != 0:
        test = False
    if test == True:
        print("PriorityQueue test passed")
    else:
        print("PriorityQueue test failed")


def test_deque():
    test = True
    dque = Deque()
    dque.insert_front(1)
    dque.insert_front(2)
    dque.insert_front(3)
    dque.insert_end(2)
    dque.insert_end(3)
    dque_elements = [3, 2, 1, 2, 3]
    if dque.check_list(dque_elements) == False:
        test = False
    dque.remove_front()
    dque.remove_end()
    dque_elements1 = [2, 1, 2]
    if dque.check_list(dque_elements1) == False:
        test = False
    if dque.get_first() != 2 and dque.get_last() != 2:
        test = False
    if test == True:
        print("Deque test passed")
    else:
        print("Deque test failed")


def test_cyclic_array_deque():
    test = True
    cyclic_deque = CyclicArrayDeque()
    cyclic_deque.insert_front(1)
    cyclic_deque.insert_front(2)
    cyclic_deque.insert_front(3)
    cyclic_deque.insert_end(2)
    cyclic_deque.insert_end(3)
    dque_elements = [3, 2, 1, 2, 3]
    if cyclic_deque.check_list(dque_elements) == False:
        test = False
    cyclic_deque.remove_front()
    cyclic_deque.remove_end()
    dque_elements1 = [2, 1, 2]
    if cyclic_deque.check_list(dque_elements1) == False:
        test = False
    if cyclic_deque.get_first() != 2 and cyclic_deque.get_last() != 2:
        test = False
    if test == True:
        print("CyclicArrayDeque test passed")
    else:
        print("CyclicArrayDeque test failed")


def test_hash_set():
    test = True
    HS = HashSet(200)
    HS.add("a")
    HS.add("b")
    HS.add("c")
    HS1 = HashSet(200)
    HS1.add("c")
    HS1.add("d")
    HS1.add("e")
    for elem in HS.union(HS1):
        if HS.contains(elem) or HS1.contains(elem):
            pass
        else:
            test = False
    for elem in HS.intersection(HS1):
        if HS.contains(elem) and HS1.contains(elem):
            pass
        else:
            test = False
    my_set = ["d", "e"]
    i = 0
    HS1.subtraction(HS)
    for elem in HS1:
        if elem != my_set[i]:
            test = False
            break
        i += 1
    HS1.add("c")
    HS.union_update(HS1)
    HS.add("aa")
    HS.add("aaa")
    HS.add("cc")
    hash_set = ["a", "aa", "aaa", "b", "c", "cc", "d", "e"]
    i = 0
    for elem in HS:
        if elem != hash_set[i]:
            test = False
        i += 1
    if test == True:
        print("HashSet test passed")
    else:
        print("HashSet test failed")

def test_hash_map():
    test = True
    HM = HashMap(10)
    HM.put("Name", "Petros Petrosyan")
    HM.put("ID", 1034)
    HM.put("Major", "B.S. Electrical Engineering")
    HM.put("Credits Earned", 30)
    HM.put("GPA", 3.3)
    if HM.has_key("Name") == False:
        test = False
    if HM.has_value("Petros Petrosyan") == False:
        test = False
    if HM.has_key("GPA") == False:
        test = False
    if HM.has_key("Highschool GPA") == True:
        test = False
    if HM.has_key("Credits Earned") == False:
        test = False
    HM.update("Credits Earned", 45)
    HM.update("GPA", 3.4)
    if HM.get("Credits Earned") != 45:
        test = False
    HM.remove("ID")
    if HM.get("ID") != None:
        test = False
    if test == True:
        print("HashMap test passed")
    else:
        print("HashMap test failed")

main()