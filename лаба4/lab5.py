# TODO написать функцию, которая выдает трехзначное число
import random
def get_three_digit_number() -> int:
    digit1 = random.randint(0, 9)
    digit2 = random.randint(0, 9)
    digit3 = random.randint(0, 9)

    return digit1 * 100 + digit2 * 10 + digit3

print(get_three_digit_number())
