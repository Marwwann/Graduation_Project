import GmIdKit.tecsweep_config_ngspice as conf
from GmIdKit import read_raw
import json
import os
from numpy import zeros, reshape
import pickle
import re


class Object:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)

def generateCharts(logGenerateChartslabel, libpath, ngSpiceCommand,
                   VGS, VDS, VSB,
                   Larg):
    try:
        config = conf.C(libpath, ngSpiceCommand,
                    VGS[0], VGS[1], VGS[2],
                    VDS[0], VDS[1], VDS[2],
                    VSB[0], VSB[1], VSB[2],
                    Larg)
    except:
        print("error in generate charts")
        return

    nch = Object()
    nch.INFO = config.Info
    nch.TYPE = "nmos"
    nch.CORNER = config.corner
    nch.TEMP = config.temp
    nch.W = config.WIDTH
    nch.L = config.LENGTH
    nch.VGS = config.VGS
    nch.VDS = config.VDS
    nch.VSB = config.VSB
    nch.ID = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    nch.GM = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    nch.GMBS = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    nch.GDS = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    nch.CGG = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    nch.CGS = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    nch.CGD = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    nch.CDD = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    nch.CBS = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))

    pch = Object()
    pch.INFO = config.Info
    pch.TYPE = "pmos"
    pch.CORNER = config.corner
    pch.TEMP = config.temp
    pch.W = config.WIDTH
    pch.L = config.LENGTH
    pch.VGS = config.VGS
    pch.VDS = config.VDS
    pch.VSB = config.VSB
    pch.ID = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    pch.GM = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    pch.GMBS = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    pch.GDS = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    pch.CGG = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    pch.CGS = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    pch.CGD = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    pch.CDD = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))
    pch.CBS = zeros(shape=(len(config.LENGTH), len(config.VSB), len(config.VGS), len(config.VDS)))

    # write main netlists
    conf.write_netlist(netlist=config.gen_netlist_n(), sweep_type="techsweep_n.cir")
    conf.write_netlist(netlist=config.gen_netlist_p(), sweep_type="techsweep_p.cir")

    # simulation loop
    break_flag = 0
    for i in range(0, len(config.LENGTH)):
        if break_flag:
            break

        logGenerateChartslabel.setText("\nCurrent L = {} ==> {}".format(config.LENGTH[i], config.LENGTH[-1]))
        for j in range(0, len(config.VSB)):
            # write parameters file
            with open("techsweep_params.cir", 'w') as out:
                out.write(""".param Len={}\n.param sb={}"""
                          .format(config.LENGTH[i]*1e-6, config.VSB[j]))


            try:
                if os.system(config.sim_cmd_n+"techsweep_n.cir") or os.system(config.sim_cmd_p+"techsweep_p.cir"):
                    print("simulation failed")
                    break_flag = 1
                    break
            except:
                print("error in ngspice command:", config.sim_cmd_n)
            # Read and store results
            ndarr_n, mda_n = read_raw.rawread(config.out_file_n)
            id_n = [-i[mda_n[0]["varnames"].index("i(vdsn)")] for i in ndarr_n[0]]
            gm_n = [i[mda_n[0]["varnames"].index("@mn[gm]")] for i in ndarr_n[0]]
            gmbs_n = [i[mda_n[0]["varnames"].index("@mn[gmbs]")] for i in ndarr_n[0]]
            gds_n = [i[mda_n[0]["varnames"].index("@mn[gds]")] for i in ndarr_n[0]]
            cgg_n = [i[mda_n[0]["varnames"].index("@mn[cgg]")] for i in ndarr_n[0]]
            cgs_n = [-i[mda_n[0]["varnames"].index("@mn[cgs]")] for i in ndarr_n[0]]
            cgd_n = [-i[mda_n[0]["varnames"].index("@mn[cgd]")] for i in ndarr_n[0]]
            cdd_n = [i[mda_n[0]["varnames"].index("@mn[cdd]")] for i in ndarr_n[0]]
            cbs_n = [i[mda_n[0]["varnames"].index("@mn[cbs]")] for i in ndarr_n[0]]
            nch.ID[i][j][:][:] = reshape(id_n, (len(config.VGS), len(config.VDS)))
            nch.GM[i][j][:][:] = reshape(gm_n, (len(config.VGS), len(config.VDS)))
            nch.GMBS[i][j][:][:] = reshape(gmbs_n, (len(config.VGS), len(config.VDS)))
            nch.GDS[i][j][:][:] = reshape(gds_n, (len(config.VGS), len(config.VDS)))
            nch.CGG[i][j][:][:] = reshape(cgg_n, (len(config.VGS), len(config.VDS)))
            nch.CGS[i][j][:][:] = reshape(cgs_n, (len(config.VGS), len(config.VDS)))
            nch.CGD[i][j][:][:] = reshape(cgd_n, (len(config.VGS), len(config.VDS)))
            nch.CDD[i][j][:][:] = reshape(cdd_n, (len(config.VGS), len(config.VDS)))
            nch.CBS[i][j][:][:] = reshape(cbs_n, (len(config.VGS), len(config.VDS)))

            ndarr_p, mda_p = read_raw.rawread(config.out_file_p)
            id_p = [-i[mda_p[0]["varnames"].index("i(vdsp)")] for i in ndarr_p[0]]
            gm_p = [i[mda_p[0]["varnames"].index("@mp[gm]")] for i in ndarr_p[0]]
            gmbs_p = [i[mda_p[0]["varnames"].index("@mp[gmbs]")] for i in ndarr_p[0]]
            gds_p = [i[mda_p[0]["varnames"].index("@mp[gds]")] for i in ndarr_p[0]]
            cgg_p = [i[mda_p[0]["varnames"].index("@mp[cgg]")] for i in ndarr_p[0]]
            cgs_p = [-i[mda_p[0]["varnames"].index("@mp[cgs]")] for i in ndarr_p[0]]
            cgd_p = [-i[mda_p[0]["varnames"].index("@mp[cgd]")] for i in ndarr_p[0]]
            cdd_p = [i[mda_p[0]["varnames"].index("@mp[cdd]")] for i in ndarr_p[0]]
            cbs_p = [i[mda_p[0]["varnames"].index("@mp[cbs]")] for i in ndarr_p[0]]
            pch.ID[i][j][:][:] = reshape(id_p, (len(config.VGS), len(config.VDS)))
            pch.GM[i][j][:][:] = reshape(gm_p, (len(config.VGS), len(config.VDS)))
            pch.GMBS[i][j][:][:] = reshape(gmbs_p, (len(config.VGS), len(config.VDS)))
            pch.GDS[i][j][:][:] = reshape(gds_p, (len(config.VGS), len(config.VDS)))
            pch.CGG[i][j][:][:] = reshape(cgg_p, (len(config.VGS), len(config.VDS)))
            pch.CGS[i][j][:][:] = reshape(cgs_p, (len(config.VGS), len(config.VDS)))
            pch.CGD[i][j][:][:] = reshape(cgd_p, (len(config.VGS), len(config.VDS)))
            pch.CDD[i][j][:][:] = reshape(cdd_p, (len(config.VGS), len(config.VDS)))
            pch.CBS[i][j][:][:] = reshape(cbs_p, (len(config.VGS), len(config.VDS)))

    # delete unwanted files
    os.system("del techsweep_n.cir techsweep_p.cir techsweep_params.cir " + config.out_file_n + " " + config.out_file_p)
    # print done
    logGenerateChartslabel.setText("\nCharts generated successfully")

    # save variables

    with open("nch "+nch.INFO, "wb") as f:
        pickle.dump(nch, f)
    with open("pch "+pch.INFO, "wb") as f:
        pickle.dump(pch, f)




#x = generateCharts('D:\\Grad_Project\\Github\\task5\\130nm_bulk.pm.lib', 'ngspice', [0, 0.01, 1], [0, 0.1, 1], [0, 0.5, 1], [0.2,0.2,0.4])

#load Variables
#with open("nch 130nm_bulk", "rb") as f:
 #   nch2 = pickle.load(f)
#ith open("pch 130nm_bulk", "rb") as f:
#    pch2 = pickle.load(f)

#print(nch2.to_json())
