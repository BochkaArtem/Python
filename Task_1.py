# TODO Написать 3 класса с документацией и аннотацией типов
#ПРОВЕРЬТЕ ПОЖАЛУЙСТА 4 ЛАБОРАТОРНУЮ РАБОТУ /pull5
class MaterialEntity:
    def __init__(self, mass_kg: float, age_years: int):
        """
        Инициализация материальной сущности.

        :param mass_kg: Масса объекта в килограммах. Должна быть > 0.
        :param age_years: Возраст объекта в годах. Должен быть >= 0.
        """
        if mass_kg <= 0:
            raise ValueError("Масса должна быть положительным числом.")
        if age_years < 0:
            raise ValueError("Возраст не может быть отрицательным.")

        self.mass_kg = mass_kg
        self.age_years = age_years

    def move(self, distance_m: float) -> bool:
        """
        Описывает перемещение объекта в пространстве.

        :param distance_m: Расстояние перемещения в метрах.
        :return: True, если перемещение успешно, иначе False.

        >>> entity = MaterialEntity(10.5, 2)
        >>> entity.move(5.0)
        True
        >>> entity.move(-1.0)
        Traceback (most recent call last):
            ...
        ValueError: Расстояние перемещения не может быть отрицательным.
        """
        if distance_m < 0:
            raise ValueError("Расстояние перемещения не может быть отрицательным.")
        ...

    def get_density(self, volume_m3: float) -> float:
        """
        Вычисляет плотность объекта на основе переданного объема.

        :param volume_m3: Объем объекта в м3. Должен быть > 0.
        :return: Плотность объекта (кг/м3).

        >>> entity = MaterialEntity(100.0, 10)
        >>> entity.get_density(2.0)
        50.0
        """
        if volume_m3 <= 0:
            raise ValueError("Объем должен быть больше нуля.")
        ...


class DataContainer:
    def __init__(self, capacity: int, name: str):
        """
        Инициализация контейнера данных.

        :param capacity: Максимальное количество элементов. Должно быть > 0.
        :param name: Название структуры. Не должно быть пустой строкой.
        """
        if capacity <= 0:
            raise ValueError("Вместимость должна быть больше нуля.")
        if not name.strip():
            raise ValueError("Название не может быть пустым.")

        self.capacity = capacity
        self.name = name

    def add_item(self, item_id: int) -> str:
        """
        Добавляет идентификатор элемента в структуру.

        :param item_id: Числовой идентификатор. Должен быть положительным.
        :return: Строковое подтверждение добавления.

        >>> container = DataContainer(100, "MainStack")
        >>> container.add_item(505)
        '505'
        """
        if item_id < 0:
            raise ValueError("ID элемента должен быть положительным.")
        ...

    def is_empty(self) -> bool:
        """
        Проверяет, пуста ли структура.

        :return: True, если пуста, False в противном случае.

        >>> container = DataContainer(10, "Buffer")
        >>> container.is_empty()
        True
        """
        ...


class InfoService:
    def __init__(self, user_count: int, rating: float):
        """
        Инициализация информационного сервиса.

        :param user_count: Количество пользователей. Не может быть отрицательным.
        :param rating: Рейтинг сервиса от 0.0 до 5.0.
        """
        if user_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным.")
        if not (0.0 <= rating <= 5.0):
            raise ValueError("Рейтинг должен быть в диапазоне от 0.0 до 5.0.")

        self.user_count = user_count
        self.rating = rating

    def update_rating(self, new_score: float) -> float:
        """
        Обновляет рейтинг сервиса.

        :param new_score: Новая оценка. Должна быть от 0.0 до 5.0.
        :return: Новый средний рейтинг.

        >>> service = InfoService(1000, 4.5)
        >>> service.update_rating(5.0)
        4.75
        """
        if not (0.0 <= new_score <= 5.0):
            raise ValueError("Оценка должна быть в пределах от 0 до 5.")
        ...

    def send_notification(self, message: str) -> int:
        """
        Рассылает уведомление пользователям.

        :param message: Текст сообщения. Длина не должна превышать 255 символов.
        :return: Количество успешно отправленных уведомлений.

        >>> service = InfoService(500, 4.0)
        >>> service.send_notification("Hello World")
        'Hello World'
        """
        if len(message) > 255:
            raise ValueError("Сообщение слишком длинное.")
        ...


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
