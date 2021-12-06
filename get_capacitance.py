import numpy as np
import re
def get_cap(cap):
    capacitance = []
    if cap == '':
        capacitance.append('1f')

    else:
        range_flag = 0
        if re.search(':', cap):
            x = re.split(':', cap)
            range_flag = 1
        else:
            x = re.split('\s', cap)
            range_flag = 0

        if x[-1] == '':
            x.pop()

        if range_flag == 1:
            range_list = []
            for i in range(len(x)):
                y = re.split('p', x[i])
                y.pop()
                range_list.append(y)
            pre_capacitance = np.arange(int(range_list[0][0]), int(range_list[2][0]) + 0.00001, int(range_list[1][0]))

            for i in pre_capacitance:
                capacitance.append(str(i) + 'p')
        else:
            capacitance = x
    #print(capacitance)
    return capacitance
