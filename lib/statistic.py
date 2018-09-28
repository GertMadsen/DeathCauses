'''
    Functions to be used in order to analyze csv file. 
'''

from collections import Counter
import lib.plotting as plotting

def find_most_death(data_set, year, cause):
    state = ""
    max = 0
    for data in data_set:
        if data[0] == year and data[1] == cause:
            if data[3] > max:
                max = data[3]
                state = data[2]
    return f"\nIn {year} {state} has most deaths caused by '{cause}' with {max} deaths."

def find_least_death(data_set, year, cause):
    state = ""
    min = 1000000
    for data in data_set:
        if data[0] == year and data[1] == cause:
            if data[3] < min:
                min = data[3]
                state = data[2]
    return f"\nIn {year} {state} has the least deaths caused by '{cause}' with {min} deaths."


def find_inc(data_set, start_year, end_year, cause):
    state_dict = {}
    for data in data_set:
        state_dict.setdefault(data[2], 0)
        if data[0] == end_year and data[1] == cause:
            state_dict[data[2]] += data[3]
        if data[0] == start_year and data[1] == cause:
            state_dict[data[2]] -= data[3]
    return state_dict

def find_most_inc(data_set, start_year, end_year, cause):
    state_dict = Counter(find_inc(data_set, start_year, end_year, cause)).most_common()
    state = state_dict[0][0]
    increase = state_dict[0][1]
    plotting.plot_inc_by_year(data_set,state, cause, start_year, end_year)
    return f"\nFrom {start_year} to {end_year}, {state} has the highest increase in deaths with a {increase} increase in deaths caused by '{cause}'"
    
def find_least_inc(data_set, start_year, end_year, cause):
    state_dict = Counter(find_inc(data_set, start_year, end_year, cause)).most_common()
    remove_list = []
    for element in state_dict:
        if element[1] < 0:
            remove_list.append(element)
    for item in remove_list:
        state_dict.remove(item)
    state = state_dict[-1][0]
    increase = state_dict[-1][1]
    return f"\nFrom {start_year} to {end_year}, {state} has the smallest increase in deaths with a {increase} increase in deaths caused by '{cause}'"

