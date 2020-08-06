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
start_words = []
end_words = []

for x in range (len(split_words[:-1])):
    if not word_dict.get(split_words[x]):
        word_dict[split_words[x]] = [split_words[x+1]]
    else:
        word_dict[split_words[x]] += [split_words[x + 1]]

for x in split_words:
    if x[0].isupper() or len(x) > 1 and x[1].isupper():
        start_words.append(x)
    elif x[-1] == "." or x[-1] == "?" or x[-1] == "!" or len(x) > 1 and x[-2] == "." or len(x) > 1 and x[-2] == "?" or len(x) > 1 and x[-2] == "!":
        end_words.append(x)

for x in range (0,5):
    stop_sentence = False
    word_to_print = random.choice(start_words)
    while not stop_sentence:
        print(word_to_print, end=" ")
        if word_to_print in end_words:
            stop_sentence = True
            break
        word_to_print = random.choice(word_dict[word_to_print])
    print(" ")
    
# TODO: construct 5 random sentences
# Your code here 

