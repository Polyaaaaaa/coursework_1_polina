import json
import os

from src.file_worker import JSONSaver


# Определение класса Vacancy для тестирования
class TestVacancy:
    def __init__(self, name, link, salary, description, id):
        self.name = name
        self.link = link
        self.salary = salary
        self.description = description
        self.id = id


# Тест для класса JSONSaver
def test_json_saver():
    # Создаем временный файл для тестирования
    test_filename = "test_vacancies.json"

    # Создаем экземпляр JSONSaver
    json_saver = JSONSaver(test_filename)

    # Создаем тестовые данные вакансий
    vacancy1 = TestVacancy("Software Engineer", "http://example.com/1", "50000", "Develop software", 1)
    vacancy2 = TestVacancy("Data Scientist", "http://example.com/2", "60000", "Analyze data", 2)
    vacancy3 = TestVacancy("Product Manager", "http://example.com/3", "70000", "Manage products", 3)

    # Добавляем вакансии
    json_saver.add_vacancy(vacancy1)
    json_saver.add_vacancy(vacancy2)
    json_saver.add_vacancy(vacancy3)

    # Проверяем, что вакансии были добавлены
    with open(test_filename, "r", encoding="utf-8") as file:
        vacancies = json.load(file)
        assert len(vacancies) == 3
        assert vacancies[0]["name"] == "Software Engineer"
        assert vacancies[1]["name"] == "Data Scientist"
        assert vacancies[2]["name"] == "Product Manager"

    # Получаем вакансии по критериям
    criteria = {"salary": "60000"}
    result = json_saver.get_vacancies(criteria)
    assert len(result) == 1
    assert result[0]["name"] == "Data Scientist"

    # Удаляем вакансию
    json_saver.delete_vacancy(2)

    # Проверяем, что вакансия была удалена
    with open(test_filename, "r", encoding="utf-8") as file:
        vacancies = json.load(file)
        assert len(vacancies) == 2
        assert vacancies[0]["name"] == "Software Engineer"
        assert vacancies[1]["name"] == "Product Manager"

    # Удаляем временный файл после тестирования
    os.remove(test_filename)