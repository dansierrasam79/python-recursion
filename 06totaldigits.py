# sum digits
def totaldigits(n):
    if n == 0:
        return n
    else:
        return n % 10 + totaldigits(int(n/10))
print(totaldigits(145))
print(totaldigits(0))