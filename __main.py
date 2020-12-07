from DataStructures.HashMap import HashMap
from DataStructures.queue import PriorityQueue
from DataStructures.singly_linked_list import SingleLinkedList
from interface_tools import InterfaceTools


class HealthUtilityIndex:
    llist = SingleLinkedList()

    def __init__(self):
        self.health_index_sum = 11
        self.healthcare = 0
        self.percentile_health = 0
        self.percentile_care = 0

    def get_index(self):
        return self.health_index_sum

    def get_healthcare(self):
        return self.healthcare

    def get_index_percentile(self):
        return self.percentile_health

    def get_percentile_healthcare(self):
        return self.percentile_care

    @classmethod
    def retrieve_questions_and_answers(cls):
        import json
        with open('questions.json') as open_file:
            questions = json.load(open_file)
        import json
        with open('answer_values.json') as open_file_1:
            answers = json.load(open_file_1)
        return questions, answers

    def convert_data_and_calculate_index(self):
        questions, answers = HealthUtilityIndex.retrieve_questions_and_answers()
        n = 0
        while n < len(questions):
            for value in questions[n].values():
                HealthUtilityIndex.llist.insert_last(value)
            for value in answers[n].values():
                HealthUtilityIndex.llist.insert_last(value)
            if HealthUtilityIndex.llist.get_first() is not None:
                print(HealthUtilityIndex.llist.get_first())
                HealthUtilityIndex.llist.remove_first()
            else:
                HealthUtilityIndex.llist.remove_first()
            print(HealthUtilityIndex.llist.get_first())
            HealthUtilityIndex.llist.remove_first()
            user_answer = InterfaceTools.choose_following_from_list(HealthUtilityIndex.llist.get_first())
            HealthUtilityIndex.llist.remove_first()
            j = 1
            while j < int(user_answer):
                HealthUtilityIndex.llist.remove_first()
                j += 1
            self.health_index_sum = self.health_index_sum - HealthUtilityIndex.llist.get_first()
            HealthUtilityIndex.llist.emplty_llist()
            n += 1

    def determine_index_percentile(self):
        if self.health_index_sum <= 0.43352:
            print("You are healthier than 1 percent of americans")
            self.percentile_health = 1
        if 0.43352 < self.health_index_sum <= 0.612233:
            print("You are healthier than 5 percent of americans")
            self.percentile_health = 5
        if 0.612233 < self.health_index_sum <= 0.705392:
            print("You are healthier than 10 percent of americans")
            self.percentile_health = 10
        if 0.705392 < self.health_index_sum <= 0.805017:
            print("You are healthier than 50 percent of americans")
            self.percentile_health = 50
        if 0.805017 < self.health_index_sum <= 0.916525:
            print("You are healthier than 75 percent of americans")
            self.percentile_health = 75
        if 0.916525 < self.health_index_sum <= 0.936914:
            print("You are healthier than 90 percent of americans")
            self.percentile_health = 90
        if 0.936914 < self.health_index_sum <= 0.98565:
            print("You are healthier than 95 percent of americans")
            self.percentile_health = 95
        if 0.98565 < self.health_index_sum <= 1:
            print("You are healthier than 99 percent of americans")
            self.percentile_health = 99

    def compare_healthcare(self):
        print("\n")
        healthcare_input = input("Please input your annual healthcare spendings($)")
        while True:
            string_decimal = "." in healthcare_input
            if string_decimal == True:
                decimal_point_index = healthcare_input.find(".")
                input_after_decimal = healthcare_input[decimal_point_index + 1:]
                healthcare_input = healthcare_input[0:decimal_point_index]
            else:
                input_after_decimal = "0"
            if healthcare_input.isnumeric() and input_after_decimal.isnumeric():
                break
            else:
                healthcare_input = input("Invalid answer, please type a number")

        while True:
            if healthcare_input.isnumeric():
                healthcare = int(healthcare_input)
                if healthcare == 0:
                    self.percentile_care = 10
                    print("You spend as much as 10 percent of Americans")
                if 219 >= healthcare > 0:
                    self.percentile_care = 25
                    print("You spend more than 10 percent of Americans")
                if 1052 >= healthcare > 219:
                    self.percentile_care = 50
                    print("You spend more than 50 percent of Americans")
                if 3436 >= healthcare > 1052:
                    self.percentile_care = 75
                    print("You spend more than 50 percent of Americans")
                if 8510 >= healthcare > 3436:
                    self.percentile_care = 90
                    print("You spend more than 75 percent of Americans")
                if 14602 >= healthcare > 8510:
                    self.percentile_care = 90
                    print("You spend more than 90 percent of Americans")
                if 40862 >= healthcare > 14602:
                    self.percentile_care = 95
                    print("You spend more than 95 percent of Americans")
                if healthcare > 40862:
                    self.percentile_care = 99
                    print("You spend more than 99 percent of Americans")
                break
            else:
                healthcare_input = input("Invalid answer, type a number")
        self.healthcare = healthcare

    def compare_percentiles(self):
        if self.percentile_health >= self.percentile_care:
            print("\n", "Everything is fine, you healthcare works for you")
        else:
            print("\n", "NOT good, your spendings on healthcare exceed your level of health")


