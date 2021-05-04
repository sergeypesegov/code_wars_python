''' What is an anagram? Well, two words are anagrams of each other 
if they both contain the same letters. For example:

'abba' & 'baab' == true

'abba' & 'bbaa' == true

'abba' & 'abbba' == false

'abba' & 'abca' == false
Write a function that will find all the anagrams of a word from a list. 
You will be given two inputs a word and an array with words. 
You should return an array of all the anagrams or an empty array 
if there are none. For example:

anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']) => ['aabb', 'bbaa']

anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']) => ['carer', 'racer']

anagrams('laser', ['lazing', 'lazy',  'lacer']) => []'''

def anagrams(word, words):
    res_words = []
    
    dict_of_letters = {}
    for letter in word:
        if letter not in dict_of_letters:
            dict_of_letters[letter] = 1
        else:
            dict_of_letters[letter] += 1
            
    for word in words:
        dict_of_letters_new = {}
        for letter in word:
            if letter not in dict_of_letters_new:
                dict_of_letters_new[letter] = 1
            else:
                dict_of_letters_new[letter] += 1
        
        if dict_of_letters_new == dict_of_letters:
            res_words.append(word)
    return res_words