from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for item in question_data:
    new_text = item["text"]
    new_answer = item["answer"]
    new_question = Question(new_text, new_answer)
    question_bank.append(new_question)

quizbrain = QuizBrain(question_bank)
quizbrain.next_question()