import re

'''Adding Dictionary to Variable'''
words = open('2of4brif.txt', 'r')
dictionary = set(words.read().split())

'''Opening our Message and matching specific patterns 
   (Here the letter we need to find is 3rd letter after punctuation)'''
text = open('cipher.txt', 'r')
cipher = str((text.read()).replace(' ', ''))
punctuation_regex = re.compile(r'[:,.;\']\w{3}')
match = punctuation_regex.findall(cipher)
plaintext = ''
for i in match:
    plaintext += (i[(len(i)-1):])

print('Your message is: ', plaintext)
