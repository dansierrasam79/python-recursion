# sum series
def power_of(a,b):
    if a == 0:
        return 0
    elif b == 0:
        return 0
    elif b== 1:
        return a
    else:
        return a + power_of(a,b-1)
print(power_of(4,2))
print(power_of(1,3))