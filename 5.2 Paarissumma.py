def paarissumma(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        return n + paarissumma(n-1)
    elif n % 2 == 1:
        return paarissumma(n-1)
