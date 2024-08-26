# sum series
def recurgcd(a,b):
    lo = min(a,b)
    hi = max(a,b)
    if lo == 0:
        return hi
    elif lo == 1:
        return 1
    else:
        return recurgcd(lo,hi%lo)
print(recurgcd(14,12))
print(recurgcd(1,3))