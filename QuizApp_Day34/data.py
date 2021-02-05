import requests
from question_model import Question
from quiz_brain import QuizBrain

def api_call(cat_no):
    parameters = {
        "amount": 10,
        "type": "boolean",
        # "category": cat_no
    }
    response = requests.get("https://opentdb.com/api.php", params=parameters)
    response.raise_for_status()
    return response


cat_id = 0

def get_category(category):
    global cat_id
    for index in range(len(category_list)):
        if category_list[index]['name'] == category:
            cat_id = category_list[index]['id']


print(f"Your category id{cat_id}")

category_data = requests.get("https://opentdb.com/api_category.php")
category_list = category_data.json()['trivia_categories']
list_names = []
for i in range(len(category_list)):
    list_names.append(category_list[i]['name'])

print(category_list)



question_data = api_call(9).json()["results"]

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)