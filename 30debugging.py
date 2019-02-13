import pdb
def add(x,y):
    sum = x + y
    return sum

# def main():
#     x = int(input("Num 1 : "))
#     y = int(input("Num 2 : "))
#     pdb.set_trace()
#     z = add(x,y)
#     print(z)

if __name__ == "__main__":
    # main()
    x = int(input("Num 1 : "))
    y = int(input("Num 2 : "))
    pdb.set_trace()
    # import pdb;pdb.set_trace()
    z = add(x,y)
    print(z)
