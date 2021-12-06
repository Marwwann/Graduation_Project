# This function takes the desired length values from the users and through string manipulation it
# extractes a list of the desired VDS values.
# The function supports using a vector of lengths or discrete values
# The function return a vector of the needed length, a list of the lengths as strings and a list of
# the used units
# This function was written on 31/1/2020


import re
import numpy as np

def get_vds(vds):

    list_vds = []
    list_range = []
    list_1 = []
    units = ['m', 'u', 'n']
    vds_final = ''
    used_unit = []
    # Strip the input length vector from the length units

    for i in vds:
        if i in units:
            used_unit.append(i)
        else:
            vds_final = vds_final + i

    # Colon detection
    # Here it searches for a colon, if detected it creates an array of the desired values then
    # converts it to a string

    if vds_final.find(':') != -1:
        list_1 = re.split(':', vds_final)
        #print(list_1)
        list_range = np.arange(float(list_1[0]), float(list_1[2]) + 0.00001, float(list_1[1]))
        #print(type(list_range))
        #print(type(list_range[0]))
        dummy_var = str(list_range).strip('[]')
        list_vds = dummy_var.split()
        #print(list_length)
    # Here if the length values are discrete, list of strings of those values is returned

    else:
        list_vds = vds_final.split()
        list_range = [float(i) for i in list_vds]
    return list_vds, used_unit, list_range

#x, y, z = get_vds('0:0.2:1')
#print(type(x))
#print(type(z[0]))
#print(z)
#z = np.arange(0.1, 1.1 + 0.5, 0.5)
#print(z)

#x, y, z = get_vds('0 0.2 1 8')
#print(z)
#print(x)
