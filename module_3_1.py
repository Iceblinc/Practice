calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    length = len(string)
    upper = string.upper()
    lower = string.lower()
    return length, upper, lower


def is_contains(string, lits_to_search):
    count_calls()
    lower_calls = string.lower()
    lower_list = [item.lower() for item in lits_to_search]
    return lower_calls in lower_list


print(string_info("Time"))  # Количество символов в слове также выводит слово в верхний и нижний регистр
print(string_info("Time interval"))
print(is_contains("hello", ["hello", "world"]))  # Проверяет есть ли слово в листе
print(is_contains("python", ['hello', 'world']))
print(string_info("Как дела"))


print(calls) # Общие количество операцый
