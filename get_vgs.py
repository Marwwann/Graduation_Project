# This function takes the desired length values from the users and through string manipulation it
# extractes a list of the desired VGS values.
# The function supports using a vector of lengths or discrete values
# The function return a vector of the needed length, a list of the lengths as strings and a list of
# the used units
# This function was written on 31/1/2020


import re
import numpy as np

def get_vgs(vgs):

    list_vgs = []
    list_range = []
    list_1 = []
    units = ['m', 'u', 'n']
    vgs_final = ''
    used_unit = []
    # Strip the input length vector from the length units

    for i in vgs:
        if i in units:
            used_unit.append(i)
        else:
            vgs_final = vgs_final + i
    print(type(vgs_final[0]))
    # Colon detection
    # Here it searches for a colon, if detected it creates an array of the desired values then
    # converts it to a string

    if vgs_final.find(':') != -1:
        list_1 = re.split(':', vgs_final)
        #print(list_1)
        list_range = np.arange(float(list_1[0]), float(list_1[2]) + 0.00001, float(list_1[1]))
        #print(type(list_range))
        #print(type(list_range[0]))
        dummy_var = str(list_range).strip('[]')
        list_vgs = dummy_var.split()
        #print(list_length)
    # Here if the length values are discrete, list of strings of those values is returned

    else:
        list_vgs = vgs_final.split()
        list_range = [float(i) for i in list_vgs]

    return list_vgs, used_unit, list_range

#x, y, z = get_vgs('0:0.2:1')
#print(type(x))
#print(type(z[0]))
#print(z)
#z = np.arange(0.1, 1.1 + 0.5, 0.5)
#print(z)

#x, y, z = get_vgs('0 0.2 1 8')
#print(z)
#print(x# )

