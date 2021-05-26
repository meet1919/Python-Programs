ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"
list_cipher = list(ciphertext.split())
key = [-1, 2, -3, 4]
route_length = int(len(list_cipher) / len(key))
list_of_list = []
plaintext = ''
start = 0
stop = route_length
for k in key:
    if k < 0:
        list_of_list.append((list_cipher[start:stop])[::-1])
    if k > 0:
        list_of_list.append(list_cipher[start:stop])
    start += route_length
    stop += route_length

for i in range(route_length):
    for col_items in list_of_list:
        word = str(col_items.pop(0))
        plaintext += word + ' '

print('You Cipher Text is: ', ciphertext)
print('Your Plain Text is: ', plaintext)



