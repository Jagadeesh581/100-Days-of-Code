from data import question_data
from question_model import Question
from question_brain import QuizBrain

question_bank = [Question(q_text=question["question"], q_answer=question["correct_answer"]) for question in
                 question_data]

quiz = QuizBrain(question_list=question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the Quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
