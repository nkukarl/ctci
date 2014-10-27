'''
Assume you have a method isSubstring
which checks if one word is a substring
of another. Given two strings, s1 and s2,
write code to check if s2 is a rotation
of s1 using only one call to isSubstring
(i.e., “waterbottle” is a rotation of
“erbottlewat”).
'''

def is_rotation(str1, str2):
    if len(str1) != len(str2):
        return False
    else:
        return str2 in str1 + str1
        #return str1 in str2 + str2

print(is_rotation('apple', 'pleap'))
print(is_rotation('apple', 'ppale'))
print(is_rotation("waterbottle", "erbottlewat"))