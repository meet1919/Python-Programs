text = open('2of4brif.txt', 'r')
list = set(text.read().split())
palindromes = []

for word in list:
    if word == word[::-1]:
        palindromes.append(word)

print('Number of palindromes found: %s' % (len(palindromes)))
print(palindromes)
