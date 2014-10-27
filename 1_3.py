'''
Design an algorithm and write code
to remove the duplicate characters
in a string without using any
additional buffer.
NOTE: One or two additional variables
are fine. An extra copy of the array is not.
FOLLOW UP
Write the test cases for this method.
'''

def remove_duplicate(string):
    pass    

def remove_duplicate2(string):
    temp = ''
    for i in string:
        if i not in temp:
            temp += i
    return temp

print(remove_duplicate('hello world'))
print(remove_duplicate('additional buffer'))
    
print(remove_duplicate2('hello world'))
print(remove_duplicate2('additional buffer'))