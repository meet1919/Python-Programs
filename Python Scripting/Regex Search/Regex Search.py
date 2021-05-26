# Write a program that opens all .txt files in a folder and searches for any
# line that matches a user-supplied regular expression. The results should
# be printed to the screen.

import os
import re

os.chdir('C:\\Users\\meetg\\PycharmProjects\\untitled\\Random Projects\\Regex Search\\Text Folder')
# os.mkdir('C:\\Users\\meetg\\PycharmProjects\\untitled\\Random Projects\\Regex Search\\Text Folder')
directory = os.listdir('C:\\Users\\meetg\\PycharmProjects\\untitled\\Random Projects\\Regex Search\\Text Folder')
print('Total files in this folder: ')
print(directory)

text1 = open('Text1.txt', 'w')
text1.write('My name is Meet Gondaliya and my phone number is 9825521452')
text1.close()

text2 = open('Text2.txt', 'w')
text2.write('My name is Animesh Gondaliya and my phone number is 9825349905')
text2.close()

text3 = open('Text3.txt', 'w')
text3.write('My name is Aruna Gondaliya and my phone number is 9624003542')
text3.close()

text4 = open('Text4.txt', 'w')
text4.write('My name is Priya Gondaliya and my phone number is 8320006101')
text4.close()

print('')
print('List of all the phone numbers inside multiple files:')

for files in os.listdir():
    if files.endswith('.txt'):
        text_file = open(files, 'r')
        text = text_file.read()
        phone_number = re.compile(r'\d{10}')
        mo = phone_number.findall(text)

        print(mo)
        text_file.close()