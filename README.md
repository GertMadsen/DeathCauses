# Python Assignment 3 - Group: Plain Product.
### Analyzing dataset from Foolish Supermarket : Leading causes of deaths in The United States

* Link to download of dataset: [https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD](https://data.cdc.gov/api/views/bi63-dtpu/rows.csv?accessType=DOWNLOAD)
* This program analyzes a dataset about the leading causes of deaths in The United States and answer [questions](https://github.com/Zurina/Dataset) like which state has most deaths cause by a certain decease or which state has the highest or lowest increase in deaths. 
* This program also produces a plot that shows the increase of death per year for a specific period of time in a specific state with a specific cause of death.

### Procedure to run the program:
* Clone the project into your computer.
* How to use the program:
  * In a command prompt or bash with Python available, use the following command together with the URL to the CSV file: 
  * python main.py https://raw.githubusercontent.com/GertMadsen/csvfiles/master/NCHS_-_Leading_Causes_of_Death__United_States.csv
  * *Since the link to the CSV file in the assignment is not a link to the CSV file itself - we have downloaded the CSV file and placed it in our own CSV file repository. This way we can use the link mentioned above as argument to our main.py*

### Dependencies:
* Python - Anaconda Distribution 
* *In order to make sure that all librabies are present for a problem free execution of the software, we recommend using an Anaconda distribution of Python. But the software will probably also run with other distributiions, but then libraries such as Requests might need to be installed.*

### Using the program should result in the following output:

* **Console output:**

In 2016 California has most deaths caused by 'All causes' with 262240 deaths.

In 2016 Alaska has the least deaths caused by 'All causes' with 4494 deaths.

From 1999 to 2016, Rhode Island has the smallest increase in deaths with a 27 increase in deaths caused by 'All causes'

In 2005 Pennsylvania has most deaths caused by 'Kidney disease' with 3108 deaths.

Plot saved in plots folder as 'Annual_death_increase_for_Alzheimer's disease_in_California.png'.

From 1999 to 2016, California has the highest increase in deaths with a 11038 increase in deaths caused by 'Alzheimer's disease'

* **The CSV file should be downloaded to the 'csv' folder.**

* **A plotting image should be created in .png format and found in the 'plots' folder as:** 
  * 'Annual_death_increase_for_Alzheimer's disease_in_California.png'.

* **OBS:** *When creating the plot it should be displayed in a new window and the program execution will halt until this window is closed.*

### Group members: Lene, Mikkel H, Devran & Gert. 
