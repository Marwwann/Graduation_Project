import os
import matplotlib.pyplot as plt
import numpy as np
from GmIdKit import read_raw
from decimal import Decimal
from decimal import ROUND_UP
from scipy.interpolate import interp1d
from get_capacitance import get_cap

def num_count(inp_num):
    input_num = int(inp_num)

    count = 0
    while input_num > 0:
        count += 1
        input_num //= 10

    return count


def dip_dop(model_path, netlist_path, vdd_net, gnd_net, vinn, vinp, voutn, voutp, VDD_in, VINCM_in, cap_in, start_freq_in, stop_freq_in, no_points_in):
    with open(netlist_path, 'r') as f:
        sub_circuit = f.read()
    f.close()
    with open(model_path, 'r') as f:
        model_file = f.read()
    f.close()
    VINCM = VINCM_in
    VDD = VDD_in

    cap = cap_in

    start_freq = start_freq_in
    stop_freq = stop_freq_in
    no_points = no_points_in

    netlist = f''' 
.TITLE 5T-OTA USING NMOS

.INCULDE {model_path}


{sub_circuit}

V3 {vinp} {gnd_net} dc {VINCM} ac 1 
V4 {vinn} {gnd_net} dc {VINCM} ac -1
V5 {vdd_net} {gnd_net} dc {VDD}
C1 {voutp} {gnd_net} {cap}
C2 {voutn} {gnd_net} {cap}
X1 {vinp} {vinn} {vdd_net} {gnd_net} {voutp} {voutn} dip_dop


.save vdb({voutp}) vdb({voutn})
.ac dec {no_points} {start_freq} {stop_freq}



.probe
.end'''

    with open('trial1.txt', 'w+') as f:
        f.write(netlist)
    f.close()

    os.system('ngspice.exe -b -r result.raw trial1.txt')

    out_file = "result.raw"

    darr, mda = read_raw.rawread(out_file)
    frequency = [i[0] for i in darr[0]]
    voltage_1 = [i[1] for i in darr[0]]
    voltage_2 = [i[2] for i in darr[0]]
    #print(frequency[80])
    #print(np.real(voltage_2[79]))
    #print(np.real(voltage_2[80]))
    #print(np.real(voltage_2[81]))
    x_1 = np.real(frequency)

    y_1 = np.real(voltage_1)
    y_2 = np.real(voltage_2)
    listed_y_1 = list(y_1)
    #print(np.abs(listed_y_1))
    #print(np.log10(np.abs(listed_y_1)))
    #print(x_1[list(np.log10(np.abs(listed_y_1))).index(-3.926265282769164)])
    listed_y_2 = list(y_2)
    #print(y_1, y_2)
    #y_subtract = np.abs(np.subtract(listed_y_1, listed_y_2))
    #print(y_subtract)

    y = 20 * np.log10(np.abs(listed_y_1))
    #print(y)

    listed_y = list(y)
    #listed_x = list(x)
    # Gain calculation
    gain = Decimal(max(y)).quantize(Decimal('.01'), rounding=ROUND_UP)
    unit_gain = ' dB'
    # Bandwidth calculation
    bandwidth_voltage = gain - 3
    int_bandwidth_voltage = float(bandwidth_voltage)
    interpolation_fn_fr = interp1d(listed_y, x_1)
    pre_bandwidth = interpolation_fn_fr(int_bandwidth_voltage)
    num_digits = num_count(pre_bandwidth)

    bandwidth_non_d = 0
    unit_BW = ''

    if num_digits <= 3:
        bandwidth_non_d = pre_bandwidth
    elif num_digits > 3 and num_digits <= 6:
        bandwidth_non_d = pre_bandwidth / 10 ** 3
        unit_BW = ' KHz'
    elif num_digits > 6 and num_digits <= 9:
        bandwidth_non_d = pre_bandwidth / 10 ** 6
        unit_BW = ' MHz'
    elif num_digits > 9 and num_digits <= 12:
        bandwidth_non_d = pre_bandwidth / 10 ** 9
        unit_BW = ' GHz'
    else:
        bandwidth_non_d = pre_bandwidth / 10 ** 12
        unit_BW = ' THz'

    bandwidth = Decimal(bandwidth_non_d).quantize(Decimal('.01'), rounding=ROUND_UP)

    # Unity Gain Frequency Calculation
    pre_UGF = interpolation_fn_fr(0)

    num_digits_UGF = num_count(pre_UGF)
    UGF_non_d = 0
    unit_UGF = ''

    if num_digits_UGF <= 3:
        UGF_non_d = pre_UGF
    elif num_digits_UGF > 3 and num_digits_UGF <= 6:
        UGF_non_d = pre_UGF / 10 ** 3
        unit_UGF = ' KHz'
    elif num_digits_UGF > 6 and num_digits_UGF <= 9:
        UGF_non_d = pre_UGF / 10 ** 6
        unit_UGF = ' MHz'
    elif num_digits_UGF > 9 and num_digits_UGF <= 12:
        UGF_non_d = pre_UGF / 10 ** 9
        unit_UGF = ' GHz'
    else:
        UGF_non_d = pre_UGF / 10 ** 12
        unit_UGF = ' THz'

    UGF = Decimal(UGF_non_d).quantize(Decimal('.01'), rounding=ROUND_UP)


    netlist_2 = f''' 
.TITLE 5T-OTA USING NMOS

.INCULDE {model_path}


{sub_circuit}

V3 {vinp} {gnd_net} dc {VINCM} ac 1 
V4 {vinn} {gnd_net} dc {VINCM} ac 1
V5 {vdd_net} {gnd_net} dc {VDD}
C1 {voutp} {gnd_net} {cap}
C2 {voutn} {gnd_net} {cap}
X1 {vinp} {vinn} {vdd_net} {gnd_net} {voutp} {voutn} dip_dop


.save vdb({voutp}) vdb({voutn})
.ac dec {no_points} {start_freq} {stop_freq}




.probe
.end'''


    with open('trial1_CM.txt', 'w+') as f:
        f.write(netlist_2)
    f.close()

    os.system('ngspice.exe -b -r result2.raw trial1_CM.txt')

    out_file = "result2.raw"

    darr, mda = read_raw.rawread(out_file)


    voltage_1_CM = [i[1] for i in darr[0]]
    voltage_2_CM = [i[2] for i in darr[0]]

    #print(voltage_1_CM, voltage_2_CM)
    #x_1_CM = np.real(frequency_CM)
    # x = np.log10(x_1)

    y_1_CM = np.real(voltage_1_CM)
    y_2_CM = np.real(voltage_2_CM)
    # print(y_1_CM)
    listed_y_1_CM = list(y_1_CM)
    listed_y_2_CM = list(y_2_CM)
    # print(y_1, y_2)
    #y_subtract_CM = np.abs(np.subtract(listed_y_1_CM, listed_y_2_CM))
    y_CM = 20 * np.log10(np.abs(listed_y_1_CM))
    #print(y_CM)
    # listed_y = list(y)
    # listed_x = list(x)

    # Common Mode Gain calculation
    CM_gain = Decimal(max(y_CM)).quantize(Decimal('.01'), rounding=ROUND_UP)
    CM_unit_gain = ' dB'

    CMRR = gain - CM_gain


    result = [gain, unit_gain, bandwidth, unit_BW, UGF, unit_UGF, CM_gain, x_1, y, y_CM, CMRR]

    return result

