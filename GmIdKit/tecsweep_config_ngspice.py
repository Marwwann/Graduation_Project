from numpy import arange, concatenate
import re


class C:
    def __init__(self, libPath,
                 VGS_MIN, VGS_STEP, VGS_MAX,
                 VDS_MIN, VDS_STEP, VDS_MAX,
                 VSB_MIN, VSB_STEP, VSB_MAX,
                 L):
        # models and info
        self.model_file = libPath
        self.Info = self.model_file.split("/")[-1].split(".")[0]
        self.corner = "NOM"
        self.temp = "300"
        self.model_n, self.model_p = self.getModel(libPath)
        self.sim_cmd_n = "ngspice -b -r result_n.raw "
        self.sim_cmd_p = "ngspice -b -r result_p.raw "
        self.out_file_n = "result_n.raw"
        self.out_file_p = "result_p.raw"
        # setup parameters
        self.VGS_STEP = VGS_STEP
        self.VDS_STEP = VDS_STEP
        self.VSB_STEP = VSB_STEP
        self.VGS_MAX = VGS_MAX
        self.VDS_MAX = VDS_MAX
        self.VSB_MAX = VSB_MAX
        self.VGS_MIN = VGS_MIN
        self.VDS_MIN = VDS_MIN
        self.VSB_MIN = VSB_MIN
        self.VGS = arange(self.VGS_MIN, self.VGS_MAX + 1e-6, self.VGS_STEP)
        self.VDS = arange(self.VDS_MIN, self.VDS_MAX + 1e-6, self.VDS_STEP)
        self.VSB = arange(self.VSB_MIN, self.VSB_MAX + 1e-6, self.VSB_STEP)
        self.LENGTH = L
        print(self.LENGTH)
        self.WIDTH = 4
        self.NFING = 4
        self.savedParameters = ['v(v-sweep)', 'i(vdsn)', '@mn[gm]', '@mn[gmbs]', '@mn[gds]', '@mn[cgg]', '@mn[cgs]', '@mn[cgd]', '@mn[cdd]', '@mn[cbs]']
        self.parameterSign = {'v(v-sweep)':1, 'i(vdsn)':-1, '@mn[gm]':1, '@mn[gmbs]':1, '@mn[gds]':1, '@mn[cgg]':1, '@mn[cgs]':-1, '@mn[cgd]':-1, '@mn[cdd]':1, '@mn[cbs]':1}

    def getModel(self, fname):
        try:
            with open(fname) as my_file:
                s = my_file.read()
        except:
            print("model path is wrong")
        try:
            strn = re.findall(".[modelMODEL]{5}\s+(\S*)\s+[nmosNMOS]{4}", s)[0]
            strp = re.findall(".[modelMODEL]{5}\s+(\S*)\s+[pmosPMOS]{4}", s)[0]
            return strn, strp
        except:
            print("model file does not contain MOSFET model")
            return


    def gen_netlist_n(self):
        return """MOS test bench
* Include external file that contains MOSFET Model
.INCLUDE {}
.INCLUDE techsweep_params.cir
        
** Circuit Description **
* power supply
vdsn dn 0 dc=0  
vgsn gn 0 dc=0  
vbsn bn 0 dc={{-sb}} 
        
        
* circuit
mn dn gn 0 bn {} L={{Len}} W={}u
       
        
*sweep
.DC vdsn {} {} {} vgsn {} {} {}
        
*saving parameters
.save i(vdsn) @mn[gm] @mn[gmbs] @mn[gds] @mn[cgg] @mn[cgs] @mn[cgd] @mn[cdd] @mn[cbs]
        
.end
        """.format(self.model_file,
                   self.model_n, self.WIDTH,
                   self.VDS_MIN, self.VDS_MAX, self.VDS_STEP,
                   self.VGS_MIN, self.VGS_MAX, self.VGS_STEP)



    def gen_netlist_p(self):
        return """MOS test bench
* Include external file that contains MOSFET Model
.INCLUDE {}
.INCLUDE techsweep_params.cir
        
** Circuit Description **
* power supply
        
vdsp dp 0 dc=0 
vgsp gp 0 dc=0
vbsp bp 0 dc={{sb}}  
        
* circuit
mp dp gp 0 bp {} L={{Len}} W={}u
        
*sweep
.DC vdsp -{} -{} -{} vgsp -{} -{} -{}
        
*saving parameters
.save i(vdsp) @mp[gm] @mp[gmbs] @mp[gds] @mp[cgg] @mp[cgs] @mp[cgd] @mp[cdd] @mp[cbs]
        
.end
        """.format(self.model_file,
                   self.model_p, self.WIDTH,
                   self.VDS_MIN, self.VDS_MAX, self.VDS_STEP,
                   self.VGS_MIN, self.VGS_MAX, self.VGS_STEP)


def write_netlist(netlist, sweep_type="techsweep_n.cir"):
    with open(sweep_type, 'w') as out:
        out.write(netlist)




