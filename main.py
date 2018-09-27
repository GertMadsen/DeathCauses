'''
Usage: 
    python main.py [<url>]
Example:
    python main.py https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD
'''

import os
import sys
from lib.download import download
import numpy as np

if __name__ == '__main__':
    try:
        _, url = sys.argv
        file_name = os.path.basename(url)
        download(url, file_name)
        print("A")    
    except Exception as e:
        print("B")
        print(__doc__)
        sys.exit(1)  

    data = np.genfromtxt(file_name,delimiter=",",dtype=np.uint, skip_header=1)
    print(data)

