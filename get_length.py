# This function takes the desired length values from the users and through string manipulation it
# extractes a list of the desired length values.
# The function supports using a vector of lengths or discrete values
# The function return a vector of the needed length and a list of the lengths as strings and a list of
# the used units
# This function was written on 31/1/2020


import re
import numpy as np

def get_length(Length):

    list_length = []
    list_range = []
    list_1 = []
    units = ['m', 'u', 'n']
    length_final = ''
    used_unit = []
    # Strip the input length vector from the length units

    for i in Length:
        if i in units:
            used_unit.append(i)
        else:
            length_final = length_final + i

    # Colon detection
    # Here it searches for a colon, if detected it creates an array of the desired values then
    # converts it to a string

    if length_final.find(':') != -1:
        list_1 = re.split(':', length_final)
        #print(list_1)
        list_range = np.arange(float(list_1[0]), float(list_1[2]) + 0.00001, float(list_1[1]))
        #print(type(list_range))
        #print(type(list_range[0]))
        dummy_var = str(list_range).strip('[]')
        list_length = dummy_var.split()
        #print(list_length)
    # Here if the length values are discrete, list of strings of those values is returned

    else:
        list_length = length_final.split()
        list_range = [float(i) for i in list_length]
    return list_length, used_unit, list_range


#x, y, z = get_length('0.1u:0.5u:1.1u')
#print(type(x))
#print(type(z[0]))
#print(z)
#z = np.arange(0.1, 1.1 + 0.5, 0.5)
#print(z)

