import random
import string
def get_random_password(n:int=8) -> str:
    ...  # TODO написать функцию генерации случайных паролей
    alphabet = string.ascii_letters + string.digits
    password_chars = random.sample(alphabet, n)
    return ''.join(password_chars)
print(get_random_password())
