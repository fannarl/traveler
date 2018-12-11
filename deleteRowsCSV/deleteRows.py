import os
import csv

with open('deleteRowsCSV/birds.csv', 'r') as inp, open('deleteRowsCSV/temp.csv', 'w') as out:
    writer = csv.DictWriter(out, fieldnames=['type', 'name', 'age'])
    writer.writeheader()
    for row in csv.DictReader(inp):
        if row['type'] != "eagle":
            writer.writerow(row)
   
# Til að eyða gömlu skránni og gera nýju skránna samnefnda gömlu skránni  
os.remove('deleteRowsCSV/birds.csv')
os.rename('deleteRowsCSV/temp.csv', 'deleteRowsCSV/birds.csv')