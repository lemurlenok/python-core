#1
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __len__(self):
        return self.x + self.y

rect1 = Rectangle(5, 3)
rect2 = Rectangle(4, 7)


print(f"Сума площин: {rect1 + rect2}")
print(f"Різниця площин: {rect1 - rect2}")
print(f"Чи рівні площини? {rect1 == rect2}")
print(f"Чи нерівні площини? {rect1 != rect2}")
print(f"rect1 > rect2? {rect1 > rect2}")
print(f"rect1 < rect2? {rect1 < rect2}")
print(f"Сума сторін rect1: {len(rect1)}")
print(f"Сума сторін rect2: {len(rect2)}")

#2
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Cinderella(Human):
    __count = 0
    def __init__(self, name, age, foot_size):
        super().__init__(name, age)
        self.foot_size = foot_size
        Cinderella.__count += 1

    @classmethod
    def get_count(cls):
        print(f"Кількість створених Попелюшок: {cls.count}")


class Prince(Human):
    def __init__(self, name, age, found_shoe_size):
        super().__init__(name, age)
        self.found_shoe_size = found_shoe_size

    def find_cinderella(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.foot_size == self.found_shoe_size:
                print(f"Принц {self.name} знайшов свою Попелюшку: {cinderella.name} з розміром ноги {cinderella.foot_size}")
                return cinderella
        print("Попелюшку не знайдено!")
        return None


cinderella1 = Cinderella("Анна", 19, 36)
cinderella2 = Cinderella("Марія", 20, 37)
cinderella3 = Cinderella("Олена", 21, 38)


prince = Prince("Олександр", 25, 37)
prince.find_cinderella([cinderella1, cinderella2, cinderella3])
Cinderella.get_count()

#3
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Книга: {self.name}")

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Журнал: {self.name}")

class Main:
    printable_list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, Book) or isinstance(item, Magazine):
            cls.printable_list.append(item)
        else:
            print("Цей об'єкт не є ні книгою, ні журналом. Додавання ігнорується.")

    @classmethod
    def show_all_magazines(cls):
        print("Журнали:")
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        print("Книги:")
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 31)
Main.show_all_books()