import sys
import adressbuch


filename = sys.argv[1]

rows = adressbuch.read_data(filename)

gehaelter = []

for row in rows:
    gehaelter.append(row[6])

avg = sum(gehaelter)/len(gehaelter)
print(avg)
