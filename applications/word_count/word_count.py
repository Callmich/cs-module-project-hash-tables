# # Count the words in an input string
# ## Input
# This function takes a single string as an argument.
# ```
# Hello, my cat. And my cat doesn't say "hello" back.
# ```
# ## Output
# It returns a dictionary of words and their counts:
# ```
# {'hello': 2, 'my': 2, 'cat': 2, 'and': 1, "doesn't": 1, 'say': 1, 'back': 1}
# ```

# Case should be ignored. Output keys must be lowercase.
# Key order in the dictionary doesn't matter.
# Split the strings into words on any whitespace.
# Ignore each of the following characters:
# ```
# " : ; , . - + = / \ | [ ] { } ( ) * ^ &
# ```
# If the input contains no ignored characters, return an empty dictionary.


def word_count(s):
    # Your code here

    # I want to clean the string first make it all lower case and then remove all the unwanted characters.
    # then I want to split the string into a list
    # loop over the list and place each word into a dictionary with the value being the word count.
    # return the dictionary

    
    origString = s.lower()
    removedChars = '":;,.-+=/\|][}{()*^&'

    newString = origString
    for character in removedChars:
        newString = newString.replace(character, "")
    
    print(newString)



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))