from string import ascii_letters


class Person:

    S_RUS = "йцукенгшщзхъфывапролджэячсмитьбю- "
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio, old, passport, weigth):

        self.verify(fio)
        self.verify_old(old)
        self.verify_passport(passport)
        self.verify_weight(weigth)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = passport
        self.__weight = weigth

    @classmethod
    def verify(cls, fio):

        if type(fio) != str:
            raise TypeError("ФИО должно быть строкой")

        f = fio.split()

        if len(f) != 3:
            raise TypeError("Неверный формат записи")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER

        for s in f:

            if len(s) < 1:
                raise TypeError("в ФИО должен хотябы одни символ")

            if len(s.strip(letters)) != 0:
                raise TypeError("в ФИО содержатся недопустмые символы")

    @classmethod
    def verify_old(cls, old):
        if type(old) != int or old < 14 or old > 120:
            raise TypeError("Возраст должен быть целым числом от 14 до 120 ")

    @classmethod
    def verify_weight(cls, weigth):
        if type(weigth) != float or weigth < 20:
            raise TypeError("Вес должен быть вещественым числом от 20 и више ")

    @classmethod
    def verify_passport(cls, passport):
        if type(passport) != str:
            raise TypeError("Паспорт должен быть строкой")

        s = passport.split()
        if len(s) != 2 or len(s[0]) != 4 or len(s[1]) != 6:
            raise TypeError("Неверный формат паспорта")

        for p in s:
            if not p.isdigit():
                raise TypeError("Серия и Номер паспорта должны быть числами")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, passport):
        self.verify_passport(passport)
        self.__passport = passport


a = Person("Шевченко Иван Олександрович", 25, "3333 777777", 50.5)
