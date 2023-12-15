class QuizBrain:
  def __init__(self, question_number, question_list):
    self.question_number = 0
    self.question_list = question_list

  def question_input(self, question_number):
    question = self.question_list[question_number]
    input(f"{question}. (True/False)?")
