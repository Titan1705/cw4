import requests
import json
from src.classes.abstract.API_absctract import AbsctractAPI


class HeadHunterAPI(AbsctractAPI):
    """Создаём класс для работы с hh.ru
    С помощью него мы будем подгружать сырой список вакасний
    с api.hh.ru/vacancies, для дальнейшей обработки через класс Vacancy"""

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}

    def load_vacancies(self, keyword, page=0, per_page=20) -> list:
        """Получаем список вакансий """
        response = requests.get(self.__url,
                                params={'text': keyword, 'page': page, 'per_page': per_page},
                                headers=self.headers)
        response_json = response.json()['items']

        return response_json
