from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

# data can be swapped out and different sources can be used as long as the correct keys are passed to match data structure
## eg, https://opentdb.com/api_config.php
### https://opentdb.com/api.php?amount=10&category=18&difficulty=easy&type=boolean
for question in question_data:
  question_bank.append(Question(question['text'], question['answer']))

quiz_brain = QuizBrain(0, question_bank)

print(question_bank[10].text)

while quiz_brain.still_has_questions():
  quiz_brain.next_question()