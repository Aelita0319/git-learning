def find_narcissistic_number(start: int, end: int):
    lst = []
    for i in range(start, end):
        exp = len(str(i))
        tmp = i
        sums = 0
        for j in range(exp):
            sums += (tmp % 10) ** exp
            tmp //= 10
        if sums == i:
            lst.append(i)
    return lst
