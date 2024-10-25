from src.vacancy_worker import Vacancies


def test_vacancies_class():
    # Тест на создание объекта Vacancies
    vacancy = Vacancies(name="Software Engineer", link="http://example.com", salary=50000, description="Develop software")
    assert vacancy.name == "Software Engineer"
    assert vacancy.link == "http://example.com"
    assert vacancy.salary == 50000
    assert vacancy.description == "Develop software"

    # Тест на валидацию зарплаты
    try:
        vacancy = Vacancies(name="Software Engineer", link="http://example.com", salary=-1000, description="Develop software")
    except ValueError as e:
        assert str(e) == "Зарплата не может быть отрицательной"

    try:
        vacancy = Vacancies(name="Software Engineer", link="http://example.com", salary="abc", description="Develop software")
    except ValueError as e:
        assert str(e) == "Зарплата должна быть числом"

    # Тест на преобразование списка вакансий в список объектов Vacancies
    vacancies_list = [
        {
            "name": "Data Scientist",
            "alternate_url": "http://example.com/data-scientist",
            "salary": {"from": 60000},
            "snippet": {"requirement": "Analyze data"},
            "id": "1"
        },
        {
            "name": "Product Manager",
            "alternate_url": "http://example.com/product-manager",
            "salary": {"from": 70000},
            "snippet": {"requirement": "Manage products"},
            "id": "2"
        }
    ]
    vacancies_objects = Vacancies.cast_to_object_list(vacancies_list)
    assert len(vacancies_objects) == 2
    assert vacancies_objects[0].name == "Data Scientist"
    assert vacancies_objects[0].salary == 60000
    assert vacancies_objects[1].name == "Product Manager"
    assert vacancies_objects[1].salary == 70000

    # Тест на сравнение объектов Vacancies
    vacancy1 = Vacancies(name="Software Engineer", link="http://example.com", salary=50000, description="Develop software")
    vacancy2 = Vacancies(name="Data Scientist", link="http://example.com/data-scientist", salary=60000, description="Analyze data")
    assert vacancy1 < vacancy2
    assert vacancy1 <= vacancy2
    assert vacancy1 != vacancy2
    assert vacancy2 > vacancy1
    assert vacancy2 >= vacancy1

    # Тест на представление объекта Vacancies
    assert repr(vacancy1) == "Vacancies(name=Software Engineer, link=http://example.com, salary=50000, description=Develop software)"

    print("Тест пройден успешно!")
