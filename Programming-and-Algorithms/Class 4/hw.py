#                   split
# ---------------------------------------------------------------------------------------------------------------------------------------------------
string = "Hello, world! How are you?"                                                                                                               
words = string.split()  # Splits the string from whitespace.                                                                                        
print(words)                                                                                                                                        
'''                                                                                                                                                 
    Output:     ['Hello,', 'world!', 'How', 'are', 'you?']                                                                                            
            Here, we can see that the string is split from whitespaces and an array of strings is returned.                                         
'''                                                                                                                                                     
                                                                                                                                                    
# Passing an argument to specify what splits the string.                                                                                            
string = "1 - 2 - 3 - 4 - 5"                                                                                                                        
numbers = string.split("-")  # split the string into a list of numbers                                                                              
print(numbers)                                                                                                                                      
                                                                                                                                                    
'''                                                                                                                                                 
 Output:    ['1 ', ' 2 ', ' 3 ', ' 4 ', ' 5']                                                                                                       
        Here, we can see that the space isn't ignored but included as a part of the array.                                                          
        If you want the spaces to disappear, simply add spaces to each side of "-" making it " - " while passing the argument                       
'''                                                                                                                                                 
# ---------------------------------------------------------------------------------------------------------------------------------------------------


#               splitlines
# ---------------------------------------------------------------------------------------------------------------------------------------------------
string = "Hello\nworld\nHow are you?\r\nI'm fine, thanks."
split_lines = string.splitlines()
print(split_lines)
'''
    Output:     ['Hello', 'world', 'How are you?', "I'm fine, thanks."]
'''

string = "Hello\nworld\nHow are you?\r\nI'm fine, thanks."
lines = string.splitlines(keepends=True)
print(lines)

'''
    Output: ['Hello\n', 'world\n', 'How are you?\r\n', "I'm fine, thanks."]
        Keeps the escape characters
'''
# ---------------------------------------------------------------------------------------------------------------------------------------------------


#               Join
# ---------------------------------------------------------------------------------------------------------------------------------------------------
words = ['Hello,', 'world!', 'How', 'are', 'you?']
string = ' '.join(words)  # join the list of words into a single string [space is the seperator]
print(string)
'''
    Output:     Hello, world! How are you?
'''

numbers = ['1', '2', '3', '4', '5']
string = ','.join(numbers)  # join the list of numbers into a single string [Comma is the separator]
print(string)
'''
    Output: 1,2,3,4,5
'''
# ---------------------------------------------------------------------------------------------------------------------------------------------------


#               Partition
# ---------------------------------------------------------------------------------------------------------------------------------------------------
string = "Hello, world!"
parts = string.partition(" ")  # partition the string at the comma and space
print(parts)
# Output: ('Hello', ', ', 'world!')

string = "apple"
parts = string.partition(" ")  # partition the string at the comma and space
print(parts)
# Output: ('apple', '', '')
# ---------------------------------------------------------------------------------------------------------------------------------------------------


#               rpartition
# ---------------------------------------------------------------------------------------------------------------------------------------------------
string = "Hello, world!"
parts = string.rpartition(", ")  # partition the string at the comma and space from the right
print(parts)
'''
    Output: ('Hello', ', ', 'world!')
'''
string = "apple"
parts = string.rpartition(", ")  # partition the string at the comma and space from the right
print(parts)
'''
    Output: ('', '', 'apple')
'''
# ---------------------------------------------------------------------------------------------------------------------------------------------------

def function1():
    print("This is function 1")


function1()