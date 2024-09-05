# написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому
st = 'lnbtgu 5 vf942 54'
digits = [char for char in st if char.isdigit()]
print(','.join(digits))

# написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
st = 'df 565 bdsbd4 48'
numbers = ''.join(char if char.isdigit() else ' ' for char in st).split()
print(', '.join(numbers))

#є строка:greeting = 'Hello, world'
#записати кожний символ як окремий елемент списку і зробити його заглавним:
greeting = 'Hello, world'
upper_case_list = [char.upper() for char in greeting]
print(upper_case_list)

#з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
odd_squares = [x**2 for x in range(0, 50) if x == 0 or x % 2]
print(odd_squares)

#Функція, яка виводить ліст
def print_list(lst):
    print(lst)
print_list([1, 2, 3, 4, 5])

#Функція, яка приймає три числа та виводить і повертає найбільше
def max_of_three(a, b, c):
    max_value = max(a, b, c)
    print(max_value)
    return max_value
result = max_of_three(3, 7, 5)

#Функція, яка приймає будь-яку кількість чисел, повертає найменше, а виводить найбільше
def min_max(*args):
    min_value = min(args)
    max_value = max(args)
    print(max_value)
    return min_value
result = min_max(3, 7, 1, 9, 2)

#Функція, яка повертає найбільше число з ліста
def max_from_list(lst):
    return max(lst)
result = max_from_list([3, 7, 1, 9, 2])

# Функція, яка повертає найменше число з ліста
def min_from_list(lst):
    return min(lst)
result = min_from_list([3, 7, 1, 9, 2])

#Функція, яка приймає ліст чисел та складає значення елементів ліста та повертає його
def sum_of_list(lst):
    return sum(lst)
result = sum_of_list([3, 7, 1, 9, 2])

#Функція, яка приймає ліст чисел та повертає середнє арифметичне його значень
def average_of_list(lst):
    return sum(lst) / len(lst)

lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# Мінімальне число
min_value = min(lst)
print("Мінімальне число:", min_value)

# Видалити дублікати
lst = list(dict.fromkeys(lst))
print("Список без дублікатів:", lst)

# Замінити кожне 4-те значення на 'X'
lst = ['X' if (i + 1) % 4 == 0 else val for i, val in enumerate(lst)]
print("Список після заміни кожного 4-го елемента:", lst)

def print_square(size):
    for i in range(size):
        if i == 0 or i == size - 1:
            print('*' * size)
        else:
            print('*' + ' ' * (size - 2) + '*')

def multiplication_table():
    i = 1
    while i <= 10:
        j = 1
        while j <= 10:
            print(f'{i * j:4}', end='')
            j += 1
        print()
        i += 1

def menu():
    while True:
        print("1. Показати мінімальне число в списку")
        print("2. Видалити дублікати")
        print("3. Замінити кожне 4-те значення на 'X'")
        print("4. Вивести пустий квадрат з '*', сторона якого задана")
        print("5. Показати табличку множення")
        print("6. Вийти")

        choice = input("Виберіть дію: ")

        if choice == '1':
            lst = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
            print("Мінімальне число:", min(lst))
        elif choice == '2':
            lst = list(dict.fromkeys(lst))
            print("Список без дублікатів:", lst)
        elif choice == '3':
            lst = ['X' if (i + 1) % 4 == 0 else val for i, val in enumerate(lst)]
            print("Список після заміни кожного 4-го елемента:", lst)
        elif choice == '4':
            size = int(input("Введіть розмір сторони квадрата: "))
            print_square(size)
        elif choice == '5':
            multiplication_table()
        elif choice == '6':
            break
        else:
            print("Неправильний вибір. Спробуйте ще раз.")

menu()

