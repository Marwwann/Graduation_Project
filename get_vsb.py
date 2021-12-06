# This function takes the desired VSB values from the user and through string manipulation it
# extractes a list of the desired VSB values.
# The function supports using a vector of VSB values or discrete values
# The function return a vector of the needed VSB values and a list of the VSB values as strings and a list of
# the used units
# This function was written on 31/1/2020


import re
import numpy as np


def get_vsb(vsb):
    list_vsb = []
    list_range = []
    list_1 = []
    units = ['m', 'u']
    vsb_final = ''
    used_unit = []
    # Strip the input length vector from the length units

    for i in vsb:
        if i in units:
            used_unit.append(i)
        else:
            vsb_final = vsb_final + i

    # Colon detection
    # Here it searches for a colon, if detected it creates an array of the desired values then
    # converts it to a string

    if vsb_final.find(':') != -1:
        list_1 = re.split(':', vsb_final)
        list_range = np.arange(float(list_1[0]), float(list_1[2]) + 0.00001, float(list_1[1]))
        dummy_var = str(list_range).strip('[]')
        list_vsb = dummy_var.split()

    # Here if the length values are discrete, list of strings of those values is returned

    else:
        list_vsb = vsb_final.split()
        list_range = [float(i) for i in list_vsb]
    return list_vsb, used_unit, list_range
