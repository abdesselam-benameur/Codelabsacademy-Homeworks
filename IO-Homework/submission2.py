import string

for letter in string.ascii_uppercase:
    with open('%s.txt' % letter, 'w') as f:
        f.write("")