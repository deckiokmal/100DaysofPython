# View

from question_model import TriviaQuestion
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    questions = question["question"]
    correct_answer = question["correct_answer"]
    new_questions = TriviaQuestion(questions, correct_answer)
    question_bank.append(new_questions)

quiz_questions = QuizBrain(question_bank)


while quiz_questions.still_has_question():
    quiz_questions.next_question()

print("You've completed the quiz.")
print(f"Your final score was: {quiz_questions.score}/{quiz_questions.question_number} ")
