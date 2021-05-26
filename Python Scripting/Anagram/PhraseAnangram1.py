import sys
from collections import Counter
text = open('2of4brif.txt', 'r')
list_words = set(text.read().split())

print('Make your own anagram phrase with your name')
input_word = (input('Enter you name: ')).replace(' ', '')
name_letters = sorted(list(input_word))
len_name = len(name_letters)

def containedInFirst(a, b):
  a_count = Counter(a)
  b_count = Counter(b)
  for key in b_count:
    if b_count[key] > a_count[key]:
      return False
  return True

anagram = []
for word in list_words:
    words_letters = sorted(list(word))
    if containedInFirst(name_letters, words_letters) == True:
        anagram.append(word)

for word in anagram:
    print(word)

select = input('Select your first word for Anagram: ')
remaining_letter = name_letters
if select in anagram:
    anagram.remove(select)
