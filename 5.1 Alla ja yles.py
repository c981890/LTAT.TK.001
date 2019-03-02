def alla_ules(n):
    if n <= 0:
        print("Põhi!")
    else:
        if n % 2 == 0:
            print(n)
        elif n % 2 != 0:
            print(n)
        alla_ules(n - 2)
        if n % 2 == 0:
            print(n-1)
        elif n % 2 != 0:
            print(n-1)
