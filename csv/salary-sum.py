import csv
import sys


filename = sys.argv[1]
file = open(filename)
csv_reader = csv.reader(file, delimiter=';')

summe = 0
for persnr, vorname, nachname, email, adresse, geschlecht, gehalt in csv_reader:
    try:
        gehalt_als_zahl = int(gehalt)
    except ValueError:
        continue

    summe += gehalt_als_zahl

print('Budget:', summe)
