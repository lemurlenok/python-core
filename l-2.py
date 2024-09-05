#написати функцію на замикання котра буде в собі зберігати список справ, вам потрібно реалізувати два методи:
#- перший записує в список нову справу
#- другий повертає всі записи

def netbook():
    todo_list = []

    def add_task(task):
        todo_list.append(task)

    def get_all_tasks():
        return todo_list

    return add_task, get_all_tasks

add_task, get_all_tasks = netbook()

add_task("Порахувати всі мурахи у дворі")
add_task("Навчити кота користуватися Google")
add_task("Пошукати скарб у дивані")
add_task("Запустити бавовну")
add_task("Скласти пил за абеткою")

tasks = get_all_tasks()


print("Список справ:")
for idx, task in enumerate(tasks, start=1):
    print(f"{idx}. {task}")

# протипізувати перше завдання
from typing import List, Callable

def netbook() -> tuple[Callable[[str], None], Callable[[], List[str]]]:
    todo_list: List[str] = []

    def add_task(task: str) -> None:
        todo_list.append(task)

    def get_all_tasks() -> List[str]:
        return todo_list

    return add_task, get_all_tasks

add_todo, get_all_tasks = netbook()

add_todo("Порахувати всі мурахи у дворі")
add_todo("Навчити кота користуватися Google")
add_todo("Пошукати скарб у дивані")
add_todo("Запустити бавовну")
add_todo("Скласти пил за абеткою")

print(get_all_tasks())

# створити функцію котра буде повертати сумму розрядів числа у вигляді строки (також використовуемо типізацію)
#Приклад:
# expanded_form(12) # return '10 + 2'
# expanded_form(42) # return '40 + 2'
# expanded_form(70304) # return '70000 + 300 + 4'

def expanded_form(num: int) -> str:
    digits = list(str(num))
    expanded = [
        str(int(digit) * 10**i)
        for i, digit in enumerate(reversed(digits)) if digit != '0'
    ]
    return ' + '.join(expanded)

print(expanded_form(189))
print(expanded_form(5649))
print(expanded_form(8797195))

#створити декоратор котрий буде підраховувати скільки разів була запущена функція продекорована
# цим декоратором, та буде виводити це значення після виконання функцій

def decor(func):
    count = 0

    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"Функція '{func.__name__}' була викликана {count} раз(и).")
        result = func(*args, **kwargs)
        print("--------------------")
        return result

    return wrapper

@decor
def func1():
    print('func1')

@decor
def func2():
    print('func2')

func1()
func1()
func2()
func2()
func1()
