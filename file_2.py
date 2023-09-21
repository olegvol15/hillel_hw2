def longest_words(file):
    with open(file, 'r') as f:
        text = f.read()

    words = text.split()

    if not words:
        return []

    max_length = max(len(word) for word in words)
    longest_words_list = [word.strip() for word in words if len(word) == max_length]

    return longest_words_list

with open('article.txt', 'w') as file:
    while True:
        line = input("Enter a line of text to write to the file (empty line to finish): ")
        if line == "":
            break
        file.write(line + '\n')

print("The 'article.txt' file has been created, and data has been written to it.")

result = longest_words("article.txt")
if not result:
    print("There are no words in the text.")
else:
    print("Longest word(s):", result)