class User:
    waiting = PriorityQueue()
    users = HashMap(1000)
    HM = HashMap(20)

    def __init__(self):
        self.username = None
        self.password = None
        self.index = None
        self.index_percentile = None
        self.healthcare = None
        self.healthcare_percentile = None
        self.name = None
        self.email = None
        self.age = None
        self.gender = None
        self.country = None

    def return_index(self):
        return self.index

    def return_index_percentile(self):
        return self.index_percentile

    def return_healthcare(self):
        return self.healthcare

    def return_healthcare_percentile(self):
        return self.healthcare_percentile

    def return_email(self):
        return self.email

    def return_name(self):
        return self.name

    def return_gender(self):
        return self.gender

    def return_age(self):
        return self.age

    def return_country(self):
        return self.country

    def user_signup(self):
        print("Select one")
        user_input = InterfaceTools.choose_following_from_list(["New User", "Returning User"])
        if user_input == "1":
            while True:
                user_name = input("Please insert a username")
                n = User.users.has_key(user_name)
                if n == False:
                    break
                print("username taken, try again")
            self.username = user_name
            self.password = input("Please set a password")
            User.users.update_json_file("my_users", self.username, self.password)
        if user_input == "2":
            x = User.check_username()
            self.username = x
            self.password = User.check_password(x)
            y = ".json"
            z = x + y
            User.HM.import_from_json(z)

    @classmethod
    def check_username(cls):
        print("Username")
        input_variable = input("Please insert your answer>>>")
        while True:
            if User.users.has_key(input_variable):
                break
            print("Invalid, try again")
            input_variable = input("")
        return input_variable

    @classmethod
    def check_password(cls, username):
        print("Password")
        input_variable = input("Please insert your answer>>>")
        while True:

            if input_variable == User.users.get(username):
                break
            print("Invalid, try again")
            input_variable = input("")
        return input_variable

    def set_retrieved_info_1(self):
        self.index = User.HM.get("Index")
        self.index_percentile = User.HM.get("Percentile for Index")
        self.healthcare = User.HM.get("Healthcare Expenses Amount")
        self.healthcare_percentile = User.HM.get("Percentile for Healthcare Expenses")

    def set_retrieved_info_2(self):
        self.name = User.HM.get("Name")
        self.email = User.HM.get("Email")
        self.age = User.HM.get("Age")
        self.gender = User.HM.get("Gender")
        self.country = User.HM.get("Country")

    def get_and_set_user_info(self):
        HUI = HealthUtilityIndex()
        HUI.retrieve_questions_and_answers()
        HUI.convert_data_and_calculate_index()
        HUI.determine_index_percentile()
        HUI.compare_healthcare()
        HUI.compare_percentiles()
        self.index = HUI.get_index()
        self.healthcare = HUI.get_healthcare()
        self.index_percentile = HUI.get_index_percentile()
        self.healthcare_percentile = HUI.get_percentile_healthcare()

    def save_info(self):
        User.HM.put("Index", self.index)
        User.HM.put("Percentile for Index", self.index_percentile)
        User.HM.put("Healthcare Expenses Amount", self.healthcare)
        User.HM.put("Percentile for Healthcare Expenses", self.healthcare_percentile)
        User.HM.import_to_json(self.username)
        return User.HM

    def get_additional_info(self):
        self.name = input("Please type your name")
        self.email = input("Please type email")
        self.age = input("Please type age")
        self.gender = input("Please type gender")
        self.country = input("Please type country of residence")
        User.HM.put("Name", self.name)
        User.HM.put("Email", self.email)
        User.HM.put("Age", self.age)
        User.HM.put("Gender", self.gender)
        User.HM.put("Country", self.country)
        User.HM.import_to_json(self.username)

    def register_for_consultation(self, obj):
        import json
        with open("waiting_room.json") as file:
            people_waiting = json.load(file)
        for person in people_waiting.keys():
            if person == self.username:
                print("Already Registered")
                return
        if self.index > 0.5:
            User.waiting.update_json_file("waiting_room", obj, 2)
        if self.index <= 0.5:
            User.waiting.update_json_file("waiting_room", obj, 1)
            return True


def main():
    User.users.import_from_json("my_users.json")
    user1 = User()
    user1.user_signup()
    while True:
        print()
        print("Would you like to")
        option = InterfaceTools.choose_following_from_list([
            "Check Utility index",
            "View Saved Info",
            "Schedule a consultation",
            "Exit"
        ])
        if option == "1":
            if User.HM.size == 0:
                user1.get_and_set_user_info()
                User.HM = user1.save_info()
            else:
                print("Already Calculated")
        if option == "2":
            User.HM.iterate()
        if option == "3":
            if User.HM.size != 0:
                user1.set_retrieved_info_1()
                if User.HM.get("Email") is None:
                    user1.get_additional_info()
                else:
                    user1.set_retrieved_info_2()
                if user1.register_for_consultation(user1.username):
                    print("Consultation registered, wait for email")
            else:
                print("Please calculate index first", "\n")
        if option == "4":
            print("Thank you, See you Later!!!")
            break


main()
