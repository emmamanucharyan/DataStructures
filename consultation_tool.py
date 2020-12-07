from DataStructures.HashMap import HashMap
from DataStructures.queue import PriorityQueue
from interface_tools import InterfaceTools

HM = HashMap(20)
que = PriorityQueue()
que.import_from_json('waiting_room.json')
que.import_to_json("waiting_room")

while True:
    print("\n", "Hello, would you like to")
    option = InterfaceTools.choose_following_from_list(["View next user in waiting", "Remove user in waiting(NEXT)", "Exit"])
    if option == "1":
        if que.get_size() != 0:
            a = str(que.get_first())
            b = ".json"
            c = a + b
            print(c)
            HM.import_from_json(c)
            HM.iterate()
        else:
            print("Waiting Room Empty")
    if option == "2":
        if que.get_size() != 0:
            que.dequeue()
        else:
            print("Waiting Room Empty")
    if option == "3":
        break

