#Lookup VGS Function
#by Marwan Mohamed Ali, Faculty of Engineering-Ain Shams University.
#This code was originally written by Professor Borris Murmann in MATLAB language









import numpy as np
from scipy.interpolate import interpn
mosData = None
import pickle
from numpy import arange
import sys
from GmIdKit.lookupMos import lookup
from GmIdKit import techsweep_run
from scipy.interpolate import interp1d


def lookup_VGS(mosData, *outVars, **inVars):

    defaultL = min(mosData.L)
    defaultVGS = mosData.VGS
    defaultVDS = max(mosData.VDS) / 2
    defaultVSB = 0
    defaultVGB = None
    defaultVGD = None

# There are two basic usage scenarios:
#(1) Lookup VGS with known voltage at the source terminal
#(2) Lookup VGS with unknown source voltage, e.g. when the source of the
#    transistor is the tail node of a differential pair

    varNames = [key for key in inVars.keys()]
    #print(varNames)
    if 'VGB' in varNames and 'VGD' in varNames:
        mode = 2
    elif 'VGB' not in varNames and 'VGD' not in varNames:
        mode = 1
    else:
        print('Invalid syntax or usage mode!')
        output = []


    if 'VDS' in varNames:
        VDS = inVars['VDS']
        #print(VDS)
    if 'VSB' in varNames:
        VSB = inVars['VSB']
        #print(VSB)
    if 'L' in varNames:
        L = inVars['L']
        #print(L)


    # Check whether GM_ID or ID_W was passed to function
    if 'ID/W' in outVars:
        ratio_string = 'ID/W'
        ID_W_idx = outVars.index('ID/W')
        ID_W_value_idx = ID_W_idx + 1
        ID_W = outVars[ID_W_value_idx]
        ratio_data = ID_W
    elif 'GM/ID' in outVars:
        ratio_string = 'GM/ID'
        GM_ID_idx = outVars.index('GM/ID')
        GM_ID_value_idx = GM_ID_idx + 1
        GM_ID = outVars[GM_ID_value_idx]
        ratio_data = GM_ID
    if type(ratio_data) == np.ndarray or type(ratio_data) == list:
        max_ratio_data = max(ratio_data)
    elif type(ratio_data) == int:
        max_ratio_data = ratio_data
    else:
        print('look_upVGS: Invalid syntax or usage mode!')


    if type(ratio_data) == int:
        len_ratio_data = 1
    else:
        len_ratio_data = len(ratio_data)


    if mode == 1:
        VGS = mosData.VGS
        ratio = lookup(mosData, ratio_string)
        #print(ratio.shape)
        #print(ratio)
    else:
        step = mosData.VGS[0] - mosData.VGS[1]
        print(step)
        VSB = np.transpose(np.arange(max(mosData.VSB), min(mosData.VSB) + step, step).reshape((len(mosData.VSB), 1), int))
        print(VSB)
        VGS = mosData.VGB - VSB
        VDS = mosData.VDB - VSB
        ratio = lookup(mosData, ratio_string, VGS=VGS, VDS=VDS, VSB=VSB, L=np.ones((len(VSB), 1), dtype=int)*mosData.L)
        idx = np.isfinite(ratio)
        ratio = ratio[idx]
        VGS = VGS[idx]

    len_L = len(L) if type(L) == np.ndarray or type(L) == list else 1

    if len_L > 1:

        ratio = np.swapaxes(ratio, 0, 1)

    s = np.shape(ratio)
    #print(len(s))
    if len(s) == 1:
        output = np.empty([s[0], len_ratio_data])
        for i in range(s[0]):
            if len(ratio.shape) == 1:
                ratio_range = ratio
            else:
                ratio_range = ratio[:][i]
                #print(ratio_range)
            # print(ratio_range)
            VGS_range = VGS
            #print(VGS)
            if ratio_string == 'GM/ID':
                m = max(ratio_range)
                pre_idx = np.where(ratio_range == m)
                idx = pre_idx[0]
                #print(idx)
                VGS_range = VGS_range[idx[0]:]
                ratio_range = ratio_range[idx[0]:]
                if max_ratio_data > m:
                    print('look_upVGS: GM/ID input larger than maximum!')
            interpolation_fn = interp1d(ratio_range, VGS_range, bounds_error=False, fill_value='extrapolate')
            output[i, :] = interpolation_fn(ratio_data)
            output = output[:]

    else:
        output = np.empty([s[1], len_ratio_data])
        for i in range(s[1]):
            ratio_range = ratio[:][i]
            # print(ratio_range)
            VGS_range = VGS
            if ratio_string == 'GM/ID':
                m = max(ratio_range)
                pre_idx = np.where(ratio_range == m)
                idx = pre_idx[0]
                VGS_range = VGS_range[idx:]
                ratio_range = ratio_range[idx:]
                if max_ratio_data > m:
                    print('look_upVGS: GM/ID input larger than maximum!')
            interpolation_fn = interp1d(ratio_range, VGS_range, bounds_error=False, fill_value='extrapolate')
            output[i, :] = interpolation_fn(ratio_data)
            output = output[:]

    #print(output)




    return output



with open("nch 130nm_bulk", "rb") as f:
    nch2 = pickle.load(f)

    y = lookup_VGS(nch2, 'GM/ID', 10, VDS=0.6, VSB=0.1, L=0.1)
#print(y)
a = np.squeeze(y)
print(a.shape)


#import matplotlib.pyplot as plt
#plt.plot(arange(4, 20, 0.2), arange(1, 81), 'o')
#plt.plot(arange(4,20,0.2), y[2], 'x')
#plt.show()





#The current problem is that max() deals only with 1-D while ratio_range is 3-D