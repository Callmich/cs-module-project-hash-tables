import random
# 1. Read the file `input.txt` and split it into words.
# 2. Analyze the text, building up the dataset of which words can follow particular words.
# 3. Choose a random "start word" to begin.
# 4. Loop through: Print the word - If it's a "stop word", stop - Else randomly choose a word that can follow this one.

# Start words are words that begin with a capital, or a `"` followed by a capital.


# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here

split_words = f.split()

word_dict = {}

for x in range (len(split_words[:-1])):
    if not word_dict.get(split_words[x]):
        word_dict[split_words[x]] = [split_words[x+1]]
    else:
        word_dict[split_words[x]] += [split_words[x + 1]]

print(word_dict)


# TODO: construct 5 random sentences
# Your code here

