from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for question in question_data:
  question_bank.append(Question(question['text'], question['answer']))

quiz_brain = QuizBrain(0, question_bank)

print(question_bank[10].text)

while quiz_brain.still_has_questions():
  quiz_brain.next_question()