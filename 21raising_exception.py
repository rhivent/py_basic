'''
membuat raising custom exceptions
'''
class CoffeeTooHotException(Exception):
    def __init__(self,msg):
        # membuat message exception dari parameter class Exception
        super().__init__(msg)

class CoffeeTooColdException(Exception):
    def __init__(self,msg):
        # membuat message exception dari parameter class Exception
        super().__init__(msg)

class CoffeeCup:
    def __init__(self,temperature):
        self.__temperature = temperature

    def drink_coffee(self):
        if self.__temperature > 85:
            print('Coffee too hot')
            # bisa throw exception class ke sini
            # raise Exception('Coffee too hot')
            raise CoffeeTooHotException('Coffee temperature:' + str(self.__temperature))
        elif self.__temperature < 65:
            print('Coffee too cold')
            # raise Exception('Coffee too cold')
            raise CoffeeTooColdException('Coffee temperature:' + str(self.__temperature))
        else:
            print('Coffee ok to drink')

cup = CoffeeCup(100)
cup.drink_coffee()
