from pymatgen import Molecule

coords = [[0.000000, 0.000000, 0.000000],
          [0.000000, 0.000000, 1.089000],
          [1.026719, 0.000000, -0.363000],
          [-0.513360, -0.889165, -0.363000],
          [-0.513360, 0.889165, -0.363000]]
mol = Molecule(["C", "H", "H", "H", "H"], coords)
print("mol:",mol)
print("\n")

print("mol[0]:",mol[0])
print("mol[1]:",mol[1])
print("\n")

#断连index为0和1两个原子之间的化学键，有上面的输出可以看到这两个位c和H,但是很奇怪为何会出现如下的结果？可能与空间结构有关系？
for frag in mol.break_bond(0, 1):
    print("frag:",frag)
print("\n")

print("neighbors of mol[0]:", mol.get_neighbors(mol[0], 3))
#得到分子中的共价键
print("covalent_bonds of:",mol.get_covalent_bonds())
print("\n")

#Creates a Structure from a Molecule by putting the Molecule in
#the center of a orthorhombic box. Useful for creating Structure
#for calculating molecules using periodic codes.
#通过把分子放在正交晶（orthorhombic）的盒子box里，从分子Molecule生存结构Structure。
#创建结构Structure，用于通过周期代码计算分子。
structure = mol.get_boxed_structure(10, 10, 10)
print("structure:",structure)

#xyz format是用来表示分子几何结构的文件，需要定分子中原子的坐标。
from pymatgen.io.xyz import XYZ
xyz = XYZ(mol)
xyz.write_file("methane.xyz")