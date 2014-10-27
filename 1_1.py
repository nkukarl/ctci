'''
Implement an algorithm to determine
if a string has all unique characters.
What if you can not use additional
data structures?
'''

def is_unique(string):
    temp = ''
    for i in string:
        if i not in temp:
            temp += i
        else:
            return False
    return True
    
def is_unique2(string):
    for i in range(len(string)):
        if string[i] in string[i + 1 :]:
            return False
    return True

print(is_unique('abc'))
print(is_unique('hello world'))
print(is_unique('aa'))
print(is_unique('123467'))

print(is_unique2('abc'))
print(is_unique2('hello world'))
print(is_unique2('aa'))
print(is_unique2('123467'))