import sys
import adressbuch


rows = adressbuch.read_data(sys.argv[1])

summe = 0
for persnr, vorname, nachname, email, adresse, geschlecht, gehalt in rows:
    summe += gehalt

print('Budget:', summe)
