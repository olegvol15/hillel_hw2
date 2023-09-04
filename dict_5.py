input_string = 'python is good language to code'

char_count = {}

for char in input_string:
    if char >= 'a' and char <= 'z':
        char_count[char] = char_count.get(char, 0) + 1

print(char_count)
