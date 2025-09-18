#In following text count occurrence of each letter
#  (irrespective of case). Hint: convert string to same 
# case e.g. text.lower().
 #  ```python
 #  text = """Python is a high-level, general-purpose
 #  programming language. Its design philosophy emphasizes 
 # code readability with the use of significant indentation.
 #  Python is dynamically typed and garbage-collected. 
 # It supports multiple programming paradigms, including 
 # structured, object-oriented and functional programming."""
 #  
 # ```
from collections import Counter

import string
def function1():
    text=''' Python is a high-level, general-purpose
  programming language. Its design philosophy emphasizes 
 code readability with the use of significant indentation.
  Python is dynamically typed and garbage-collected. 
 It supports multiple programming paradigms, including 
 structured, object-oriented and functional programming. '''
    
    result=text.lower()
    print(result)
    #cleaned_text = text.lower()
    clean_text=''.join(n for n in result if n in string.ascii_lowercase )
    print(clean_text)
    counts=Counter(clean_text)
    
    #final_string=sorted(clean_text)
    #print(final_string)
    for letter in sorted(counts):
        print(f"'{letter}':{counts[letter]}")



#letter_counts = Counter(c for c in 
                       # cleaned_text if 'a' <= c <= 'z')


#for letter, count in sorted(letter_counts.items()):
   # print(f"'{letter}': {count}")





function1()    
    

