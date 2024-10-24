from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# new_q = Question(question_data[0]["text"], question_data[0]["answer"])
# print(new_q.text, new_q.answer)

question_bank = []
index = 0

score = 0

for item in question_data:
    new_q = Question(question_data[index]["text"], question_data[index]["answer"])
    question_bank.append(new_q)
    index += 1

# print(question_bank)

# for item in range (0, 12):
#     question = input(f"Q.{quiz_brain.question_number + 1}: {question_bank[quiz_brain.question_number].text}.
#     (True/False). ")
#     if question == question_bank[quiz_brain.question_number].answer:
#         score += 1
#         print("You got it right! ")
#         print(f"The correct answer was: {question_bank[quiz_brain.question_number].answer}. ")
#         print(f"Your current score is: {score}/{quiz_brain.question_number + 1} ")
#     else:
#         print("That's wrong. ")
#         print(f"The correct answer was: {question_bank[quiz_brain.question_number].answer}. ")
#         print(f"Your current score is: {score}/{quiz_brain.question_number + 1} ")
#     quiz_brain.next_question()

quiz_brain = QuizBrain(question_bank)

while quiz_brain.still_has_question():
    quiz_brain.next_question()

if quiz_brain.still_has_question() == False:
    print("You've completed the quiz. ")
    print(f"Your final score was: {quiz_brain.score}/{quiz_brain.question_number} ")
