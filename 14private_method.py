# class Hello:
#     def __init__(self,name):
#         self.a = 10
#         self._b = 20
#         self.__c = 30
#     def public_method(self):
#         print(self.a)
#         print(self.__c)
#         print('public')
#
# halo = Hello('name')
# print(halo.a)
# print(halo._b)
#
# halo.public_method()

# membuat private method
class Hello:
    def __init__(self,name):
        self.a = 10
        self._b = 20
        self.__c = 30
    def public_method(self):
        print(self.a)
        print(self.__c)
        print('public')
        self.__private_method()
        
    def __private_method(self):
        print('private')

halo = Hello('name')
print(halo.a)
print(halo._b)

halo.public_method()

# akses private method diluar class
halo.__private_method()
# maka error no attribut __private_method()
# diluar class maka tidak bisa mengakases fungsi

# cara menggunakan private method maka menggunakan self
