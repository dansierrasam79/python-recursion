# sum series
def harmonicseries(n):
    if n < 2:
        return n
    else:
        return n + 1/harmonicseries(n-1)
print(harmonicseries(14))
print(harmonicseries(1))