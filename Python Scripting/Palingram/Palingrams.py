text = open('2of4brif.txt', 'r')
list = set(text.read().split())
pali_list = []

for word in list:
    end = len(word)
    rev_word = word[::-1]
    if end > 1:
        for i in range(end):
            if word[i:] == rev_word[:end-i]and rev_word[end-i:]in list:
                pali_list.append((word, rev_word[end-i:]))
            if word[:i] == rev_word[end-i:]and rev_word[:end-i]in list:
                pali_list.append((rev_word[:end-i], word))

palingrams_sorted = sorted(pali_list)

#display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
