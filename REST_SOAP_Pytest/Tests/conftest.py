import csv

def pytest_generate_tests(metafunc):
    # Пропускаем функции, у которых нет аргументов
    if ("name" and "email" and "password" and "exp_res") not in metafunc.fixturenames:
        return
    # Загружаем элементы из файла
    with open('Data/payload.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter='|')
        test_cases = ()
        for row in reader:
            test_cases = test_cases + ((row["name"], row["email"], row["password"], int(row["exp_res"])), )
    if not reader:
        raise ValueError("Test cases not loaded")
    # Параметризуем функции с заданными параметрами
    metafunc.parametrize("name, email, password, exp_res", test_cases)
