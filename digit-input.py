import sys

try:
    digit = int(input('Bitte gib hier eine Ziffer ein: '))
except ValueError:
    print('du depp, hier wollen wir nur integers')
    sys.exit()

translation_table = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
}

try:
    translated = translation_table[digit]
except KeyError:
    print(digit, 'ist keine ziffer')
    sys.exit()
    
print(translated)

