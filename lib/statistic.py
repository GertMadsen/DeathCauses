'''
    Functions to be used in order to analyze csv file. 
'''

from collections import Counter
import lib.plotting as plotting

def find_most_death(data_set, year, cause):
    state = ""
    max = 0
    for data in data_set:
        # We look at the data set in order to find a match in year and cause
        if data[0] == year and data[1] == cause:
            # In case of a match we check if the number of death for this state is higher than a previously
            # recorded maximum. If this is the case, this number of death becomes the new max and we register
            # the correspondng state.
            if data[3] > max:
                max = data[3]
                state = data[2]
    return f"\nIn {year} {state} has most deaths caused by '{cause}' with {max} deaths."

def find_least_death(data_set, year, cause):
    state = ""
    min = 0
    for data in data_set:
        # We check for a match in cause and year
        if data[0] == year and data[1] == cause:
            # In case of a match we check if the number of death for this state is lower than a previously
            # recorded maximum. If this is the case, this number of death becomes the new min and we register
            # the correspondng state.
            # The check if min is 0 is to ensure that a start minimum is assigned other than 0.
            if data[3] < min or min == 0:
                min = data[3]
                state = data[2]
    return f"\nIn {year} {state} has the least deaths caused by '{cause}' with {min} deaths."

def find_most_inc(data_set, start_year, end_year, cause):
    # After using the find_inc function to make a dictionary with the increases in death for all states,
    # we then use the most common method in the Counter Class from the collection library to sort the dict.
    state_dict = Counter(find_inc(data_set, start_year, end_year, cause)).most_common()
    # The first key,value pair in this newly sorted dict will then be the state with the highest increase in deaths
    state = state_dict[0][0]
    increase = state_dict[0][1]
    plotting.plot_inc_by_year(data_set,state, cause, start_year, end_year)
    return f"\nFrom {start_year} to {end_year}, {state} has the highest increase in deaths with a {increase} increase in deaths caused by '{cause}'"
    
def find_least_inc(data_set, start_year, end_year, cause):
    # Again we use the find_inc function to make a dictionary with the increases in death for all states.
    # And after that we then use the most common method in the Counter Class from the collection library to sort the dict.
    state_dict = Counter(find_inc(data_set, start_year, end_year, cause)).most_common()
    # We think that a negative increase is not an increase - but a decrease.
    # Therefore we decided to clean the dict for all negative values.
    # So first we find all negative values an add them to a remove_list
    remove_list = []
    for element in state_dict:
        if element[1] < 0:
            remove_list.append(element)
    # The we iterate through this list and remove all elements from our remove_list from the dict
    for item in remove_list:
        state_dict.remove(item)
    # Since the list was previously sorted, we can now look at the last key,value pair and this must be the state
    # with the lowest increase in death. The [-1] notation returns the last key,value pair in a dict.
    state = state_dict[-1][0]
    increase = state_dict[-1][1]
    return f"\nFrom {start_year} to {end_year}, {state} has the smallest increase in deaths with a {increase} increase in deaths caused by '{cause}'"

# This function finds the annual increase in death between two years for every state
# and stores this in a dictionary where the states are keys and numbers of death are values
def find_inc(data_set, start_year, end_year, cause):
    state_dict = {}
    for data in data_set:
        state_dict.setdefault(data[2], 0)
        if data[0] == end_year and data[1] == cause:
            state_dict[data[2]] += data[3]
        if data[0] == start_year and data[1] == cause:
            state_dict[data[2]] -= data[3]
    return state_dict
