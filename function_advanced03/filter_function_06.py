print('Filter a list of numbers to include only even numbers using a lambda function and filter')

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# normal way
even_list = []
for item in numbers_list:
    if item % 2 == 0:
        even_list.append(item)

print(even_list)

# using Filter function
def get_even(item):
    if item % 2 == 0:
        return item

even_list = list( filter( get_even, numbers_list))
print(even_list)

# using Lambda
even_list = list( filter( lambda item : item % 2 == 0, numbers_list))
print(even_list)

print('---------------- Filter a list of strings to include only those with length greater than 5 -----------------------')
words_list = ['apple', 'banana', 'kiwi', 'orange', 'grape']
# normal mode
new_words_list = []
for word in words_list:
    if len(word) > 5:
        new_words_list.append(word)

print(new_words_list)

# using filter
def get_correct_word(word):
    if len(word) > 5:
        return word

new_words_list = list(filter ( get_correct_word, words_list ) )
print(new_words_list)

# using lambda
new_words_list = list(filter (  lambda word : len(word) > 5 , words_list ) )
print(new_words_list)
