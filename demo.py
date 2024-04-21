from src.boxify import boxify

print('Single line, word.')
print(boxify('Hello!'))

print()

print('Single line, sentence.')
print(boxify('Hey there! how are you?'))

print()

print('Multiple lines, paragraph')
paragraph = """Just creating a small function.
It is so because I am bored.
I don't know what to fill here too."""
print(boxify(paragraph))

print('Setting a fixed width for a paragraph.')
paragraph = """Just creating a small function.
It is so because I am bored.
I don't know what to fill here too."""
print(boxify(paragraph, width=80))

print('Setting a fixed width for a paragraph.')
paragraph = """Just creating a small function.
It is so because I am bored.
I don't know what to fill here too."""
print(boxify(paragraph, width=80, align="centre"))