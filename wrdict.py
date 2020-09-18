import csv

with open('dic.csv', 'r', encoding='utf-8') as f:
    fields = ['name', 'age', 'profession']
    reader = csv.DictReader(f, fields, delimiter=';')
    for row in reader:
        print(row)        