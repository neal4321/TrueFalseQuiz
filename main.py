from data import question_data
from question_model import Question
from quiz_brain import quiz_brain

question_bank = []

for i in question_data:
    question = Question(i["text"], i["answer"])
    question_bank.append(question)

quiz = quiz_brain(question_bank)

while quiz.check_score():
    quiz.next_question()
