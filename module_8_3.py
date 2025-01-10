"""Создаем 3 класса (2 из которых будут исключениями):"""

"""
Класс Car должен обладать следующими свойствами:

1. Атрибут объекта model - название автомобиля (строка).
2. Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
3. Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность. Возвращает True,
если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
4. Атрибут __numbers - номера автомобиля (строка).
5. Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность. Возвращает True,
если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
6. Классы исключений IncorrectVinNumber и IncorrectCarNumbers, объекты которых обладают атрибутом message - сообщение,
которое будет выводиться при выбрасывании исключения.
"""


class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        self.__vin = vin
        self.__numbers = numbers
        self.__is_valid_vin()
        self.__is_valid_numbers()

    """
    Работа метода __is_valid_vin
    1. Выбрасывает исключение IncorrectVinNumber с сообщением 'Некорректный тип vin номер', если передано не целое
    число. (тип данных можно проверить функцией isinstance).
    2. Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера', если переданное число
    находится не в диапазоне от 1000000 до 9999999 включительно.
    3. Возвращает True, если исключения не были выброшены.
    """
    def __is_valid_vin(self):
        if not isinstance(self.__vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номер')
        if not 1000000 <= self.__vin <= 9999999:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    """
    Работа метода __is_valid_numbers
    1. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Некорректный тип данных для номеров', если передана
    не строка. (тип данных можно проверить функцией isinstance).
    2. Выбрасывает исключение IncorrectCarNumbers с сообщением 'Неверная длина номера', переданная строка должна
    состоять ровно из 6 символов.
    3. Возвращает True, если исключения не были выброшены.
    """
    def __is_valid_numbers(self):
        if not isinstance(self.__numbers, str):
            raise IncorrectCarNumbers('Неверный тип данных для номеров')
        if len(self.__numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        return True


class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message


"""
Пример результата выполнения программы:
Пример выполняемого кода:
Вывод на консоль:
"""

"""Первый блок исключения"""
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

"""Второй блок исключения"""
try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

"""Третий блок исключения"""
try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')