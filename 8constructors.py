'''
mendefinisikan multiple constructor
__init__ method yg di pakai yaitu yg terakhir
sedngkan yg seblumnya akan di overwrite (ditimpa)
'''

class Hello:
    def __init__(self): pass
    def __init__(self,name): pass
    # memberikan multi parameter
    def __init__(self,*args,**kwargs): pass

halo = Hello()
halo1 = Hello('name','ah','sss',name='wmkamdak')


class Nice:
    def __init__(self,name):
        self.name = name
        # bisa menginisiai static value utk atribut,
        # tanpa harus passing sebagai argumen
        self.age = 10

nice = Nice('name')
