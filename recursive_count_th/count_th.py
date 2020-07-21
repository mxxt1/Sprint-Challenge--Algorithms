'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
# get length of word
# check if there are enough letters for th
# check the first two letters
# python return {object} add +1 for counter
# if the first two are th, increment the counter and pass the word again frm second letter so "word" is "ord"
# if it's not th, then recurse passing word from second letter ord


def count_th(word):
    
    length = len(word)
    # not enough letters, return zero
    if length < 2:
        return 0
    # if first two letters are th, then recurse and return word from second letter to end, +1 to increment a counter of 'th' instances
    elif(word[:2] == 'th'):
        return count_th(word[1:]) + 1 
    else:
    # recurse, returning word from second letter to end
        return count_th(word[1:])

print(count_th("thenthenthetenththethe"))









# def count_th(word):
# if len(word) == 0 or len(word) < 2:
#     return 0

# if word[:2] == 'th':
#!  add + 1 to recursive return creates count of found --> no need to create global count, will return count
#     return count_th(word[1:]) + 1
# else:
#     return count_th(word[1:])


# if len(word) < 2 or len(word) == 0:
#     return 0

#  split = list(word)
    # if (split[0] == 't' and split[1] == 'h'):
    #     word = word[2:]
    #     return count_th(word) + 1
#     else: 
#         word=word[2:]
#         return count_th(word) 
    
#     return word
