import sys

name = input('Name: ')

sex = input('Sex (m/f): ')
sex = sex.lower()
if sex not in ('m', 'f'):
    print('invalid sex: expected (m/f)')
    sys.exit(1)

try:
    hour = int(input('Hour of day (0-23): '))
except ValueError:
    print('not a number')
    sys.exit(2)

if not 0 <= hour <= 23:
    print('hour must be between (inclusive) 0 and 23')
    sys.exit(3)

if sex == 'm':
    anrede = 'Mr.'
if sex == 'f':
    anrede = 'Mrs.'
if 0 <= hour <= 9:
    timeofdaystr = 'Good morning'
if 10 <= hour <= 17:
    timeofdaystr = 'Good day'
if 18 <= hour <= 23:
    timeofdaystr = 'Good evening'

print(timeofdaystr + ', ' + anrede + ' ' + name)    
