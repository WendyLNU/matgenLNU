import pymatgen as mg
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun
from pymatgen import Spin
from pymatgen.electronic_structure.plotter import BSPlotter, BSDOSPlotter, DosPlotter

import matplotlib.pyplot as plt

#The file "vasprun.xml" is in aim_data. Rename it after unzip.
run = BSVasprun("vasprun.xml", parse_projected_eigen=True)

bs = run.get_band_structure("KPOINTS")

print("number of bands", bs.nb_bands)
print("number of kpoints", len(bs.kpoints))