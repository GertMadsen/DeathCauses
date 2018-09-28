'''
    Create plots to be stored in files 
'''

import matplotlib.pyplot as plt
import numpy as np
import os

def plot_inc_by_year(data_set, state, cause, start_year, end_year):
    years = range(start_year, end_year+1)     

    death_arr = [data[3] for year in years for data in data_set if data[0] == year and data[2] == state and data[1] == cause]                    
    
    end_years = np.array(death_arr[1:])
    start_years = np.array(death_arr[:-1])
    increase_arr = end_years - start_years
    
    plot_file = f'Annual_death_increase_for_{cause}_in_{state}.png'
    script_dir = os.path.dirname(__file__)
    plot_dir = os.path.join(script_dir, '..', 'plots/')
    if not os.path.isdir(plot_dir):
        os.makedirs(plot_dir)

    xs = years[1:]
    ys = increase_arr
    xlabels = [f'{year}-{year+1}' for year in years]
    
    plt.title(f"Annual increase in deaths for\n '{cause}' in '{state}'", fontsize=14)
    plt.xlabel("Time period", fontsize=12)
    plt.ylabel("Deaths", fontsize=12) 
    plt.xticks(xs, xlabels, rotation='vertical')
    plt.tight_layout(pad=2.0)
    plt.plot(xs, ys, linewidth=5)
    plt.savefig(plot_dir + plot_file)
    plt.show()
    plt.close()
    
    print("\nPlot saved in plots folder as '" + plot_file + "'.")
