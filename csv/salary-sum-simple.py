import sys
import adressbuch


rows = adressbuch.read_data(sys.argv[1])

def gehalt_aus_row(row):
    return row[6]

print(sum(map(gehalt_aus_row, rows)))
