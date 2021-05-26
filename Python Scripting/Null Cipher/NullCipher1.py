'''For this practice project, write a program that embeds the message
“Give your word and we rise” in a list of surnames. To hide the letters
in the message, start at the second letter in the second name, move to
the third letter in the third name, and then keep alternating between
second and third letters for the remaining words.'''

import string
surnames = open('surname.txt', 'r')
list_surnames = set(surnames.read().split())
message = 'Give your word and we rise'.replace(' ', '').lower()
index = 0
index1 = 0
cipher = []
int_num = 1
float_num = 1.5

'''Loop through all the surnames in list_surnames'''
for surname in list_surnames:
    '''If the value of index is less than the total letters in message than continue'''
    if index < len(message):
        '''Surname should be greater than four letters and should be starting with a letter'''
        if len(surname) > 4 and surname[0] in string.ascii_letters:
            if len(cipher) == 0:
                '''First word of Cipher should not contain any letter of message'''
                cipher.append(surname)
                index1 += 1

            elif len(cipher) == index1:

                if len(cipher) % 2 == 1:
                    '''This adds a word having message letter in second index position'''
                    if message[index] == surname[1]:
                        cipher.append(surname)
                        index += 1
                        index1 += 1

                elif len(cipher) % 2 == 0:
                    '''This adds a word having message letter in third index position'''
                    if message[index] == surname[2]:
                        cipher.append(surname)
                        index += 1
                        index1 += 1
    '''If value of index is greater than equal to the letters in message, break the loop'''
    if index >= len(message):
        break

for i in cipher:
    print(i)

