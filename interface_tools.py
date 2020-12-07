
class InterfaceTools:

    @staticmethod
    def get_valid_input(answers, input_question=""):
        print(input_question)
        input_variable = input("Please insert your answer>>>").lower()
        valid_answer = False
        while True:
            answer_values = len(answers)
            i = 0
            while i < answer_values:
                if input_variable == answers[i]:
                    valid_answer = True
                    break
                else:
                    i += 1
            if valid_answer == True:
                break
            print("Invalid answer, please type one of the following")
            for answer in answers:
                print(answer, "\t\t", end="")
            input_variable = input("").lower()
        final_answer = input_variable
        return final_answer

    @staticmethod
    def choose_following_from_list(my_list):
        i = 0
        j = 1
        number_of_questions = []
        while i < len(my_list):
            print(j, ")", my_list[i])
            number_of_questions.append(str(j))
            i += 1
            j += 1
        response = InterfaceTools.get_valid_input(number_of_questions)
        return response