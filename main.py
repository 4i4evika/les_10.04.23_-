### Зад.1. Реализуйте класс «Автомобиль». Необходимо хранить в полях класса: название модели,
# год выпуска, производителя, объем двигателя, цвет машины, цену. Реализуйте методы класса
# для ввода данных, вывода данных, реализуйте доступ к отдельным полям через методы класса.

# class Auto:
#     def __init__(self, model, year, manufacturer, engine, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.engine = engine
#         self.color = color
#         self.price = price
#
#     def reset(self):
#         self.model = input('Введите модель автомобиля: ')
#         self.year = input('Введите год выпуска: ')
#         self.manufacturer = input('Введите производителя: ')
#         self.engine = input('Введите объем двигателя: ')
#         self.color = input('Введите цвет: ')
#         self.price = input('Введите цену автомобиля: ')
#
#     def print_info(self):
#         print(f'Модель автомобиля: {self.model}')
#         print(f'Год выпуска: {self.year}')
#         print(f'Страна-производитель: {self.manufacturer}')
#         print(f'Объем двигателя: {self.engine}')
#         print(f'Цвет автомобиля: {self.color}')
#         print(f'Цена автомобиля: {self.price}')
#
# new_auto = Auto('KIA', '2022', 'Корея', '1.6', 'зеленый', '1 890 000')
# new_auto.print_info()
# print('---------------')
# new_auto.reset()
# print('---------------')
# new_auto.print_info()



### Зад.2. Реализуйте класс «Книга». Необходимо хранить в полях класса: название книги, год выпуска, издателя,
# жанр, автора, цену. Реализуйте методы класса для ввода данных, вывода данных, реализуйте доступ к отдельным
# полям через методы класса.

# class Book:
#     def __init__(self, name, year, publisher, genre, author, price):
#         self.name = name
#         self.year = year
#         self.publisher = publisher
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def reset(self):
#         self.name = input('Введите название книги: ')
#         self.year = input('Введите год выпуска: ')
#         self.publisherer = input('Введите издателя: ')
#         self.genre = input('Введите жанр: ')
#         self.author = input('Введите автора: ')
#         self.price = input('Введите цену книги: ')
#
#     def print_info(self):
#         print(f'Название книги: {self.name}')
#         print(f'Год выпуска: {self.year}')
#         print(f'Издатель: {self.publisher}')
#         print(f'Жанр: {self.genre}')
#         print(f'Автор: {self.author}')
#         print(f'Цена книги: {self.price}')
#
# new_book = Book('Сказка о рыбаке и рыбке', '1833', 'журнал', 'сказка', 'А.С.Пушкин', '1000')
# new_book.print_info()
# print('------------------')
# new_book.reset()
# print('------------------')
# new_book.print_info()



### Зад.3. Реализуйте класс «Стадион». Необходимо хранить в полях класса: название стадиона, дату открытия,
# страну, город, вместимость. Реализуйте методы класса для ввода данных, вывода данных,
# реализуйте доступ к отдельным полям через методы класса.

# class Stadium:
#     def __init__(self, name, year, country, city, capacity):
#         self.name = name
#         self.year = year
#         self.country = country
#         self.city = city
#         self.capacity = capacity
#
#     def reset(self):
#         self.name = input('Введите название стадиона: ')
#         self.year = input('Введите дату открытия: ')
#         self.country = input('Введите страну: ')
#         self.city = input('Введите город: ')
#         self.capacity = input('Введите вместимость: ')
#
#     def print_info(self):
#         print(f'Название стадиона: {self.name}')
#         print(f'Дата открытия: {self.year}')
#         print(f'Страна: {self.country}')
#         print(f'Город: {self.city}')
#         print(f'Вместимость: {self.capacity}')
#
# new_stadium = Stadium('Динамо', '1928', 'Россия', 'Москва', '70 000')
# new_stadium.print_info()
# print('------------------')
# new_stadium.reset()
# print('------------------')
# new_stadium.print_info()