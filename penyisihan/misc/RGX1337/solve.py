import re

matches = []

with open('flags.txt') as f:
    for line in f:
        matches += re.findall('slashroot7{[A-Z]{5}\d{6}[a-z]{8}[A-Z]{7}}', line)

for match in matches:
    print(match)
