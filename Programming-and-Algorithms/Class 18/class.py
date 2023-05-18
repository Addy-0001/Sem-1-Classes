add = lambda a, b : a + b
sub = lambda a, b : a - b
mul = lambda a, b : a * b
div = lambda a, b : a / b

print(add(10, 20))
print(sub(10, 20))
print(mul(10, 20))
print(div(10, 20))

#using map function 
print(list(map(add, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])))
print(list(map(sub, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])))
print(list(map(mul, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])))
print(list(map(div, [1, 2, 3, 4, 5], [1, 2, 3, 4, 5])))

# using reduce function
from functools import reduce
print(reduce(add, [1, 2, 3, 4, 5]))
print(reduce(sub, [1, 2, 3, 4, 5]))
print(reduce(mul, [1, 2, 3, 4, 5]))
print(reduce(div, [1, 2, 3, 4, 5]))

#using filter function
print(list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x % 2 != 0, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x > 2, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x < 2, [1, 2, 3, 4, 5])))
print(list(filter(lambda x: x == 2, [1, 2, 3, 4, 5])))