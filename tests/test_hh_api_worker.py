import requests


# Определение родительского класса Parser для тестирования
class Parser:
    def __init__(self, file_worker):
        self.file_worker = file_worker


# Определение класса FileWorker для определение имени файла тестирования
class FileWorker:
    def __init__(self, filename):
        self.filename = filename


# Определение класса HeadHunterAPI
class HeadHunterAPI(Parser):
    """
    Класс для работы с API HeadHunter
    Класс Parser является родительским классом, который вам необходимо реализовать
    """

    def __init__(self, file_worker):
        self.url = "https://api.hh.ru/vacancies"
        self.headers = {"User-Agent": "HH-User-Agent"}
        self.params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params["text"] = keyword
        while self.params["page"] < 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            if response.status_code != 200:
                print(f"Ошибка при запросе: {response.status_code}")
                return []  # Возвращаем пустой список в случае ошибки

            vacancies = response.json().get("items", [])
            if not vacancies:
                break
            self.vacancies.extend(vacancies)
            self.params["page"] += 1
        return self.vacancies


# Тест для класса HeadHunterAPI
def test_head_hunter_api():
    # Создаем экземпляр FileWorker для тестирования
    file_worker = FileWorker("test_vacancies.json")

    # Создаем экземпляр HeadHunterAPI
    hh_api = HeadHunterAPI(file_worker)

    # Загружаем вакансии по ключевому слову
    keyword = "Python"
    vacancies = hh_api.load_vacancies(keyword)

    # Проверяем, что вакансии были загружены
    assert isinstance(vacancies, list), "Вакансии должны быть списком"
    assert len(vacancies) > 0, "Список вакансий не должен быть пустым"

    # Проверяем, что каждая вакансия имеет ожидаемые ключи
    for vacancy in vacancies:
        assert "name" in vacancy, "Вакансия должна содержать ключ 'name'"
        assert "alternate_url" in vacancy, "Вакансия должна содержать ключ 'alternate_url'"
        assert "salary" in vacancy, "Вакансия должна содержать ключ 'salary'"
        assert "snippet" in vacancy, "Вакансия должна содержать ключ 'snippet'"
        assert "id" in vacancy, "Вакансия должна содержать ключ 'id'"
