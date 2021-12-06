# This function sets up all the needed configurations to generate a netlist
# that is used to run ngspice and generate all the needed device parameters
# to construct the 4D array needed for the gm/id charts.

# This function is written on 31/1/2020


from read_model_file import read_model_file
from get_model import get_model


def techsweep_config_ngspice(path, width, temp, vgs_min, vgs_step, vgs_max, vds_min, vds_step, vds_max):

    bsim_model = read_model_file(path)
    width = width
    temp = temp
    nfing = 4
    model = get_model(path)


    # Generate a netlist for BSIM Model 3
    if bsim_model == 3:

        with open('netlist_nmos_BSIM3.txt', 'w') as out_n_3:
            out_n_3.write(f'''MOS test bench
* Include external file that contains MOSFET Model
.INCLUDE {path}
.INCLUDE techsweep_params.cir
        
** Circuit Description **
* power supply
vdsn dn 0 dc=0  
vgsn gn 0 dc=0  
vbsn bn 0 dc={{-sb}} 
        
        
* circuit
mn dn gn 0 bn {model[0]} L={{Len}} W={width}u
       
        
*sweep
.DC vgsn {vgs_min} {vgs_max} {vgs_step} vdsn {vds_min} {vds_max} {vds_step}
.TEMP {temp}        
*saving parameters
.save i(vdsn) @mn[gm] @mn[gmbs] @mn[gds] @mn[cgg] @mn[cgs] @mn[cgd] @mn[cdd] @mn[cbs]
        
.end''')
            out_n_3.close()

        with open('netlist_pmos_BSIM3.txt', 'w') as out_p_3:
            out_p_3.write(f'''MOS Test Bench
* Include external file that contains MOSFET Model
.INCLUDE {path}
.INCLUDE techsweep_params.cir

** Circuit Description **
* power supply

vdsp dp 0 dc=0 
vgsp gp 0 dc=0
vbsp bp 0 dc={{sb}}  

* circuit
mp dp gp 0 bp {model[1]} L={{Len}} W={width}u

*sweep
.DC vgsp -{vgs_min} -{vgs_max} -{vgs_step} vdsp -{vds_min} -{vds_max} -{vds_step}
.TEMP {temp}
*saving parameters
.save i(vdsp) @mp[gm] @mp[gmbs] @mp[gds] @mp[cgg] @mp[cgs] @mp[cgd] @mp[cdd] @mp[cbs]

.end''')
            out_p_3.close()

    # Generate a netlist for BSIM Model 4
    elif bsim_model == 4:

        with open('netlist_nmos_BSIM4.txt', 'w') as out_n_4:
            out_n_4.write(f'''MOS test bench
* Include external file that contains MOSFET Model
.INCLUDE {path}
.INCLUDE techsweep_params.cir

** Circuit Description **
* power supply
vdsn dn 0 dc=0  
vgsn gn 0 dc=0  
vbsn bn 0 dc={{-sb}} 


* circuit
mn dn gn 0 bn {model[0]} L={{Len}} W={width}u


*sweep
.DC vgsn {vgs_min} {vgs_max} {vgs_step} vdsn {vds_min} {vds_max} {vds_step}
.TEMP {temp}
*saving parameters
.save i(vdsn) @mn[gm] @mn[gmbs] @mn[gds] @mn[cgg] @mn[cgs] @mn[cgd] @mn[cdd] @mn[cbs] @mn[vdsat]

.end''')
            out_n_4.close()

        with open('netlist_pmos_BSIM4.txt', 'w') as out_p_4:
            out_p_4.write(f'''MOS Test Bench
* Include external file that contains MOSFET Model
.INCLUDE {path}
.INCLUDE techsweep_params.cir

** Circuit Description **
* power supply

vdsp dp 0 dc=0 
vgsp gp 0 dc=0
vbsp bp 0 dc={{sb}}  

* circuit
mp dp gp 0 bp {model[1]} L={{Len}} W={width}u

*sweep
.DC vgsp -{vgs_min} -{vgs_max} -{vgs_step} vdsp -{vds_min} -{vds_max} -{vds_step}
.TEMP {temp}
*saving parameters
.save i(vdsp) @mp[gm] @mp[gmbs] @mp[gds] @mp[cgg] @mp[cgs] @mp[cgd] @mp[cdd] @mp[cbs] @mp[vdsat]

.end''')
            out_p_4.close()

    return


techsweep_config_ngspice('D:\\Grad_Project\\Github\\task5\\130nm_bulk.LIB', 4, 27, 0, 0.1, 1, 0, 0.5, 1)