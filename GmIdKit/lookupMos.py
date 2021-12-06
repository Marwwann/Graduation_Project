import numpy as np
from scipy.interpolate import interpn


mosDat = None
import pickle
from numpy import arange
import sys


def lookup(mosDat, *outVars, **inVars):
    '''Main lookup function'''

    defaultL = min(mosDat.L)
    defaultVGS = mosDat.VGS
    defaultVDS = max(mosDat.VDS) / 2
    defaultVSB = 0

    # Figure out the mode of operation and the requested output arguments.
    # Mode 1 : Just one variable requested as output.
    # Mode 2 : A ratio or product of variables requested as output.
    # Mode 3 : Two ratios or products of variables requested as output.
    mode = 1
    outVarList = []
    #print(len(outVars))
    #print(len(inVars))
    if len(outVars) == 2:
        mode = 3
        for outVar in outVars:
            if type(outVar) == str:
                if (outVar.find('/') != -1):
                    pos = outVar.find('/')
                    outVarList.append(outVar[:pos].upper())
                    outVarList.append(outVar[pos])
                    outVarList.append(outVar[pos+1:].upper())
                elif (outVar.find('*') != -1):
                    pos = outVar.find('*')
                    outVarList.append(outVar[:pos].upper())
                    outVarList.append(outVar[pos])
                    outVarList.append(outVar[pos+1:].upper())
                else:
                    print("ERROR: Outputs requested must be a ratio or product of variables")
                    return None
            else:
                print("ERROR: Output variables must be strings!")
                return None
    elif len(outVars) == 1:
        outVar = outVars[0]
        if type(outVar) == str:
            if outVar.find('/') == -1 and outVar.find('*') == -1:
                mode = 1
                outVarList.append(outVar.upper())
            else:
                mode = 2
                if outVar.find('/') != -1:
                    pos = outVar.find('/')
                    outVarList.append(outVar[:pos].upper())
                    outVarList.append(outVar[pos])
                    outVarList.append(outVar[pos+1:].upper())
                elif outVar.find('*') != -1:
                    pos = outVar.find('*')
                    outVarList.append(outVar[:pos].upper())
                    outVarList.append(outVar[pos])
                    outVarList.append(outVar[pos+1:].upper())
        else:
            print("ERROR: Output variables must be strings!")
            return None
    else:
        print("ERROR: No output variables specified")
        return None

    # Figure out the input arguments. Set to default those not specified.
    varNames = [key for key in inVars.keys()]

    for varName in varNames:
        if not varName.isupper():
            print("ERROR: Keyword args must be upper case. Allowed arguments: L, VGS, VDS and VSB.")
            return None
        if varName not in ['L', 'VGS', 'VDS', 'VSB', 'RANGE']:
            print("ERROR: Invalid keyword arg(s). Allowed arguments: RANGE, L, VGS, VDS and VSB.")
            return None

    L = defaultL
    VGS = defaultVGS
    VDS = defaultVDS
    VSB = defaultVSB

    if 'L' in varNames:
        L = inVars['L']
    if 'VGS' in varNames:
        VGS = inVars['VGS']
    if 'VDS' in varNames:
        VDS = inVars['VDS']
    if 'VSB' in varNames:
        VSB = inVars['VSB']


    #print(VGS)
    #print(VDS)
    #print(VSB)
    #print(L)
    #print(type(L))

    xdata4DRaw = None
    ydata4DRaw = None

    # Extract the data that was requested
    if (mode == 1):
        ydata4DRaw = eval("mosDat.{}".format(outVarList[0]))
    elif (mode == 2 or mode == 3):
        ydata4DRaw = eval(("mosDat.{}" + outVarList[1] + "mosDat.{}").format(outVarList[0], outVarList[2]))
        if (mode == 3):
            xdata4DRaw = eval(("mosDat.{}" + outVarList[4] + "mosDat.{}").format(outVarList[3], outVarList[5]))

    # Change Data Type
    xdata = np.array(xdata4DRaw)
    ydata = np.array(ydata4DRaw)

    #print(xdata.shape)
    #print('ydata is ', ydata)



    vsbf = np.array(mosDat.VSB)
    #print(vsbf)
    vdsf = np.array(mosDat.VDS)
    #print(max(vdsf))
    vgsf = np.array(mosDat.VGS)
    #print(vgsf)
    lf = np.array(mosDat.L)
    #print(lf)

    message_flag = 0

    if type(L) == float or type(L) == int:
        if L <= max(lf):
            L = L
        else:
            L = max(lf)
            print('The specified length was larger than the previously specified, the maximum allowed length was used.')
        L = [L]

    if type(L) == list:
        L1 = []
        for i in L:
            if i <= max(lf):
                L1.append(i)
        L = L1
    print(L)
    # Interpolate for the input variables provided
    if (mosDat.TYPE == 'nmos'):
        # points = ( -mosDat['VSB'][0], mosDat['VDS'][0], mosDat['VGS'][0], mosDat['L'][0])
        points = (lf, vsbf, vgsf, vdsf)
    else:
        # points = ( mosDat['VSB'][0], -mosDat['VDS'][0], -mosDat['VGS'][0], mosDat['L'][0])
        points = (lf, vsbf, -vgsf, -vdsf)

    xi_mesh = np.array(np.meshgrid(L, VSB, VGS, VDS))
    #print('xi_mesh is: ', xi_mesh.shape)
    xi = np.rollaxis(xi_mesh, 0, 5)
    #print('xi at rollaxis is:', xi.shape)
    xi = xi.reshape(xi_mesh.size // 4, 4)
    #print('xi final is: ', xi.shape)
    result = None
    len_VSB = len(VSB) if type(VSB) == np.ndarray or type(VSB) == list else 1
    len_VDS = len(VDS) if type(VDS) == np.ndarray or type(VDS) == list else 1
    len_VGS = len(VGS) if type(VGS) == np.ndarray or type(VGS) == list else 1
    len_L = len(L) if type(L) == np.ndarray or type(L) == list else 1

    if mode == 1 or mode == 2:
        result = np.squeeze(interpn(points, ydata, xi, method='linear', bounds_error=True, fill_value=None).reshape(len_L, len_VSB, len_VGS, len_VDS))
    elif mode == 3:
        x_interpolated = interpn(points, xdata, xi, method='linear', bounds_error=True, fill_value=None).reshape(len_L, len_VSB, len_VGS, len_VDS)
        #print('x interpolated is: ', x_interpolated.shape)
        y_interpolated = interpn(points, ydata, xi, method='linear', bounds_error=True, fill_value=None).reshape(len_L, len_VSB, len_VGS, len_VDS)
        #print('y interpolated is: ', y_interpolated)

        x = np.squeeze(np.transpose(x_interpolated, (2, 0, 3, 1)))
        #print('x is: ', x)
        y = np.squeeze(np.transpose(y_interpolated, (2, 0, 3, 1)))
        #print('y is: ', y)
        if "RANGE" not in varNames:
            print("ERROR: you must specify x axis RANGE in mode3 ex: range=...")
            return None

        x_wanted = inVars['RANGE']
        #print('X wanted is: ', x_wanted)
        x = np.expand_dims(x, 1) if np.ndim(x) == 1 else x
        print('x_new is: ', x)
        #print(x.shape)
        y = np.expand_dims(y, 1) if np.ndim(y) == 1 else y
        #print('y_new is: ', y)
        LListLength = np.shape(x)[1]  # length of Length Dimension
        #print(LListLength)
        result = np.zeros(shape=(LListLength, len(x_wanted)))

        for i in range(0, LListLength):
            for j in range(0, len(x_wanted)):
                mx = max(x[:, i])
                print('max is: ', mx)
                mxIndex = np.argmax(x[:, i])
                print('X wanted at j is: ', x_wanted[j])
                if x_wanted[j] > mx:
                    print("warning input greater than maximum")
                if outVarList[3].upper() == "GM" and outVarList[5].upper() == "ID":
                    x_right = x[:mxIndex:-1, i]
                    y_right = y[:mxIndex:-1, i]
                    print('x right is: ', x_right, '\n', 'Y right is: ', y_right)
                    result[i, j] = np.squeeze(interpn((x_right,), y_right, [x_wanted[j]], method='linear', bounds_error=True, fill_value=None))
                    #print('The result is: ', result)
                elif outVarList[3].upper() == "GM" and (outVarList[5].upper() == "CGG" or outVarList[5].upper() == "CGS"):
                    x_left = x[0:mxIndex, i]
                    y_left = y[0:mxIndex, i]
                    result[i, j] = np.squeeze(interpn(x_left, y_left, x_wanted[j], method='linear', bounds_error=True, fill_value=None).reshape(len_VGS, len_L))
                else:
                    result[i, j] = np.squeeze(interpn(x[:, i], y[:, i], x_wanted[j], method='linear', bounds_error=False, fill_value=None).reshape(len_VGS, len_L))


        #print("ERROR: Mode 3 not supported yet :-(")

    # Return the result
    return result



with open("..\\nch 130nm_bulk", "rb") as f:
    nch2 = pickle.load(f)

y = lookup(nch2, "ID/W", "GM/ID", L=[0.25, 0.5, 0.75, 1, 1.25], RANGE=arange(4, 25, 0.4))

#print('y is: ', y)


#import matplotlib.pyplot as plt


#plt.plot(arange(4,20,0.2), y[1], 'o')
#plt.plot(arange(4,20,0.2), y[2], 'x')
#plt.show()


