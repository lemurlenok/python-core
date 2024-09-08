#- є функція:
#def pr():
#    return 'Hello_boss_!!!'
# написати декоратор до цієї функції, який замінює нижні підчеркування на пробіли і повертає це значення
#функцию pr менять не можно

def replace_underscores(func):
    def wrapper():
        result = func()
        return result.replace('_', ' ')
    return wrapper

@replace_underscores
def pr():
    return 'Hello_boss_!!!'

print(pr())

#вивести послідовність Фібоначі, кількість вказана в знінній,
# наприклад: x = 10 -> 1 1 2 3 5 8 13 21 34 55
#(число з послідовності - це сума попередніх двох чисел)

#порахувати кількість парних і непарних цифр числа,
#наприклад: х = 225688 -> п = 5, н = 1;
#         х = 33294 -> п = 2, н = 3

def fibonacci_sequence(n):
    sequence = []
    a, b = 1, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def count_even_odd_digits(num):
    even_count = 0
    odd_count = 0
    for digit in str(num):
        if int(digit) % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

x = 17
fibonacci_seq = fibonacci_sequence(x)
print(f'Послідовність Фібоначчі ({x} чисел): {fibonacci_seq}')

for number in fibonacci_seq:
    even_count, odd_count = count_even_odd_digits(number)
    print(f'Число: {number}, парні: {even_count}, непарні: {odd_count}')

#прога, що виводить кількість кожного символа з введеної строки, наприклад: st = 'as 23 fdfdg544'  # введена строка
#'a' -> 1  # вивело в консолі
#'s' -> 1
#' ' -> 2
#'2' -> 1
#'3' -> 1
#'f' -> 2
#'d' -> 2
#'g' -> 1
#'5' -> 1
#'4' -> 2


def count_characters(st):
    char_count = {}
    for char in st:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    for char, count in char_count.items():
        print(f"'{char}' -> {count}")

st = 'Gjmik 596746 ds 4689'
count_characters(st)

#створити декоратор який буде рахувати кількість запущених функцій продекорованих цим декоратором

def make_decorator():
    call_count = {'count': 0}

    def decorator(func):
        def wrapper(*args, **kwargs):
            call_count['count'] += 1
            print(f"Функція '{func.__name__}' викликана {call_count['count']} раз(и).")
            return func(*args, **kwargs)
        return wrapper

    return decorator

decor = make_decorator()

@decor
def func1():
    print("Hello!")

@decor
def func2():
    print("Hi!")


func1()
func1()
func1()
func2()
func1()
func2()
func1()
func2()
func2()
func1()