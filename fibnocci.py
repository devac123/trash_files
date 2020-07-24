n = int(input("enter that which you want to find fibnocci : "))
def fibnoci(var):
    a = 0
    b = 1
    if n == 1 or n==2:
        return 1
    else:
        for i in range(n):
            c = a + b
            a = b
            b = c
            print(b , end=",")
fibnoci(n)
