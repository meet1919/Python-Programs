from itertools import permutations
name = 'elvis'
perm = [''.join(i) for i in permutations(name)]
print(perm)
