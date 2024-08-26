# sum series
def totalseries(n):
    if n < 1:
        return n
    else:
        return n + totalseries(n-2)
print(totalseries(14))
print(totalseries(0))