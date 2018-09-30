'''
    Converts the CSV file into a for our exercise more useful representation of the data
'''
import csv

# This function cleans the data in the CSV file 
def convert(file_name):
    with open(file_name) as fp:
        reader = csv.reader(fp)
        next(reader)
        data_set = []
        for line in reader:
            # We only uses year, cause, state and death from the data set since this is all we need for the exercise.
            year, _, cause, state, death, _ = line
            year, death, = int(year), int(death)
            # We filter away the 'United States' entry in order to only focus on states.1
            if state != "United States":
                data_set.append([year, cause, state, death])
    return data_set