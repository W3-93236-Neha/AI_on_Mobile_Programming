#Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's language").
#  That is, double every consonant and place an occurrence of "o" in between. For example, translate("this is fun") 
# should return the string "tothohisos isos fofunon".
def translate(n):
    translate_text=[]
    consonant="bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    for letters in n:
        if letters in consonant:
            translate_text.append(letters + 'o' + letters)
        else:
            translate_text.append(letters)

    return "".join(translate_text)
original_text="this is run"
translated_text=translate(original_text)
print(f'Orininal:{original_text}')
print(f'Translated:{translated_text}')

original_text_2="Python is a great language"
translated_text_2=translate(original_text_2)
print(f'original:{original_text_2}')
print(f'Translated: {translated_text_2}')
           

        