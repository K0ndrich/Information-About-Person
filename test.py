from string import ascii_letters

class Person:
    
    S_RUS="йцукенгшщзхъфывапролджэячсмитьбю- "
    S_RUS_UPPER=S_RUS.upper()

    def __init__(self, fio, old, passport, weigth):
        
        self.verify(fio)

        self.__fio = fio.split()
        self.__old = old
        self.__passport = passport
        self.__weight = weigth
    
    @classmethod
    def verify(cls,fio):
        
        if type(fio)!=str:
            raise TypeError("ФИО должно быть строкой")
        
        f=fio.split()
        
        if len(f)!=3:
            raise TypeError("Неверный формат записи")
        
        letters=ascii_letters+cls.S_RUS+cls.S_RUS_UPPER
        
        for s in f:
            
            if len(s)<1:
                raise TypeError("в ФИО должен хотябы одни символ")
            
            if len(s.strip(letters))!=0:
                raise TypeError("в ФИО содержатся недопустмые символы")

a=Person('Кондратенко- Максим Олександрович',20,30,40)

