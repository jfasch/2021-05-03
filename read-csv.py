import csv
import sys


filename = sys.argv[1]
file = open(filename)
csv_reader = csv.reader(file, delimiter=';')

for persnr, vorname, nachname, email, adresse, geschlecht, gehalt in csv_reader:
    print(f'PersonalNr: {persnr}, Vorname: {vorname}, Nachname: {nachname}, Email: {email}, Adresse: {adresse}, Geschlecht: {geschlecht}, Gehalt: {gehalt}')


