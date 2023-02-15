wp = 'worm party'

# for i in range(0, len(text)):
#     character = text[i]
#     if character != 'o':
#         print(i)

# for i in wp:
#     print(ord(i))

wormvalues = (119, 111, 114, 109, 32, 112, 97, 114, 116, 121)

for i in wormvalues:
    for j in range(i):
        print('o', end = "")
    print('x', end = "")


