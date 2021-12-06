# This function works on plotting different ratios of device parameters against gm/id
# by obtaining each device parameter ratio against VGS and the same for gm/id and plotting
# the intersections.
# The algorithm is inherited from "Systematic Design of Analog CMOS Circuits" by P. Jespers and B. Murmann (2017)
# This function is written on 4/2/2020.
import decimal
import pickle
import matplotlib.pyplot as plt
from get_length import get_length
from get_vsb import get_vsb
import numpy as np
from scipy.interpolate import interpn
from get_vds import get_vds
from get_vgs import get_vgs

def lookup_3(path_n, path_p, vgs_original, vds_original, vsb_original, Length_original, width, var_1, var_2, used_model, **kwargs):

    # Opening the data obtained from sweeping over different length, VSB, VDS and VGS.

    with open(f'{path_n}', 'rb') as out:
        n_data = pickle.load(out)
        out.close()
    with open(f'{path_p}', 'rb') as out:
        p_data = pickle.load(out)
        out.close()

    w = width

    nmos_flag = 0
    pmos_flag = 0
    if used_model == 'NMOS':
        nmos_flag = 1
    elif used_model == 'PMOS':
        pmos_flag = 1

    dummy_var, dummy_var_2, vgs_1 = get_vgs(vgs_original)
    dummy_var_7, dummy_var_8, vds_1 = get_vds(vds_original)
    '''
    dummy_var = vgs.split(':')
    dummy_var_2 = vds.split(':')

    # Obtain the minimum, maximum and step values for both VDS and VGS that were used to generate the 4D array

    vgs_min = dummy_var[0]
    vgs_max = dummy_var[2]
    vgs_step = dummy_var[1]

    vds_min = dummy_var_2[0]
    vds_max = dummy_var_2[2]
    vds_step = dummy_var_2[1]

    # Create a 1D array of the values of VGS and VDS
    vgs_1 = np.arange(float(vgs_min), float(vgs_max) + 0.00001, float(vgs_step))
    vds_1 = np.arange(float(vds_min), float(vds_max) + 0.00001, float(vds_step))
    '''
    # Obtain the values of length and VSB that were used to generate the 4D array
    dummy_var_3, dummy_var_4, length = get_length(Length_original)
    dummy_var_5, dummy_var_6, vsb_value = get_vsb(vsb_original)

    # Defining default values of length, VSB and VDS in case of not being defined by the user.
    # The default values are: minimum length, VDD/2 and VSB = 0

    default_L = min(length)
    default_vds = vds_1[-1]/2
    e = decimal.Decimal(default_vds)
    e = round(e, 2)
    default_vds = float(e)
    #print(default_vds)
    default_vsb = 0
    #print('default length is: ', default_L)
    #print('default VSB is: ', default_vds)
    #print('default VSB is: ', default_vsb)

    # Setting the values of length, VSB and VDS to the default values

    L_used = [default_L]
    vsb_used = [default_vsb]
    vgs_used = [vgs_1]
    vds_used = [default_vds]
    #vds_used = 0.4

    x_final = []
    y_final = []

    # Looking if the length, VSB, VDS or VGS were defined by the user and using these values.
    flag_L = 0
    flag_vgs = 0
    flag_vds = 0
    flag_vsb = 0
    a = 0
    b = 0
    c = 0
    for key in kwargs:
        if 'L' in key:
            a = kwargs['L']
            if a == '':
                L_used = [default_L]
            else:
                b, c, L_used = get_length(a)
                flag_L = 1
        elif 'vsb' in key:
            a = kwargs['vsb']
            if a == '':
                vsb_used = [default_vsb]
            else:
                b, c, vsb_used = get_vsb(a)
                flag_vsb = 1
        elif 'vgs' in key:
            a = kwargs['vgs']
            if a == '':
                vgs_used = [vgs_1]
            else:
                b, c, vgs_used = get_vgs(a)
                flag_vgs = 1
        elif 'vds' in key:
            a = kwargs['vds']
            if a == '':
                vds_used = [default_vds]
            else:
                b, c, vds_used = get_vds(a)
                flag_vds = 1
    #print(list(vds_1).index(vds_used))
    '''
    print('11111111')
    print('Length before is: ', L_used)
    print(len(L_used))
    print('VSB before is: ', vsb_used)
    print(len(vsb_used))
    print('VDS before is: ', vds_used)
    print(len(vds_used))
'''
    #print('Used VSB is ', vsb_used)
    ##print('Used VDS is ', vds_used)
    #print('Used VGS is ', vgs_used)
    #print('Used length is ', L_used)
    interp_values_final_L = []
    interp_values_final_vsb = []
    interp_values_final_vgs = []
    interp_values_final_vds = []

    if flag_L == 1:

        # Check if the input of the user has any value greater than the maximum value used to generate the
        # 4D array, if occurred it will be replaced by the maximum value allowed

        while max(L_used) > max(length):
            L_used[list(L_used).index(max(L_used))] = max(length)

        # Remove all the duplicated values from the list
        for i in range(len(L_used)):
            e = decimal.Decimal(L_used[i])
            e = round(e, 2)
            L_used[i] = float(e)
        L_used = list(dict.fromkeys(L_used))

        # A list to save the approximated values of the Length of the 4D array
        dummy_list_L = []

        # A list to save the approximated values of the Length required
        dummy_list_1_L = []

        # A list to save the values in common between the length values used to generate the 4D array
        # and the required length values
        common_values_L = []

        # A list to save the values of the required length values that are not in the values of lengths
        # used to generate the 4D array.
        # These values will be interpolated.
        interp_values_L = []

        for i in range(len(length)):
            e = decimal.Decimal(length[i])
            dummy_list_L.append(round(e, 2))
            dummy_list_L[i] = float(dummy_list_L[i])

        for i in range(len(L_used)):
            e = decimal.Decimal(L_used[i])
            dummy_list_1_L.append(round(e, 2))

        for i in range(len(L_used)):
            if float(dummy_list_1_L[i]) in dummy_list_L:
                common_values_L.append(dummy_list_1_L[i])
            else:
                interp_values_L.append(dummy_list_1_L[i])

        common_values_final_L = list(map(float, common_values_L))
        interp_values_final_L = list(map(float, interp_values_L))
    if flag_vsb == 1:

        # Check if the input of the user has any value greater than the maximum value used to generate the
        # 4D array, if occurred it will be replaced by the maximum value allowed

        while max(vsb_used) > max(vsb_value):
            vsb_used[list(vsb_used).index(max(vsb_used))] = max(vsb_value)

        # Remove all the duplicated values from the list
        for i in range(len(vsb_used)):
            e = decimal.Decimal(vsb_used[i])
            e = round(e, 2)
            vsb_used[i] = float(e)
        vsb_used = list(dict.fromkeys(vsb_used))

        # A list to save the approximated values of the Length of the 4D array
        dummy_list_vsb = []

        # A list to save the approximated values of the Length required
        dummy_list_1_vsb = []

        # A list to save the values in common between the length values used to generate the 4D array
        # and the required length values
        common_values_vsb = []

        # A list to save the values of the required length values that are not in the values of lengths
        # used to generate the 4D array.
        # These values will be interpolated.
        interp_values_vsb = []

        for i in range(len(vsb_value)):
            e = decimal.Decimal(vsb_value[i])
            dummy_list_vsb.append(round(e, 2))
            dummy_list_vsb[i] = float(dummy_list_vsb[i])

        for i in range(len(vsb_used)):
            e = decimal.Decimal(vsb_used[i])
            dummy_list_1_vsb.append(round(e, 2))

        for i in range(len(vsb_used)):
            if float(dummy_list_1_vsb[i]) in dummy_list_vsb:
                common_values_vsb.append(dummy_list_1_vsb[i])
            else:
                interp_values_vsb.append(dummy_list_1_vsb[i])

        common_values_final_vsb = list(map(float, common_values_vsb))
        interp_values_final_vsb = list(map(float, interp_values_vsb))

    if flag_vgs == 1:

        # Check if the input of the user has any value greater than the maximum value used to generate the
        # 4D array, if occurred it will be replaced by the maximum value allowed

        while max(vgs_used) > max(vgs_1):
            vgs_used[list(vgs_used).index(max(vgs_used))] = max(vgs_1)

        # Remove all the duplicated values from the list
        for i in range(len(vgs_used)):
            e = decimal.Decimal(vgs_used[i])
            e = round(e, 2)
            vgs_used[i] = float(e)
        vgs_used = list(dict.fromkeys(vgs_used))

        # A list to save the approximated values of the Length of the 4D array
        dummy_list_vgs = []

        # A list to save the approximated values of the Length required
        dummy_list_1_vgs = []

        # A list to save the values in common between the length values used to generate the 4D array
        # and the required length values
        common_values_vgs = []

        # A list to save the values of the required length values that are not in the values of lengths
        # used to generate the 4D array.
        # These values will be interpolated.
        interp_values_vgs = []

        for i in range(len(vgs_1)):
            e = decimal.Decimal(vgs_1[i])
            dummy_list_vgs.append(round(e, 2))
            dummy_list_vgs[i] = float(dummy_list_vgs[i])

        for i in range(len(vgs_used)):
            e = decimal.Decimal(vgs_used[i])
            dummy_list_1_vgs.append(round(e, 2))

        for i in range(len(vgs_used)):
            if float(dummy_list_1_vgs[i]) in dummy_list_vgs:
                common_values_vgs.append(dummy_list_1_vgs[i])
            else:
                interp_values_vgs.append(dummy_list_1_vgs[i])

        common_values_final_vgs = list(map(float, common_values_vgs))
        interp_values_final_vgs = list(map(float, interp_values_vgs))

    if flag_vds == 1:

        # Check if the input of the user has any value greater than the maximum value used to generate the
        # 4D array, if occurred it will be replaced by the maximum value allowed

        while max(vds_used) > max(vds_1):
            vds_used[list(vds_used).index(max(vds_used))] = max(vds_1)

        # Remove all the duplicated values from the list
        for i in range(len(vds_used)):
            e = decimal.Decimal(vds_used[i])
            e = round(e, 2)
            vds_used[i] = float(e)
        vds_used = list(dict.fromkeys(vds_used))

        # A list to save the approximated values of the Length of the 4D array
        dummy_list_vds = []

        # A list to save the approximated values of the Length required
        dummy_list_1_vds = []

        # A list to save the values in common between the length values used to generate the 4D array
        # and the required length values
        common_values_vds = []

        # A list to save the values of the required length values that are not in the values of lengths
        # used to generate the 4D array.
        # These values will be interpolated.
        interp_values_vds = []

        for i in range(len(vds_1)):
            e = decimal.Decimal(vds_1[i])
            dummy_list_vds.append(round(e, 2))
            dummy_list_vds[i] = float(dummy_list_vds[i])

        for i in range(len(vds_used)):
            e = decimal.Decimal(vds_used[i])
            dummy_list_1_vds.append(round(e, 2))

        for i in range(len(vds_used)):
            if float(dummy_list_1_vds[i]) in dummy_list_vds:
                common_values_vds.append(dummy_list_1_vds[i])
            else:
                interp_values_vds.append(dummy_list_1_vds[i])

        common_values_final_vds = list(map(float, common_values_vds))
        interp_values_final_vds = list(map(float, interp_values_vds))

    # Check if we need to perform interpolation

    need_L = 0
    need_vsb = 0
    need_vgs = 0
    need_vds = 0

    if len(interp_values_final_L) != 0:
        need_L = 1
    if len(interp_values_final_vsb) != 0:
        need_vsb = 1
    if len(interp_values_final_vgs) != 0:
        need_vgs = 1
    if len(interp_values_final_vds) != 0:
        need_vds = 1

    points = (length, vsb_value, vgs_1, vds_1)
    array_vsb_d = 0
    array_l_d = 0
    array_vds_d = 0

    if flag_vsb == 0:
        array_vsb_d = 1
    else:
        array_vsb_d = len(vsb_used)

    if flag_vds == 0:
        array_vds_d = 1
    else:
        array_vds_d = len(vds_used)

    if flag_L == 0:
        array_l_d = 1
    else:
        array_l_d = len(L_used)

    results_gm_n = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    results_gm_p = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    xi_gm = ()
    '''
    print('222222')
    print('Length after is: ', L_used)
    print(len(L_used))
    print('VSB after is: ', vsb_used)
    print(len(vsb_used))
    print('VDS after is: ', vds_used)
    print(len(vds_used))
'''

    for i in range(array_vsb_d):
        for j in range(array_vds_d):
            for k in range(array_l_d):


                xi = (L_used[k], vsb_used[i], vgs_used, vds_used[j])
                results_gm_n[i][k][j] = interpn(points, n_data['gm'], xi)
                results_gm_p[i][k][j] = interpn(points, p_data['gm'], xi)
                #arew = interpn(points, n_data['gm'], xi)

    results_id_n = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    results_id_p = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    xi_id = ()

    for i in range(array_vsb_d):
        for j in range(array_vds_d):
            for k in range(array_l_d):
                xi_id = (L_used[k], vsb_used[i], vgs_used, vds_used[j])
                #print(xi_id)
                results_id_n[i][k][j] = interpn(points, n_data['id'], xi_id)
                results_id_p[i][k][j] = interpn(points, p_data['id'], xi_id)
                # arew = interpn(points, n_data['gm'], xi)
    #print(results_id_p)
    # Calculating the gm/id ratio

    results_gm_id_n = np.divide(results_gm_n, results_id_n)
    results_gm_id_p = np.divide(results_gm_p, results_id_p)

    #print('111111111111', results_gm_id_n)
    #print('222222222222', results_gm_id_p)

    # The graph of gm/id inherits a non monotonic behaviour as illustrated in the previously mentioned
    # reference in the appendix section, so for the gm/id curve we find its maximum value and taking
    # all the points to its right to implement a monotonic behaviour.
    # Such behaviour is repeated also for both of ratios: gm/cgg and gm/cgs but we take the values tp their
    # left as will be illustrated shortly.
    vgs_final_n = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    vgs_final_p = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    for i in range(array_vsb_d):
        for j in range(array_vds_d):
            for k in range(array_l_d):
                #print(i, j, k)
                #print(results_gm_id_n[i][k][j])
                max_gmid_n = max(list(results_gm_id_n[i][k][j])[0])
                max_gmid_p = max(list(results_gm_id_p[i][k][j])[0])

                gmid_used = list(list(results_gm_id_n[i][k][j])[0])[list(list(results_gm_id_n[i][k][j])[0]).index(max_gmid_n):]
                #print(len(gmid_used))
                idx = list(list(results_gm_id_n[i][k][j])[0]).index(max_gmid_n)
                results_gm_id_n[i][k][j] = gmid_used
                vgs_final_n[i][k][j] = vgs_1[idx:, ]

                gmid_used = list(list(results_gm_id_p[i][k][j])[0])[
                            list(list(results_gm_id_p[i][k][j])[0]).index(max_gmid_p):]
                # print(len(gmid_used))
                idx = list(list(results_gm_id_p[i][k][j])[0]).index(max_gmid_p)
                results_gm_id_p[i][k][j] = gmid_used
                vgs_final_p[i][k][j] = vgs_1[idx:, ]
                #print(len(vgs_final[i][k][j]))

    #print('VGS final n is: ', vgs_final_n)
    #print('VGS final p is: ', vgs_final_p)
    #print(vgs_final.shape)
    #print('results final n are:', results_gm_id_n)
    #print('results final p are:', results_gm_id_p)
    #print(results_gm_id_n.shape)
    #plt.plot(vgs_new, gmid_used)
    #plt.show()

    y_1 = []
    y_2 = []
    flag = 0

    # Check if one of the output desired variables is the transistor's width

    if var_1 in n_data.keys():
        y_1 = n_data[var_1]
    elif var_1 == 'w':
        y_1 = float(w)
    if var_2 in n_data.keys():
        y_2 = n_data[var_2]
    elif var_2 == 'w':
        y_2 = float(w)
    #Creating 2 arrays to hold the values of the required parameter at the requested values of Length, VSB and VDS
    results_var_1 = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    results_var_2 = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    y = np.zeros(shape=(array_vsb_d, array_l_d, array_vds_d), dtype=object)
    #Creating two empty tuples to use in case of having points off-grid that will require interpolation
    xi_var_1 = ()
    xi_var_2 = ()

    if var_1 == 'w' or var_2 == 'w':
        if type(y_1) is int:
            for i in range(array_vsb_d):
                for j in range(array_vds_d):
                    for k in range(array_l_d):
                        xi_var_2 = (L_used[k], vsb_used[i], vgs_used, vds_used[j])

                        results_var_2[i][k][j] = interpn(points, y_2, xi_var_2)

            y = np.divide(y_1, results_var_2)


        else:
            for i in range(array_vsb_d):
                for j in range(array_vds_d):
                    for k in range(array_l_d):
                        xi_var_1 = (L_used[k], vsb_used[i], vgs_used, vds_used[j])

                        results_var_1[i][k][j] = interpn(points, y_1, xi_var_1)
            y = np.divide(results_var_1, y_2)

    else:
        for i in range(array_vsb_d):
            for j in range(array_vds_d):
                for k in range(array_l_d):
                    xi_var_2 = (L_used[k], vsb_used[i], vgs_used, vds_used[j])
                    results_var_1[i][k][j] = interpn(points, y_1, xi_var_2)
                    results_var_2[i][k][j] = interpn(points, y_2, xi_var_2)

        y = np.divide(results_var_1, results_var_2)

    #print(n_data['gm'])
    #print(y_1)
    #print(results_id[0][2][0])
    #print(results_var_2[0][2][0])
    #print(results_var_2)
    #print(list(y[0][0][1])[0])

    for i in range(array_vsb_d):
        for j in range(array_vds_d):
            for k in range(array_l_d):
                if nmos_flag == 1:

                    out_used = list(list(y[i][k][j])[0][list(vgs_1).index(list(vgs_final_n[i][k][j])[0]):])
                    y[i][k][j] = out_used
                if pmos_flag == 1:

                    out_used = list(list(y[i][k][j])[0][list(vgs_1).index(list(vgs_final_p[i][k][j])[0]):])
                    y[i][k][j] = out_used

    #y_used = y[idx:, ]
    #print(y_1[list(length).index(L_used), list(vsb_value).index(vsb_used), :, list(vds_1).index(vds_used)])
    #print(y_2[list(length).index(L_used), list(vsb_value).index(vsb_used), :, list(vds_1).index(vds_used)])
    #print(max(list(y)))
    #print(y[:list(y).index(max(list(y)))+1])
    #print(list(y).index(max(list(y))))

    # The gm/cgs and gm/cgg case.
    if var_1 == 'gm':
        if var_2 == 'cgg' or var_2 == 'cgs':
            #print('7alawa')
            for i in range(array_vsb_d):
                for j in range(array_vds_d):
                    for k in range(array_l_d):
                        if nmos_flag == 1:
                            y_max = max(y[i][k][j])
                            y_gm_cggs = list(list(y[i][k][j])[:list(y[i][k][j]).index(y_max)+1])
                            idx_1 = list(y[i][k][j]).index(y_max)
                            y[i][k][j] = y_gm_cggs
                            vgs_gm_cggs = list(list(vgs_final_n)[i][k][j][:idx_1+1])
                            vgs_final_n[i][k][j] = vgs_gm_cggs
                            gm_id_cggs = list(list(results_gm_id_n[i][k][j])[:idx_1+1])
                            results_gm_id_n[i][k][j] = gm_id_cggs

                        if pmos_flag == 1:
                            y_max = max(y[i][k][j])
                            y_gm_cggs = list(list(y[i][k][j])[:list(y[i][k][j]).index(y_max)+1])
                            idx_1 = list(y[i][k][j]).index(y_max)
                            y[i][k][j] = y_gm_cggs
                            vgs_gm_cggs = list(list(vgs_final_p)[i][k][j][:idx_1+1])
                            vgs_final_p[i][k][j] = vgs_gm_cggs
                            gm_id_cggs = list(list(results_gm_id_p[i][k][j])[:idx_1+1])
                            results_gm_id_p[i][k][j] = gm_id_cggs
    #print(len(y[0][1][4]))
    #print(len(results_gm_id_n[0][1][4]))


    output_var = var_1 + '/' + var_2

    for i in range(len(L_used)):
        L_used[i] = str(L_used[i])
    for i in range(len(vds_used)):
        vds_used[i] = str(vds_used[i])
    for i in range(len(vsb_used)):
        vsb_used[i] = str(vsb_used[i])

    return y, results_gm_id_n, results_gm_id_p, L_used, vds_used, vsb_used, output_var
    #plt.plot(x_final, y_final)

    #plt.show()

