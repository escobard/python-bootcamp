class QuizBrain:
  def __init__(self, question_number, question_list):
    self.has_questions = True
    self.score = 0
    self.question_number = 0
    self.question_list = question_list

  def next_question(self):
    if self.has_questions:
      current_question = self.question_list[self.question_number]
      self.question_number += 1
      user_answer = input(f"Q.{self.question_number}: {current_question.text}. (True/False)?")
      # call a python method within this class
      self.check_answer(user_answer, current_question.answer)
    else:
      print("You've completed the quiz")
      print(f"Your final score was: {self.score} / {self.question_number}")

  def still_has_questions(self):
    # when question number reaches equal length as length, there will be no questions left
    self.has_questions = True if self.question_number < len(self.question_list) else False
    return self.has_questions

  def check_answer(self, user_answer, correct_answer):
    if user_answer == correct_answer.lower():
      print('You got it right!')
      self.score += 1
    else:
      print('You got it wrong.')
    print(f"The correct answer was: {correct_answer}")
    print(f"Your current score is: {self.score}/{self.question_number}")