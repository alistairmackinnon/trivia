import requests
import base64


def get_questions():
    request_url = f'https://opentdb.com/api.php?amount={amount}&type=boolean&encode=base64'
    response = requests.get(request_url)
    response_lst = response.json()
    return response_lst['results']


print('How many questions would you like?')
amount = input()

questions = get_questions()

for question_detail in questions:
    question = question_detail['question']
    question = base64.b64decode(question).decode('ascii')
    correct_answer = question_detail['correct_answer']
    correct_answer = base64.b64decode(correct_answer).decode('ascii')
    print('True or False?')
    print(question)
    user_answer = input()
    if user_answer == correct_answer:
        print('Correct')
    else:
        print(f'Incorrect - the answer is {correct_answer}')
