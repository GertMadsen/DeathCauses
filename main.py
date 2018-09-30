'''
Usage: 
    python main.py [<url>]
Example:
    python main.py https://raw.githubusercontent.com/GertMadsen/csvfiles/master/NCHS_-_Leading_Causes_of_Death__United_States.csv
'''

import os
import sys
from lib.converter import convert
from lib.download import download
import lib.statistic as stat

if __name__ == '__main__':
    file_dir = 'csv'
    # If the csv directory already exits it will be created
    if not os.path.isdir(file_dir):
        os.makedirs(file_dir)

    try:
        _, url = sys.argv
        file_name = os.path.join(file_dir, os.path.basename(url))
        download(url, file_name)   
    except Exception as e:
        print(__doc__)
        sys.exit(1)  

    
    # After downloading the csv file we use our own converter to read the file and clean it up. 
    # We filter some data way in order to represent our data in away we find more easy to work with
    data_set = convert(file_name)

    print(stat.find_most_death(data_set, 2016, "All causes"))
    print(stat.find_least_death(data_set, 2016, "All causes"))
    print(stat.find_least_inc(data_set, 1999, 2016, "All causes"))
    print(stat.find_most_death(data_set, 2005, "Kidney disease"))
    print(stat.find_most_inc(data_set, 1999, 2016, "Alzheimer's disease"))
    