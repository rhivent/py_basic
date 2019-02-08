'''
composition adalah mewakili kata part-of dari kelas yg berhubungan

cek aggregation dengan mempassing object yg telah dibuat
salary = Salary(arg1,arg2)
emp = Employee('max',25,salary)

ke dlm parameter __init__(self,name,age,salary)

artinya aggregation itu represents Has a relationship
di dlm suatu associative kelas.
ini berarti unidirectional association

artinya mereka saling berkaitan tetapi jika salah satu
objek di hapus misal emp, maka salary tetap ada

sedangkan pada 17composition.py jika emp dihapus maka
salary juga itu terhapus.

jadi mereka objek terpisah tidak bersatu seperti komposisi
ini yg dinamakan aggregation.

jadi perbedaan antara mereka berdua:
=> composition:
1. sallary is part-of Employee
2. ketika delete Employee objek
maka sallary objek automatic will be deleted
sallary object is dependend on sallary class
3. sallary dan Employee saling bergantung
satu sama lain (inter-dependent)
=> aggregation:
1. Employee has a relationship with sallary
2. sallary objek dan Employee objek are independent
so they can survive jika salah satu di hapus
3. relationship is unidirectional
we can pass sallary obj ke Employee class
tetapi kita tdk bisa menge-pass Employee ke sallary objek
'''
class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return(self.pay*12) + self.bonus

class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        # create composition
        # mengintasiasi class Salary ke di dlm Employee
        # aritnya Employee class adalh container dr
        # Salary class, sedangkan Salary class adalh kontent
        self.obj_salary =salary;

    def total_salary(self):
        return self.obj_salary.annual_salary()

salary = Salary(15500,10000)
emp = Employee('max',25,salary)
print(emp.total_salary())
