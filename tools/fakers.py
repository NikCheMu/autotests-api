from faker import Faker

class Fake:
    """
    Класс для генерации случайных тестовых данных с использованием библиотеки Faker
    """

    def __init__(self, faker: Faker) -> None:
        self.faker = faker

    def text(self) -> str:
        """
        Метод для получения случайного текста
        :return: Случайный текст
        """
        return self.faker.text()

    def uuid4(self) -> str:
        """
        Метод для получения случайного uuid4
        :return: случайный uuid4
        """
        return self.faker.uuid4()

    def email(self, domain: str | None = None) -> str:
        """
        Генерирует случайный email.

        :param domain: Домен электронной почты (например, "example.com").
        Если не указан, будет использован случайный домен.
        :return: Случайный email.
        """
        return self.faker.email(domain=domain)

    def sentence(self) -> str:
        """
        Метод для получения случайного предложения
        :return: случайное предложение
        """
        return self.faker.sentence()

    def password(self) -> str:
        """
        Метод для получения случайного пароля
        :return: Случайный пароль
        """
        return self.faker.password()

    def last_name(self) -> str:
        """
        Метод для получения случайной фамилии
        :return: Случайная фамилия
        """
        return self.faker.last_name()

    def first_name(self) -> str:
        """
        Метод для получения случайного имени
        :return: Случайное имя
        """
        return self.faker.first_name()

    def middle_name(self) -> str:
        """
        Метод для получения случайного отчества
        :return: Случайное отчество
        """
        return self.faker.first_name()

    def estimated_time(self) -> str:
        """
        Метод для получения случайной строки планируемого времени в формате "2 weeks"
        :return: строка планируемого времени в формате "2 weeks"
        """
        return f"{self.integer(start=1,end=10)} weeks"

    def integer(self, start: int = 1, end: int = 100) -> int:
        """
        Метод для получения случайного числа в диапазоне от 1 до 100
        :param start: Начало диапазона (включ)
        :param end: Конец диапазона (Включ)
        :return: случайное число
        """
        return self.faker.random_int(min=start, max=end)

    def max_score(self) -> int:
        """
        Метод для получения случайного значения максимального балла (от 50 до 100)
        :return: случайное значение максимального балла
        """
        return self.integer(start=50, end=100)

    def min_score(self) -> int:
        """
        Метод для получения случайного значения минимального балла (от 1 до 30)
        :return: случайное значение минимального балла
        """
        return self.integer(start=1, end=30)


fake = Fake(faker=Faker())