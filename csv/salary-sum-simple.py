import csv
import sys


filename = sys.argv[1]
file = open(filename)
csv_reader = csv.reader(file, delimiter=';')

def gehalt_aus_row(row):
    return int(row[6])

print(sum(map(gehalt_aus_row, list(csv_reader)[1:])))
