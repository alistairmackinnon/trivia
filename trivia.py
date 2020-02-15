import requests
import base64


def get_questions(amount):
    request_url = f'https://opentdb.com/api.php?amount={amount}&type=boolean&encode=base64'
    response = requests.get(request_url)
    response_lst = response.json()
    questions = response_lst['results']
    for question_detail in questions:
        question = question_detail['question']
        question = base64.b64decode(question).decode('ascii')
        correct_answer = question_detail['correct_answer']
        correct_answer = base64.b64decode(correct_answer).decode('ascii')
        return question, correct_answer

if __name__ == "__main__":
    get_questions(1)
