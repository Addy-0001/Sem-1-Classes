# a = "Python"
# # Escape Characters 
# # \n - New Line
# print("Hello\nPython")

# # \t - Tab
# print("Hello\tPython")

# # \b - Backspace
# print("Hello\bPython")

# # \r - Carriage Return
# print("Hello\rPython")

# # \f - Form Feed
# print("Hello\fPython")

# #\v - Vertical Tab
# print("Hello\v\v\vPython")

# #Raw String
# print(r"Hello\nhi")

# #/r - Carriage Return
# print("HelloWorld\rPython")

# # Replacing String
# a = "python"
# print(a)
# b = a.replace('p', 'P')
# a = b
# print(a)

# a = "python"
# b = a.replace('y', 'Y').replace('t', 'T')
# a = b
# print(a)

# a = "python"
# b = a.replace('n', '')
# a = b
# print(a)

# a = "python"
# b = a.replace('t', 'tA')
# print(b)

# a = "python"
# b  = a[0:3] + "A" + a[3:]
# print(b)

# a = "python"
# b = a[ : 5] + "A" + a[5 : ]
# print(b)
# print(a.upper())
# print(b.lower())
# print(b.swapcase())

# c = 'Hi People'
# print(c.title())
# print(c.capitalize())
# if c.isupper():
#     print("All Upper")
# elif c.istitle():
#     print("TITLE CASE")
# elif c.islower(): 
#     print("All lower")
# else: 
#     print("Some Uppper, some lower")

a = "pytho"
no = 10
starno = no + len(a)
print(a.center(starno, '*'))
print(a.center(10, "*"))
print(a.center(8, "*"))
print(a.zfill(10))


'''
    isidentifier() 
    isspare()
    isalpha()
    isalnum()
    isspace()
'''

a = "py1thon"
print(a.isidentifier())
print(a.isspace())
print(a.isalpha())
print(a.isalnum())

# find, rfind, index and rindex
print(a.find('h'))
print(a.rfind('h'))
print(a.index('h'))
print(a.rindex('h'))

# count
# HW - How Split, Splitlines, Join, Partition, and rpartition works

a = "Hello Python"
print(a.count('o'))
