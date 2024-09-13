"""Завдання 1

Створіть клас, який описує автомобіль. Які атрибути та методи мають бути повністю інкапсульовані?
Доступ до таких атрибутів та зміну даних реалізуйте через спеціальні методи (get, set)."""


class Auto:
    def __init__(self, model: str, brand: str):
        self.__model = model
        self.__brand = brand

    def set_model(self, new_model: str):
        self.__model = new_model

    def set_brand(self, new_brand: str):
        if new_brand.isalpha():
            self.__brand = new_brand

    def get_model(self):
        return self.__model

    def get_brand(self):
        return self.__brand


if __name__ == '__main__':
    auto1 = Auto('F50', 'Ferrari')
    print(auto1.get_brand())

    auto1.set_brand('Porshe')
    print(auto1.get_brand())