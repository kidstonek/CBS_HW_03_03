"""
Завдання 3

Використовуючи посилання наприкінці цього уроку, ознайомтеся з таким засобом інкапсуляції,
як властивості. Ознайомтеся з декоратором property у Python. Створіть клас, що описує температуру
 і дозволяє задавати та отримувати температуру за шкалою Цельсія та Фаренгейта, причому дані можуть
  бути задані в одній шкалі, а отримані в іншій.

"""

class Temperature:
    def __init__(self, temperature: float, type_of_temperature: str):
        self.temperature = temperature
        self.type_of_temperature = type_of_temperature

    @property
    def temp(self):
        return f'{self.temperature} Celsius degrees are equal {(self.temperature * (9 / 5)) + 32} Fahrenheit degrees' \
            if self.type_of_temperature in ['c', 'C', 'Celsius'] else (f'{self.temperature} Fahrenheit degrees is equal '
                                                          f'{(self.temperature-32)*(5/9)} of Celsius') \
            if self.type_of_temperature in ['f', 'F', 'Fahrenheit'] else 'wrong temp type'


if __name__ == '__main__':
    temper1 = Temperature(150.0, 'f')
    print(temper1.temp)