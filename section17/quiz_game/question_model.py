class Question:
  # set default parameters if none are provided
  def __init__(self, text='Sample text', answer='Sample answer'):
    self.text = text
    self.answer = answer


question = Question()

print(question.text, question.answer)
