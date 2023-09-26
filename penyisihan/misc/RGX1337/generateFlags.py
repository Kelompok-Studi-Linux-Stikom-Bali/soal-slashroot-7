import random, string

flagStart = 'slashroot7{'
flagEnd = '}'

with open('flags.txt', 'w') as f:
    for flagCount in range(5000):
        if (flagCount == 787):
            firstPart = ''.join(random.choices(string.ascii_uppercase, k=5))
            secondPart = ''.join(random.choices(string.digits, k=6))
            thirdPart = ''.join(random.choices(string.ascii_lowercase, k=8))
            fourthPart = ''.join(random.choices(string.ascii_uppercase, k=7))
            flagContent = firstPart + secondPart + thirdPart + fourthPart
        else:            
            flagContent = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=26))

        f.write(flagStart + flagContent + flagEnd)
        f.write('\n')
