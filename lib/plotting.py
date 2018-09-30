'''
    Create plots to be stored in files 
'''

import matplotlib.pyplot as plt
import numpy as np
import os

# This functions take the data_set, a state, a cause, start year and end year and plots the annual increase in death.
def plot_inc_by_year(data_set, state, cause, start_year, end_year):
    '''
    Makes a plot showing the annual increase in death for a specific state and cause in a given time period:
    '''
    
    years = range(start_year, end_year+1)     
    
    # death_arr is an array containing the total death for the chosen state and cause for every year in the given period.
    death_arr = [data[3] for year in years for data in data_set if data[0] == year and data[2] == state and data[1] == cause]                    
    
    # increase_arr represent the increase from year to year in the period.
    # we use numby to create to arrays with the deaths for respectively the start years and end years for each yearly interval
    # and the we use numby to substract the start values from the end values.  
    end_years = np.array(death_arr[1:])
    start_years = np.array(death_arr[:-1])
    increase_arr = end_years - start_years
    
    plot_file = f'Annual_death_increase_for_{cause}_in_{state}.png'
    plot_dir = 'plots'
    # If the plot directory is not already present it will be created.
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    xs = years[1:]
    ys = increase_arr
    # We create a string to use as xlabes in the plot to show that we plot year intervals.
    xlabels = [f'{year}-{year+1}' for year in years]
    
    plt.title(f"Annual increase in deaths for\n '{cause}' in '{state}'", fontsize=14)
    plt.xlabel("Time period", fontsize=12)
    plt.ylabel("Deaths", fontsize=12) 
    plt.xticks(xs, xlabels, rotation='vertical')
    plt.tight_layout(pad=2.0)
    plt.plot(xs, ys, linewidth=5)
    plt.savefig(os.path.join(plot_dir, plot_file))
    plt.show()
    plt.close()
    
    print("\nPlot saved in plots folder as '" + plot_file + "'.")
