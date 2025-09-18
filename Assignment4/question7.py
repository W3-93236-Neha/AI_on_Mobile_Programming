#Write a version of a palindrome recognizer that also accepts phrase palindromes such as
#  "Go hanga salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis",
#  "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori",
# "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are 
# usually ignored.

import re

def is_phrase_palindrome(phrase):
   
    
    processed_phrase = re.sub(r'[^A-Za-z0-9]', '', phrase).lower()
    
   
    return processed_phrase == processed_phrase[::-1]

# Test cases
test_phrases = [
    "Go hanga salami I'm a lasagna hog.",
    "Was it a rat I saw?",
    "Step on no pets",
    "Sit on a potato pan, Otis",
    "Lisa Bonet ate no basil",
    "Satan, oscillate my metallic sonatas",
    "I roamed under it as a tired nude Maori",
    "Rise to vote sir",
    "Dammit, I'm mad!",
    "This is not a palindrome.",
]

for phrase in test_phrases:
    result = "is" if is_phrase_palindrome(phrase) else "is not"
    print(f'"{phrase}" {result} a palindrome.')

