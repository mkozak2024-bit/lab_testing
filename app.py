
def count_symbols(text: str) -> int:
    return len(text)


def count_vowels(text: str) -> int:
    vowels = "аеєиіїоуюяАЕЄИІЇОУЮЯ"
    return sum(1 for letter in text if letter in vowels)


def divide(a, b):
    return a / b


class Figure:

    def __init__(self, figure_type, length):
        if length < 0:
            raise ValueError("Довжина не може бути від'ємною")

        self.figure_type = figure_type
        self.length = length

    def get_figure_type(self):
        return self.figure_type

    def get_figure_length(self):
        return self.length

    def get_angles(self):
        if self.figure_type == "квадрат":
            return 4
        elif self.figure_type == "прямокутник":
            return 4
        elif self.figure_type == "трикутник":
            return 3
        else:
            raise ValueError("Невідомий тип фігури")
