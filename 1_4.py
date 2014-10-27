'''
Write a method to decide if two strings
are anagrams or not.
'''

def is_anagram(str1, str2):
    if len(str1) != len(str2) or str1 == str2:
        return False
    else:
        return sorted(str1) == sorted(str2)
        
print(is_anagram('heart', 'earth'))
print(is_anagram('heart', 'heart'))
print(is_anagram('heart', 'hear'))
print(is_anagram('123', 'hear'))