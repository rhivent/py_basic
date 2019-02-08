class Salary:
    def __init__(self,pay,bonus):
        self.pay=pay
        self.bonus=bonus

    def annual_salary(self):
        return(self.pay*12) + self.bonus

class Employee:
    def __init__(self,name,age,pay,bonus):
        self.name = name
        self.age = age
        # create composition
        # mengintasiasi class Salary ke di dlm Employee
        # aritnya Employee class adalh container dr
        # Salary class, sedangkan Salary class adalh kontent
        self.obj_salary = Salary(pay,bonus)

    def total_salary(self):
        return self.obj_salary.annual_salary()

emp = Employee('max',25,15500,10000)
print(emp.total_salary())
'''
# tidak bisa mengheritance a/ Salary dan Employee
# tetapi ada hubungan antar class saat Employee dan
# Salary saat perhitungan artinya gaji(Salary) adalah
# penghasilan dari karyawan
# konsep composition adalah mendelegasikan tanggungjawab dari
satu class ke kelas lain
caranya yaitu :
membuat 1 variabel pada method class itu
cek kode ini
...
self.obj_salary = Salary(pay,bonus)
...

saat print eksekssi di bawah kita tidak harus
mengintasiasi Salary class, hal ini yg membuat keren
hanya mengintasiasi Salary di dlm Employee class

intinya ketika kita mengintasiasi 1 klass di dlm method suatu class
artinya komposisi

contoh lain yaitu Book and Chapter
Book is not a chapter and chapter is not a book
tpi kita bisa delegasikan dari kelas Chapter ke dlm kelas Book
'''
