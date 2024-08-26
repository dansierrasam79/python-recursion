# sum a list of lists

def list_sum(lst):
    total = 0
    for item in lst:
        if isinstance(item, (list)):
            total += list_sum(item)
        else:
            total += item
    return total

print(list_sum([1, 2, [3, 4], [5, 6]]))
