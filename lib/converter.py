'''
    Converts a csv file to an array
'''
import csv

def convert(file_name):
    with open(file_name) as fp:
        reader = csv.reader(fp)
        header__row = next(reader)
        data = []
        for line in reader:
            year, _, cause, state, death, death_rate = line
            year, death, death_rate = int(year), int(death), float(death_rate)
            data.append([year, cause, state, death, death_rate])
    return data