from pymatgen import Structure
from pymatgen.io.vasp.sets import MPRelaxSet

s = Structure.from_file("ICSD_182730_Si.cif", primitive=True)
custom_settings = {"NELMIN": 5} # user custom incar settings
relax = MPRelaxSet(s, user_incar_settings=custom_settings)
relax.write_input("Si-relax")