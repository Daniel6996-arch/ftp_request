import csv

file_loc = 'water_dispense_data/dispensed.csv'

def process_csv_file(file):
    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list()
        for row in csv_reader:
            
            data.append(row)
        
    return data

def show():
   print( process_csv_file('water_dispense_data/dispensed.csv'))