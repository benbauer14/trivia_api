import requests

trivia = requests.get("https://opentdb.com/api.php?amount=10&type=boolean")

question_data = trivia.json()["results"]