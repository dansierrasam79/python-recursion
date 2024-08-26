# sum series
def geoseries(n):
    if n == 0:
        return n
    else:
        return 1/pow(2,n) + geoseries(n-1)
print(geoseries(14))
print(geoseries(1))