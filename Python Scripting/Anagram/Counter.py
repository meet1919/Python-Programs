from itertools import permutations
word = 'elvis'
perms = {''.join(i) for i in permutations(word)}
print(perms)