import pprint
print("Enter a phrase whose characters you want to count")
message = input()
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
