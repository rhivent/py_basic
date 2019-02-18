'''
0,1,1,2,3,5,8  ==> angka ketiga adalah angka penambhan
dari dua angka sebelumnya, dmikian angka ke-4,
penambhan angka 2 dan 3
'''

n = int(input("enter how many numbers you want in this series:"))

first = 0
second = 1

for i in range(n):
    print(first,",",end="")
    temp = first
    first = second
    second = temp + second
print()
