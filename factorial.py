def hehe(k):
    """
        :param n: Integer
        :return: n * n-1 * n-2 * n-3.......1
    """
    fac = 1
    for i in range(k):
        fac= fac * (i+1)
    return fac

num=int(input("Enter the number"))
print(hehe(num))