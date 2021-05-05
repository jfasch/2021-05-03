import csv

def read_data(filename):
    '''Read filename as a CSV, ignoring the first row which is
    considered to only be the heading. Convert the 'Gehalt' 
    column to int, and return the remaining rows as a list.
    '''
    file = open(filename)
    rdr = csv.reader(file, delimiter=';')

    rows = []

    for row_no, row in enumerate(rdr):
        if row_no == 0:
            continue
        row[6] = int(row[6])
        rows.append(row)

    return rows
