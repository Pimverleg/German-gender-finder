# German-gender-finder
Find the gender of the German word.

You can use this script to find out what article your german word needs. Der, Die or Das

## Usage 

Finding the gender of the word "Besuch" directly from the command line (cmd):

![image](https://user-images.githubusercontent.com/13415440/170574091-b78b883f-a863-4d6a-b33b-903f61ca290a.png)


Or from within a script

```python
import find_gender
print(find_gender.get_gender_of_word('mutter'))
#{'word': 'mutter', 'definite_article': 'die', 'indefinite_article': 'eine', 'warning': 'Sure: Found in word list, highly reliable'}
```


## Notes

1. The script first searches a world list.
2. If the script cannot find the word in the list it will use grammar rules to find its gender.
3. All words that are exceptions to rules should be in the list.

## return values

The script always returns a dictionary with a warning message detailing the reliability:

```python
# very reliable
{
  'word': 'somewordyouchose', 
  'definite_article': 'die',
  'indefinite_article': 'eine',
  'warning': 'Sure: Found in word list, highly reliable'
}


# very reliable
{
    'word': 'somewordyouchose',
    'definite_article': 'der',
    'indefinite_article': 'ein',
    'warning': 'Sure: male due to masculine ending'
}

# not sure, see warning message!
{
     'word': 'somewordyouchose',
     'definite_article': 'der',
     'indefinite_article': 'ein',
     'warning': 'Unsure: However 80% of words ending in "en" are masculine'
}

# all messages you could get:

'warning': 'Sure: Found in word list',
'warning': 'Sure: male due to masculine ending',
'warning': 'Sure: female due to feminine ending',
'warning': 'Sure: neuter due to neuter ending',
'warning': 'Unsure: However 80% of words ending in "en" are masculine',
'warning': 'Unsure: However 60% of nouns ending in "el" are masculine',
'warning': 'Unsure: However 60% of nouns ending in "er" are masculine',
'warning': 'Unsure: However 90% of nouns ending in "e" are masculine',
'warning': 'Unsure: However 90% of nouns starting with "ge" are feminine',
'warning': 'Unsure: Most nouns ending in -t originating from verbs are feminine.',
'warning': 'Not_found: word not found',
 


```

The words in the word list are taken from:

https://github.com/mejutoco/german-grammar-statistics

I removed all words without a gender assigned.

    