#cap = get_cap('1p:1p:4p')

#for i in range(len(cap)):


#x = dip_dop('D:\\Grad_Project\\Github\\task5\\130nm_bulk.LIB', 'D:\\Grad_Project\\Github\\task5\\MODELS\\dipdop.txt', '3', '0', '1',
#            '2', '5', '7', '1.2', '730m', '1p', '1', '10G', '10')
#print(list(x[7]).index(100000000.00000052))
#print(x[8])
'''
print('The differential gain of the 5T-OTA is: ' + str(x[0]) + str(x[1]))
print('The bandwidth of the 5T-OTA is: ' + str(x[2]) + str(x[3]))
print('The unity gain frequency of the 5T-OTA is: ' + str(x[4]) + str(x[5]))
print('The common mode gain of the 5T-OTA is: ' + str(x[6]) + str(x[1]))
print('The common mode rejection ratio of the 5T-OTA is: ' + str(x[10]) + str(x[1]))

plt.figure(1)
plt.plot(x[7], x[8])
plt.xscale('log')
#plt.legend()
plt.grid()
plt.xlabel('Frequnecy (Hz)')
plt.ylabel('Avd')


plt.figure(2)
plt.plot(x[7], x[9])
plt.xscale('log')
#plt.legend()
plt.grid()
plt.xlabel('Frequnecy (Hz)')
plt.ylabel('AvCM')

plt.show()
# input()"""
'''