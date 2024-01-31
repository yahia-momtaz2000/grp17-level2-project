
print('--- check for a word if palindrome ------')

# normal way
def check_word(word):
    if word == word[::-1]:
        return True
    else:
        return False

# main program
result = check_word('radar')
print(result)

# Recursion
def recursive_palind(word):
    if len(word) == 0:
        return True
    else:
        return word[0] == word[-1] and recursive_palind(word[1:-1])

# main program
result = check_word('radar')
print(result)