#plot_graphs('D:\\Grad_Project\\Github\\task5\\nmos_data.txt', 'D:\\Grad_Project\\Github\\task5\\pmos_data.txt', '0:0.1:1',
            #'0:0.2:1.2', '0:0.5:1', '0.2u:0.2u:1u', 'id', 'w')

#plot_graphs('D:\\Grad_Project\\Github\\task5\\nmos_data.txt', 'D:\\Grad_Project\\Github\\task5\\pmos_data.txt', '0:0.1:1',
 #           '0:0.2:1.2', '0:0.5:1', '0.2u:0.2u:1u', 'gm', 'cgs')

#y, x1, x2, L, vds, vsb, out = lookup_3('D:\\Grad_Project\\Github\\task5\\nmos_data.txt', 'D:\\Grad_Project\\Github\\task5\\pmos_data.txt', '0:0.1:1',
 #           '0:0.2:1.2', '0:0.5:1', '0.2:0.2:1', '2', 'gm', 'gds', 'PMOS', L='0.2:0.2:0.8', vsb='0:0.3:1.6', vds='0:0.2:1.6')



#, L='0.5u:0.2u:1u', vsb='0', vds='0:0.3:1.5'
#y, x, L, out = plot_graphs('D:\\Grad_Project\\Github\\task5\\nmos_data.txt', 'D:\\Grad_Project\\Github\\task5\\pmos_data.txt', '0:0.1:1',
 #           '0:0.2:1.2', '0:0.5:1', '0.2u:0.2u:1u', 'gm', 'cgg')

#a = x[0, :, 2]
#b = y[0, :, 2]
#print(x.shape)
#print(len(a))
#print(b)
#print(out)
#print(type(out))
#print(y)
#for i in range(len(a)):
 #   plt.plot(a[i], b[i], label=f'L = {L[i]} um')
#print(y)
#y_new = 20*np.log10(y[0, 0, 2])
#print(len(x[0, 0, 2]))
#print(len(y[0, 0, 2]))
#'''
#y_new = 20*np.log10(y)
#plt.plot(x[0, 0, 2], y_new)

#plt.legend()
#plt.grid()
#plt.xlabel('gm/id')
#plt.ylabel(out)
#plt.title(f'{out} vs. gm/id')
#plt.show()
#'''