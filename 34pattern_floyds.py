'''
1
2 3
4 5 6
7 8 9 10

segitiga yg number berurutan, atau floyds triangle by robert floyds
'''
# inisiasi variabel
n = int(input("enter the number of row:"))

# nested for() loop
# there are 4 cols and 4 rows
# inisiasi
num = 1
for row in range(1,n+1):
    for col in range(1,row+1):
        print(num,end=" ")
        num+=1
    print() # untuk enter di next line
