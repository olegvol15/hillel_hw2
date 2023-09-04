import string

text = """Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.
Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.
Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами."""

translator = str.maketrans('', '', string.punctuation)
text = text.translate(translator).lower()

words = text.split()
word_count = {}
for word in words:
    word_count[word] = word_count.setdefault(word, 0) + 1


max_word = max(word_count, key=word_count.get)
max_count = word_count[max_word]

min_word = min(word_count, key=word_count.get)
min_count = word_count[min_word]
print(word_count)
print(f"The word '{max_word}' appears {max_count} times the most in the text.")
print(f"The word '{min_word}' appears {min_count} times the least in the text.")  
