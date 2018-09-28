'''
    Converts a csv file to an array
'''
import csv

def convert(file_name):
    with open(file_name) as fp:
        reader = csv.reader(fp)
        next(reader)
        data_set = []
        for line in reader:
            year, _, cause, state, death, _ = line
            year, death, = int(year), int(death)
            if state != "United States":
                data_set.append([year, cause, state, death])
    return data_set