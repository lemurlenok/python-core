with open('emails.txt', 'r') as file:
    emails = file.readlines()

gmail_emails = [email.strip() for email in emails if email.strip().endswith('@gmail.com')]

with open('filtered_emails.txt', 'w') as output_file:
    for email in gmail_emails:
        output_file.write(email + '\n')

print(f"Знайдено {len(gmail_emails)} емейлів з доменом gmail.com")

import json

FILE_PATH = 'purchases.json'

# Завантаження покупки з файлу
def load_purchases():
    try:
        with open(FILE_PATH, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Зберігання покупки у файл
def save_purchases(purchases):
    with open(FILE_PATH, 'w') as file:
        json.dump(purchases, file, indent=4)

# Додавання новї покупки
def add_purchase():
    purchases = load_purchases()
    id_ = input("Введіть ID покупки: ")
    name = input("Введіть назву покупки: ")
    price = float(input("Введіть ціну покупки: "))
    purchases.append({"id": id_, "name": name, "price": price})
    save_purchases(purchases)
    print("Покупку успішно додано!")

# Вивід всих покупок
def show_all_purchases():
    purchases = load_purchases()
    if not purchases:
        print("Немає жодної покупки.")
    else:
        for purchase in purchases:
            print(f"ID: {purchase['id']}, Назва: {purchase['name']}, Ціна: {purchase['price']}")

# Пошук покупки за полем
def search_purchase():
    purchases = load_purchases()
    field = input("За яким полем шукати (id, name, price): ")
    value = input("Введіть значення для пошуку: ")

    for purchase in purchases:
        if str(purchase.get(field, '')).lower() == value.lower():
            print(f"Знайдено: ID: {purchase['id']}, Назва: {purchase['name']}, Ціна: {purchase['price']}")
            return

    print("Покупка не знайдена.")

# Вивід найдорожчої покупки
def show_most_expensive():
    purchases = load_purchases()
    if not purchases:
        print("Немає жодної покупки.")
    else:
        most_expensive = max(purchases, key=lambda x: x['price'])
        print(f"Найдорожча покупка: ID: {most_expensive['id']}, Назва: {most_expensive['name']}, Ціна: {most_expensive['price']}")

# Видалення покупки за ID
def delete_purchase():
    purchases = load_purchases()
    id_ = input("Введіть ID покупки для видалення: ")
    updated_purchases = [purchase for purchase in purchases if purchase['id'] != id_]

    if len(purchases) == len(updated_purchases):
        print("Покупка з таким ID не знайдена.")
    else:
        save_purchases(updated_purchases)
        print("Покупку успішно видалено!")

# Меню
def menu():
    while True:
        print("\nМеню:")
        print("1. Додати покупку")
        print("2. Показати всі покупки")
        print("3. Шукати покупку")
        print("4. Показати найдорожчу покупку")
        print("5. Видалити покупку")
        print("6. Вийти")

        choice = input("Виберіть опцію: ")

        if choice == '1':
            add_purchase()
        elif choice == '2':
            show_all_purchases()
        elif choice == '3':
            search_purchase()
        elif choice == '4':
            show_most_expensive()
        elif choice == '5':
            delete_purchase()
        elif choice == '6':
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")


if __name__ == '__main__':
    menu()
