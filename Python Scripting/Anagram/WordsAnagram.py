import sys
text = open('2of4brif.txt', 'r')
list_words = set(text.read().split())

print('Make your own anagram with words of your choice')
input_word = input('Enter you word: ')
print('\nYour Words are ↓')
letters = sorted(list(input_word))
anagram_list = []

for word in list_words:
    letters_anagram = sorted(list(word))
    if letters_anagram == letters:
        anagram_list.append(word)
        
if len(anagram_list) != 0:
    for anagram in anagram_list:
        print(anagram, file=sys.stderr)
else:
    print('You need a large Dictionary or a new word')