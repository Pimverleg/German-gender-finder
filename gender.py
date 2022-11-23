import csv
from collections import defaultdict

wordMap = defaultdict(list)
with open('wordList.csv', encoding='utf8') as file:
    dr = csv.DictReader(file)
    for line in dr:
        wordMap[line['Word']] = line['Gender']


# this function tries to find the gender of the german word by its ending.
# at this moment we have already checked the wordlist and not found a match
def find_gender_by_ending(word):
    # first checking the masculine endings,
    # exceptions to this rule have been added to the word list.
    # if you find a false positive please add it to the word list and make a pullrequest
    masculine_endings = ['ant', 'ast', 'ich', 'ig', 'ismus', 'ling', 'or', 'us']
    for masculine_ending in masculine_endings:
        if word.endswith(masculine_ending):
            return {
                'word': word,
                'definite_article': 'der',
                'indefinite_article': 'ein',
                'warning': 'Sure: male due to masculine ending'
            }

    # first checking the feminine endings,
    # exceptions to this rule have been added to the word list.
    # if you find a false positive please add it to the word list and make a pullrequest
    feminine_endings = ['a', 'ei', 'enz', 'heit', 'ie', 'ik', 'shaft', 'sion', 'tät', 'tion', 'ung', 'ur']
    for feminine_ending in feminine_endings:
        if word.endswith(feminine_ending):
            return {
                'word': word,
                'definite_article': 'die',
                'indefinite_article': 'eine',
                'warning': 'Sure: female due to feminine ending'
            }

    # first checking the neuter endings,
    # exceptions to this rule have been added to the word list.
    # if you find a false positive please add it to the word list and make a pullrequest
    neuter_endings = ['chen', 'lein', 'ma', 'ment', 'sel', 'tel', 'um']
    for neuter_ending in neuter_endings:
        if word.endswith(neuter_ending):
            return {
                'word': word,
                'definite_article': 'das',
                'indefinite_article': 'ein',
                'warning': 'Sure: neuter due to neuter ending'
            }

    # now we are at the "educated guess" stage..
    if word.endswith('en'):
        return {
            'word': word,
            'definite_article': 'der',
            'indefinite_article': 'ein',
            'warning': 'Unsure: However 80% of words ending in "en" are masculine'
        }

    # now we are at the "educated guess" stage..
    if word.endswith('el'):
        return {
            'word': word,
            'definite_article': 'der',
            'indefinite_article': 'ein',
            'warning': 'Unsure: However 60% of nouns ending in "el" are masculine'
        }

    # now we are at the "educated guess" stage..
    if word.endswith('er'):
        return {
            'word': word,
            'definite_article': 'der',
            'indefinite_article': 'ein',
            'warning': 'Unsure: However 60% of nouns ending in "er" are masculine'
        }

    # now we are at the "educated guess" stage..
    if word.endswith('e'):
        return {
            'word': word,
            'definite_article': 'die',
            'indefinite_article': 'eine',
            'warning': 'Unsure: However 90% of nouns ending in "e" are feminine'
        }

    # now we are at the "educated guess" stage..
    if word.startswith('ge'):
        return {
            'word': word,
            'definite_article': 'das',
            'indefinite_article': 'ein',
            'warning': 'Unsure: However 90% of nouns starting with "ge" are neuter'
        }

    if word.endswith('t'):
        return {
            'word': word,
            'definite_article': 'die',
            'indefinite_article': 'eine',
            'warning': 'Unsure: Most nouns ending in -t originating from verbs are feminine.'
        }

    # No gender is found, if your word is a real word please make a pullrequest to add it to the dictionary
    return {
        'word': word,
        'definite_article': 'none',
        'indefinite_article': 'none',
        'warning': 'Not_found: word not found'
    }


# Check to see if the word can be found in our dictionary
def get_gender_of_word(word):
    # make it lowercase so capitalized words are also found
    word = word.lower()

    # build the word_info dictionary
    if word in wordMap:
        word_info = {
            'word': word,
            'definite_article': 'none',
            'indefinite_article': 'none',
            'warning': 'Sure: Found in word list, highly reliable'
        }

        gender = wordMap[word]

        # it is a feminine word
        if 'f' in gender:
            word_info['definite_article'] = 'die'
            word_info['indefinite_article'] = 'eine'

        # it is a neuter word
        if 'n' in gender:
            word_info['definite_article'] = 'das'
            word_info['indefinite_article'] = 'ein'

        # it is a masculine word
        if 'm' in gender:
            word_info['definite_article'] = 'der'
            word_info['indefinite_article'] = 'ein'

        return word_info

    return find_gender_by_ending(word)
