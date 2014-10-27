'''
Write code to reverse a C-Style String.
(C-String means that “abcd” is
represented as five characters,
including the null character.)
'''

def reverse(string):
    return string[::-1]
    
def reverse2(string):
    lst = list(string)
    return ''.join(reversed(lst))
    
print(reverse('hello world'))
print(reverse('abc'))
print(reverse('123'))
print(reverse('write a code'))

print(reverse2('hello world'))
print(reverse2('abc'))
print(reverse2('123'))
print(reverse2('write a code'))