a = {1, 2, 3, 4, 8, 7, 5, 10}
print(a)
a.add(6)
print(a)
a.remove(1)
print(a)
a.pop()
print(a)
a.discard(7)
# a.discard() This gives error
print(a)
a.clear()
print(a)
b = {1, 2, 3, 4, 5}
c = {4, 5, 6, 7, 8}
print(b.union(c))  # same as b | c
print(b.intersection(c))  # same as b & c
print(b.difference(c))  # same as b - c
print(b.symmetric_difference(c))  # same as b ^ c
print(b.isdisjoint(c))  # True if no common element
print(b.issubset(c))  # True if b is subset of c
print(b.issuperset(c))  # True if b is superset of c
print(b.update(c))  # same as b |= c
print(b)  # b is updated
print(b.intersection_update(c))  # same as b &= c
print(b)  # b is updated
print(b.difference_update(c))  # same as b -= c
print(b)  # b is updated
print(b.symmetric_difference_update(c))  # same as b ^= c
print(b)  # b is updated
print(b.copy())  # shallow copy of b
print(b)  # b is not updated
print(b.pop())  # removes and returns an arbitrary element from b
print(b)  # b is updated
print(type(a))
