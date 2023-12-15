class QuizBrain:
  def __init__(self, question_number, question_list):
    self.has_questions = True
    self.question_number = 0
    self.question_list = question_list

  def next_question(self):
    current_question = self.question_list[self.question_number]
    self.question_number += 1
    input(f"Q.{self.question_number}: {current_question.text}. (True/False)?")

  def still_has_questions(self):
    self.has_questions = True if self.question_number <= len(self.question_list) else False
    return self.has_questions
