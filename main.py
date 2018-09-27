'''
Usage: 
    python main.py [<url>]
Example:
    python main.py https://raw.githubusercontent.com/GertMadsen/DeathCauses/master/NCHS_-_Leading_Causes_of_Death__United_States.csv
'''

import os
import sys
from lib.converter import convert
from lib.download import download

if __name__ == '__main__':
    try:
        _, url = sys.argv
        file_name = os.path.basename(url)
        download(url, file_name)   
    except Exception as e:
        print(__doc__)
        sys.exit(1)  

    data = convert(file_name)

