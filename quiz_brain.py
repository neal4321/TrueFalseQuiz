class quiz_brain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        user_answer = input(f"Q{self.question_number+1}. {self.question_list[self.question_number].text} (True/False)?: ").lower()
        if user_answer == self.question_list[self.question_number].answer.lower():
            print("Congratulations you got it right!")
            print(f"The correct answer was {self.question_list[self.question_number].answer}")
            self.question_number += 1
            self.score += 1
            print(f"Your current score is {self.score}/{self.question_number}\n")
        else:
            print("Sorry. That was incorrect.")
            print(f"The correct answer was {self.question_list[self.question_number].answer}")
            self.question_number += 1
            print(f"Your final score is {self.score}/{self.question_number}\n")

    def check_score(self):
        if self.question_number == len(self.question_list):
            print("Congratulations! You completed all the questions!")
            print(f"Your final score is {self.score}/{self.score}")
            return False
        else:
            return True
