# This function starts creating a 4D array having the values of device parameters that were previously determined
# by the techsweep_config_ngspice function.
# The function uses ngspice as a SPICE simulator to obtain the results needed and then it stores all the data
# in 4D array for each parameter.
# The output files of ngspice are of RAW type, so we use the predefined function "readraw", credits go to MIT students.


from techsweep_configuration_ngspice import techsweep_config_ngspice
from get_length import get_length
from get_vsb import get_vsb
from get_vds import get_vds
from get_vgs import get_vgs
import os
import numpy as np
from GmIdKit.read_raw import rawread
import pickle

def techsweep_run_ngspice(path, width, temp, Length, vsb, vgs, vds):

    dummy_var = vgs.split(':')
    dummy_var_2 = vds.split(':')
    list_vgs, used_unit_vgs, vgs_values = get_vgs(vgs)

    list_vds, used_unit_vds, vds_values = get_vds(vds)
    # Obtain the minimum, maximum and step values for both VDS and VGS

    vgs_min = dummy_var[0]
    vgs_max = dummy_var[2]
    vgs_step = dummy_var[1]

    vds_min = dummy_var_2[0]
    vds_max = dummy_var_2[2]
    vds_step = dummy_var_2[1]

    # Create a 1D array of the values of VGS and VDS

    vgs_1 = np.arange(float(vgs_min), float(vgs_max) + 0.000001, float(vgs_step))
    vds_1 = np.arange(float(vds_min), float(vds_max) + 0.000001, float(vds_step))
    print(vds_1)
    # Call the techsweep_config_ngspice to generate the required netlist at the given sweep values

    techsweep_config_ngspice(path, width, temp, vgs_min, vgs_step, vgs_max, vds_min, vds_step, vds_max)

    # Use the get_length and get_vsb functions to obtain vectors of the length and VSB values needed for the sweep.

    list_length, used_unit_length, length_values = get_length(Length)
    list_vsb, used_unit_vsb, vsb_values = get_vsb(vsb)

    # Create a 4D array for each device parameter defined in the netlist with the dimensions
    # of VGS, VDS, VSB and Length.
    # The rows are the VGS values, columns are VDS values, the third dimension is the VSB values
    # and the fourth is the Length values.
    # The arrays are generated for both NMOS and PMOS.

    n_id = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    n_gm = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    n_gmbs = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    n_gds = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    n_cgg = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    n_cgs = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    n_cgd = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    n_cdd = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    n_cbs = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))

    p_id = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    p_gm = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    p_gmbs = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    p_gds = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    p_cgg = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    p_cgs = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    p_cgd = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    p_cdd = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))
    p_cbs = np.zeros(shape=(len(list_length), len(list_vsb), len(vgs_1), len(vds_1)))

    # Using for loop to iterate over the required values of the length and VSB
    for i in range(len(list_length)):
        for j in range(len(list_vsb)):
            # Creating the parameter file to include in the netlist with the required length and VSB value
            with open('techsweep_params.cir', 'w') as out:
                out.write(f'.param Len={float(list_length[i])*1e-6}\n.param sb={float(list_vsb[j])}')
                out.close()

            # Calling ngspice in the batch mode and saving the results as raw files for both NMOS and PMOS.

            os.system('ngspice -b -r results_nmos.raw netlist_nmos_BSIM4.txt')
            os.system('ngspice -b -r results_pmos.raw netlist_pmos_BSIM4.txt')

            # Creating the 4D array by reading the data and storing it for each device parameter
            # for both NMOS and PMOS.

            dummy_list_n = []
            dummy_list_p = []
            darrs_n, mda_n = rawread('results_nmos.raw')
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][c][mda_n[0]['varnames'].index('i(vdsn)')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_id[i][j][:][:] = a
            #print(n_id)
            dummy_list_n = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][c][mda_n[0]['varnames'].index('@mn[gm]')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_gm[i][j][:][:] = a
            dummy_list_n = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][c][mda_n[0]['varnames'].index('@mn[gmbs]')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_gmbs[i][j][:][:] = a
            dummy_list_n = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][c][mda_n[0]['varnames'].index('@mn[gds]')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_gds[i][j][:][:] = a
            dummy_list_n = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][c][mda_n[0]['varnames'].index('@mn[cgg]')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_cgg[i][j][:][:] = a
            dummy_list_n = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][i][mda_n[0]['varnames'].index('@mn[cgs]')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_cgs[i][j][:][:] = a
            dummy_list_n = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][c][mda_n[0]['varnames'].index('@mn[cgd]')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_cgd[i][j][:][:] = a
            dummy_list_n = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][c][mda_n[0]['varnames'].index('@mn[cdd]')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_cdd[i][j][:][:] = a
            dummy_list_n = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_n[0])):
                dummy_list_n.append(darrs_n[0][c][mda_n[0]['varnames'].index('@mn[cbs]')])
            z = np.reshape(dummy_list_n, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            n_cbs[i][j][:][:] = a
            dummy_list_n = []
            z = 0
            a = 0
            c = 0

            darrs_p, mda_p = rawread('results_pmos.raw')

            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('i(vdsp)')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_id[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('@mp[gm]')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_gm[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('@mp[gmbs]')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_gmbs[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('@mp[gds]')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_gds[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('@mp[cgg]')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_cgg[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('@mp[cgs]')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_cgs[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('@mp[cgd]')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_cgd[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('@mp[cdd]')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_cdd[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0
            for c in range(len(darrs_p[0])):
                dummy_list_p.append(darrs_p[0][c][mda_p[0]['varnames'].index('@mp[cbs]')])
            z = np.reshape(dummy_list_p, (len(vds_1), len(vgs_1)))
            a = np.absolute(z.T)
            p_cbs[i][j][:][:] = a
            dummy_list_p = []
            z = 0
            a = 0
            c = 0


    nmos_dict = {'width': width, 'length': Length, 'vgs': vgs, 'vds': vds, 'vsb': vsb, 'id': n_id, 'gm': n_gm, 'gmbs': n_gmbs, 'gds': n_gds, 'cgg': n_cgg, 'cgs': n_cgs, 'cgd': n_cgd, 'cdd': n_cdd,
                 'cbs': n_cbs}
    pmos_dict = {'width': width, 'length': Length, 'vgs': vgs, 'vds': vds, 'vsb': vsb, 'id': p_id, 'gm': p_gm, 'gmbs': p_gmbs, 'gds': p_gds, 'cgg': p_cgg, 'cgs': p_cgs, 'cgd': p_cgd,
                'cdd': p_cdd, 'cbs': p_cbs}

    with open('nmos_data.txt', 'wb') as out:
        pickle.dump(nmos_dict, out)
        out.close()
    with open('pmos_data.txt', 'wb') as out:
        pickle.dump(pmos_dict, out)
        out.close()

'''
techsweep_run_ngspice('D:\\Grad_Project\\Github\\task5\\130nm_bulk.LIB', '4', '27', '0.2u:0.2u:1u', '0:0.5:1', '0:0.1:1', '0:0.2:1.2')
with open('nmos_data.txt', 'rb') as out:
    x = pickle.load(out)
    out.close()
print(x['id'])
with open('pmos_data.txt', 'rb') as out:
    y = pickle.load(out)
    out.close()
print(y['id'])
'''