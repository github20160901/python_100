from functools import reduce                   # 引入reduce


def sum(x, y):
    return x + y

print (reduce(sum, range(0, 10)))
print (reduce(sum, range(0, 10), 10))
print (reduce(sum, range(0, 0), 10))
