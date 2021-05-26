words = open('2of4brif.txt', 'r')
dictionary = set(words.read().split())

print('Welcome to Vocabulary training.\nThis code will display a list of random words\n')
input_message = "Panel at east end of chapel slides"
message = input_message.replace(' ', '')
index = 0
words_practice = []
for word in dictionary:
    '''Encoding message in second letter of thw word'''
    if ((message)[index]).lower() == word[2]:
        if index < len(message):
            words_practice.append(word)
            index += 1
        if index >= len(message):
            break

print(words_practice)
