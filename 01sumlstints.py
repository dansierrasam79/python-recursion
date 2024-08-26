# sum a list of integers
def to_sum_up(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0] + to_sum_up(lst[1:])

print(to_sum_up([2, 4, 5, 6, 7]))
