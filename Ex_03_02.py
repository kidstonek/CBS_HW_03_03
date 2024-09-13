"""
Завдання 2

Створіть 2 класи мови, наприклад, англійська та іспанська. В обох класів має бути метод greeting().
Обидва створюють різні привітання. Створіть два відповідні об'єкти з двох класів вище та викличте дії цих
двох об'єктів в одній функції (функція hello_friend).

"""


class Language:
    def greeting(self):
        return


class English(Language):
    def greeting(self):
        return "Hello"


class Spanish(Language):
    def greeting(self):
        return "Ola"


def hello_friend(obj: Language):
    return obj.greeting()


if __name__ == '__main__':
    eng_greet = English()
    span_greet = Spanish()
    print(hello_friend(eng_greet))
    print(hello_friend(span_greet))
