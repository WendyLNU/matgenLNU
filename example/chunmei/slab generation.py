# Import the neccesary tools to generate surfaces
from pymatgen.core.surface import SlabGenerator, generate_all_slabs, Structure, Lattice
# Import the neccesary tools for making a Wulff shape
from pymatgen.analysis.wulff import WulffShape

import os

lattice = Lattice.cubic(3.508)

Ni = Structure(lattice, ["Ni", "Ni", "Ni", "Ni"],
               [[0,0,0], [0,0.5,0],
                [0.5,0,0], [0,0,0.5]
               ])
slabgen = SlabGenerator(Ni, (1,1,1), 10, 10)

lattice = Lattice.cubic(5.46873)
Si = Structure(lattice, ["Si", "Si", "Si", "Si",
                         "Si", "Si", "Si", "Si"],
               [[0.00000, 0.00000, 0.50000],
                [0.75000, 0.75000, 0.75000],
                [0.00000, 0.50000, 0.00000],
                [0.75000, 0.25000, 0.25000],
                [0.50000, 0.00000, 0.00000],
                [0.25000, 0.75000, 0.25000],
                [0.50000, 0.50000, 0.50000],
                [0.25000, 0.25000, 0.75000]])

slabgen = SlabGenerator(Si, (1,1,1), 10, 10)
print("Notice now there are actually now %s terminations that can be \
generated in the (111) direction for diamond Si" %(len(slabgen.get_slabs())))