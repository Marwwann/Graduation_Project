import json
import pickle
import sys

class Object:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


if sys.argv[2] =="nmos":

    with open(sys.argv[1], "rb") as f:
        nch2 = pickle.load(f)

    nch2.L = nch2.L.tolist()
    nch2.VGS = nch2.VGS .tolist()
    nch2.VDS = nch2.VDS.tolist()
    nch2.VSB = nch2.VSB.tolist()

    nch2.ID = nch2.ID.tolist()
    nch2.GM = nch2.GM.tolist()
    nch2.GMBS = nch2.GMBS.tolist()
    nch2.GDS = nch2.GDS.tolist()
    nch2.CGG = nch2.CGG .tolist()
    nch2.CGS = nch2.CGS.tolist()
    nch2.CGD = nch2.CGD.tolist()
    nch2.CDD = nch2.CDD.tolist()
    nch2.CBS = nch2.CBS.tolist()
    print(nch2.to_json().replace(" ", ""))

elif sys.argv[2] == "pmos":
    with open('pch 65nm_bulk', "rb") as f:
        pch2 = pickle.load(f)
    pch2.L = pch2.L.tolist()
    pch2.VGS = pch2.VGS .tolist()
    pch2.VDS = pch2.VDS.tolist()
    pch2.VSB = pch2.VSB.tolist()

    pch2.ID = pch2.ID.tolist()
    pch2.GM = pch2.GM.tolist()
    pch2.GMBS = pch2.GMBS.tolist()
    pch2.GDS = pch2.GDS.tolist()
    pch2.CGG = pch2.CGG .tolist()
    pch2.CGS = pch2.CGS.tolist()
    pch2.CGD = pch2.CGD.tolist()
    pch2.CDD = pch2.CDD.tolist()
    pch2.CBS = pch2.CBS.tolist()

    print(pch2.to_json().replace(" ", ""))


