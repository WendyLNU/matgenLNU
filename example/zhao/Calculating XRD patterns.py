from pymatgen import Lattice, Structure
from pymatgen.analysis.diffraction.xrd import XRDCalculator
from IPython.display import Image, display


# Create CsCl structure
a = 4.209 #Angstrom(埃:一个长度单位，用来表示原子尺寸、键长和电磁波波长。)
latt = Lattice.cubic(a)
structure = Structure(latt, ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]])
c = XRDCalculator()
c.get_plot(structure, two_theta_range=(0, 90), annotate_peaks=True, ax=None, with_labels=True, fontsize=16)
#display(Image(filename=('./PDF - alpha CsCl.png')))
a = 6.923 #Angstrom
latt = Lattice.cubic(a)
structure = Structure(latt, ["Cs", "Cs", "Cs", "Cs", "Cl", "Cl", "Cl", "Cl"],
                      [[0, 0, 0], [0.5, 0.5, 0], [0, 0.5, 0.5], [0.5, 0, 0.5],
                       [0.5, 0.5, 0.5], [0, 0, 0.5], [0, 0.5, 0], [0.5, 0, 0]])

c.get_plot(structure, two_theta_range=(0, 90), annotate_peaks=True, ax=None, with_labels=True, fontsize=16)
#display(Image(filename=('./PDF - beta CsCl.png')))这段代码display我还没有弄明白，帮我看看哪里出问题了
