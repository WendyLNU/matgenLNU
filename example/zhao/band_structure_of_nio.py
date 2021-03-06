import pymatgen as mg
from pymatgen.io.vasp.outputs import BSVasprun, Vasprun
from pymatgen import Spin
from pymatgen.electronic_structure.plotter import BSPlotter, BSDOSPlotter, DosPlotter

import matplotlib.pyplot as plt



#The file "vasprun.xml" is in aim_data. Rename it after unzip.
run = BSVasprun("vasprun.xml", parse_projected_eigen=True)

bs = run.get_band_structure("KPOINTS")#得到计算能带，（我只查到这个计算能带是vasp中的内容，kpoint是对应的坐标，具体对于VASP我也不是很了解）

print("number of bands", bs.nb_bands)
print("number of kpoints", len(bs.kpoints))

print(bs.is_metal())
print(bs.is_spin_polarized)

print(bs.bands)

print(bs.bands[Spin.up].shape)
print(bs.bands[Spin.down][163,:])
for kpoints,e in zip(bs.kpoints,bs.bands[Spin.down][163,:]):
   print("kx = %5.3f ky = %5.3f kz = %5.3f eps(k) = %8.4f" % (tuple(kpoints.frac_coords) + (e,)))


bsplot = BSPlotter(bs)#这个代码有点错误，好像是跟类型有关，我还没有弄明白





#ax = plt.gca()
#ax.set_title("NiO Band Structure", fontsize=20)
#xlim = ax.get_xlim()
#ax.hlines(0,xlim[0],xlim[1],linestyles="dashed",color="black")
#ax.plot((),(),"b-",label="spin up")
#ax.plot((),(),"r--",label="spin down")
#ax.legend(fontsize=16,loc="upper left")









