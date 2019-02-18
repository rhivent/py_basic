# logika ini mirip dengan col dan row
# cek di file 32pattern_heart.py

num = int(input("enter the number of rows:"))
for i in range(1,num+1):
    for j in range(1,num-i+1):
        print(end=" ")
    for j in range(i,0,-1): # i = 1 range is (1,0,-1) will give 1 so j value is 1
    # when i =2 or row = 2 range is (2,0,-1) it will give j = 2,1
        print(j,end="")
    for j in range(2,i+1): # i =1 so range is (2,1+1) so it won't execute
    # when i = 2 then range is (2,i+1) so , (2,2+1) so j = 2
    # i=3 range(2,3+1) so j = 2,3
        print(j,end="")
    print()
