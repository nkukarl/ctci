'''
Write a method to replace all spaces
in a string with ‘%20’.
'''

def replace_space(string):
    new_list = []
    for i in string:
        if i == ' ':
            new_list.append('%20')
        else:
            new_list.append(i)
    return ''.join(new_list)
    
print(replace_space('s t r i n g'))
print(replace_space('hello world'))
print(replace_space('helloworld'))