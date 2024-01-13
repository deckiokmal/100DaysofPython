# Controller


class QuizBrain:
    score = 0

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        questions = self.question_list[self.question_number]
        self.question_number += 1
        answer = input(
            f"Q.{self.question_number}: {questions.question}. (True/False)?: "
        )
        self.check_answer(answer, questions.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            QuizBrain.score += 1
            print("You got it right!")
        else:
            print("Wrong answer.")

        print(f"The correct answer was {correct_answer}")
        print(
            f"Your score is {QuizBrain.score} from {self.question_number} Questions.\n\n"
        )
