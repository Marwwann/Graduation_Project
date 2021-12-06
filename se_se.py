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


def se_se(model_path, netlist_path, vdd_net, gnd_net, vin, vout, VDD_in, VIN_in_DC, cap_in, start_freq_in, stop_freq_in, no_points_in):
    with open(netlist_path, 'r') as f:
        sub_circuit = f.read()
    f.close()

    VINCM = VIN_in_DC
    VDD = VDD_in

    cap = cap_in

    start_freq = start_freq_in
    stop_freq = stop_freq_in
    no_points = no_points_in

    netlist = f''' .TITLE 5T-OTA USING NMOS

    .INCULDE {model_path}


    {sub_circuit}

    V3 {vin} {gnd_net} dc {VINCM} ac 1 
    V5 {vdd_net} {gnd_net} dc {VDD}
    C1 {vout} {gnd_net} {cap}
    X1 {vin} {vdd_net} {gnd_net} {vout} se_se


    .save vdb({vout})
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
    voltage = [i[1] for i in darr[0]]

    x_1 = np.real(frequency)
    x = np.log10(x_1)

    y_1 = np.abs(voltage)
    y = 20 * np.log10(y_1)

    listed_y = list(y)
    listed_x = list(x)

    # Gain calculation
    gain = Decimal(max(y)).quantize(Decimal('.01'), rounding=ROUND_UP)
    unit_gain = ' dB'

    # Bandwidth calculation
    bandwidth_voltage = gain - 3
    int_bandwidth_voltage = float(bandwidth_voltage)
    interpolation_fn_fr = interp1d(listed_y, listed_x)

    pre_bandwidth = interpolation_fn_fr(int_bandwidth_voltage)
    bandwidth_freq = 10 ** (pre_bandwidth)

    num_digits = num_count(bandwidth_freq)

    bandwidth_non_d = 0
    unit_BW = ''

    if num_digits <= 3:
        bandwidth_non_d = bandwidth_freq
    elif num_digits > 3 and num_digits <= 6:
        bandwidth_non_d = bandwidth_freq / 10 ** 3
        unit_BW = ' KHz'
    elif num_digits > 6 and num_digits <= 9:
        bandwidth_non_d = bandwidth_freq / 10 ** 6
        unit_BW = ' MHz'
    elif num_digits > 9 and num_digits <= 12:
        bandwidth_non_d = bandwidth_freq / 10 ** 9
        unit_BW = ' GHz'
    else:
        bandwidth_non_d = bandwidth_freq / 10 ** 12
        unit_BW = ' THz'

    bandwidth = Decimal(bandwidth_non_d).quantize(Decimal('.01'), rounding=ROUND_UP)

    # Unity Gain Frequency Calculation
    pre_UGF = interpolation_fn_fr(0)

    UGF_freq = 10 ** (pre_UGF)

    num_digits_UGF = num_count(UGF_freq)
    UGF_non_d = 0
    unit_UGF = ''

    if num_digits_UGF <= 3:
        UGF_non_d = UGF_freq
    elif num_digits_UGF > 3 and num_digits_UGF <= 6:
        UGF_non_d = UGF_freq / 10 ** 3
        unit_UGF = ' KHz'
    elif num_digits_UGF > 6 and num_digits_UGF <= 9:
        UGF_non_d = UGF_freq / 10 ** 6
        unit_UGF = ' MHz'
    elif num_digits_UGF > 9 and num_digits_UGF <= 12:
        UGF_non_d = UGF_freq / 10 ** 9
        unit_UGF = ' GHz'
    else:
        UGF_non_d = UGF_freq / 10 ** 12
        unit_UGF = ' THz'

    UGF = Decimal(UGF_non_d).quantize(Decimal('.01'), rounding=ROUND_UP)

    result = [gain, unit_gain, bandwidth, unit_BW, UGF, unit_UGF, x_1, y]

    return result
'''
x = se_se('D:\\Grad_Project\\Github\\task5\\130nm_bulk.LIB', 'C:\\Users\\Marawan\\Desktop\\se_se.txt', '1', '0', '3', '2',
          '1.2', '600m', '1p', '1', '10G', '10')


print('The gain is: ' + str(x[0]) + str(x[1]))
print('The bandwidth is: ' + str(x[2]) + str(x[3]))
print('The unity gain frequency is: ' + str(x[4]) + str(x[5]))

plt.figure(1)
plt.plot(x[6], x[7])
plt.xscale('log')
plt.show()
'''