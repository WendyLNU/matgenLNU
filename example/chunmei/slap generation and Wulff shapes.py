# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:春梅
# Import the neccesary tools to generate surfaces导入必要的工具以生成表面
from pymatgen.core.surface import SlabGenerator, generate_all_slabs, Structure, Lattice
# Import the neccesary tools for making a Wulff shape
#为制作Wulff形状导入必要的工具(Wulff没有查出特定的意思，我觉得可能是一个人名，表示记忆性）
from pymatgen.analysis.wulff import WulffShape
import os
# Let's start with fcc Ni  (fcc(Food Chemicals Codex)《食品化学法典》(FCC) 是国际公认的标准各论，用于验证食品成分的纯度及特性。)
lattice = Lattice.cubic(3.508)#lattice:点阵一个长度为a的立方体
Ni = Structure(lattice, ["Ni", "Ni", "Ni", "Ni"],
               [[0,0,0], [0,0.5,0],
                [0.5,0,0], [0,0,0.5]
               ])#先创建出Ni晶体的结构
# We'll use the SlabGenerator class to get a single slab. We'll start with the
# (111) slab of Ni. Plug in the CONVENTIONAL unit cell of your structure, the
# maximum Miller index value to generate the different slab orientations along
# with the minimum slab and vacuum size in Angstroms
#该类使用由何处决定的移位值生成不同的板
#一个独特的终止可以和其他标准一起找到，比如
#终止不会破坏多面体的键。移动值然后指示
#平板层将在真空系统中开始和结束。
slabgen = SlabGenerator(Ni, (1,1,1), 10, 10)
# If we want to find all terminations for a particular Miller index orientation,
# we use the get_slabs() method. This returns a LIST of slabs rather than a single
# slab. When generating a slab for a particular orientation, there are sometimes
# more than one location we can terminate or cut the structure to create a slab. The
# simplest example of this would be the Si(Fd-3m) (111) slab which can be cut or
# terminated in two different locations along the vector of the Miller index. For a
# fcc structure such as Ni however, there should only be one way to cut a (111) slab.
all_slabs = slabgen.get_slabs()
print("The Ni(111) slab only has %s termination." %(len(all_slabs)))#len返回容器中的项目数
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
all_slabs = generate_all_slabs(Si, 3, 10, 10)
print("%s unique slab structures have been found for a max Miller index of 3" %(len(all_slabs)))
# What are the Miller indices of these slabs?（晶面的米勒指数是用来表达晶面在晶体上之方向的一组无公约数的整数，他们的具体数值等于该晶面在结晶轴上所截截距的倒数比）
for slab in all_slabs:
    print(slab.miller_index)
print("Notice some Miller indices are repeated. Again, this is due to there being more than one termination")
# Now let's assume that we then calculated the surface energies for these slabs

# Surface energy values in J/m^2
surface_energies_Ni = {(3, 2, 0): 2.3869, (1, 1, 0): 2.2862,
                       (3, 1, 0): 2.3964, (2, 1, 0): 2.3969,
                       (3, 3, 2): 2.0944, (1, 0, 0): 2.2084,
                       (2, 1, 1): 2.2353, (3, 2, 2): 2.1242,
                       (3, 2, 1): 2.3183, (2, 2, 1): 2.1732,
                       (3, 3, 1): 2.2288, (3, 1, 1): 2.3039,
                       (1, 1, 1): 1.9235}
miller_list = surface_energies_Ni.keys()
e_surf_list = surface_energies_Ni.values()

# We can now construct a Wulff shape with an accuracy up to a max Miller index of 3
wulffshape = WulffShape(Ni.lattice, miller_list, e_surf_list)

# Let's get some useful information from our wulffshape object
print("shape factor: %.3f, anisotropy: \
%.3f, weighted surface energy: %.3f J/m^2" %(wulffshape.shape_factor,
                                       wulffshape.anisotropy,
                                       wulffshape.weighted_surface_energy))


# If we want to see what our Wulff shape looks like
wulffshape.show()
# Lets try something a little more complicated, say LiFePO4
from pymatgen.util.testing import PymatgenTest
# Get the LiFePO4 structure
LiFePO4 = PymatgenTest.get_structure("LiFePO4")

# Let's add some oxidation states to LiFePO4, this will be
# important when we want to take surface polarity into consideration
LiFePO4.add_oxidation_state_by_element({"Fe": 2, "Li": 1, "P": 5, "O": -2})
slabgen = SlabGenerator(LiFePO4, (0,0,1), 10, 10)
all_slabs = slabgen.get_slabs(bonds={("P", "O"): 2})
# any bond between P and O less than 2 Angstroms cannot be broken when generating slabs
print("For the (001) slab of LiFePO4, there are %s terminations." %(len(all_slabs)))
for slab in all_slabs:
    print(slab.is_polar(), slab.is_symmetric())
# Notice that none of the terminations in the (001) direction do not simultaneously satisfy
# our two criteria so a (001) surface with a reasonable surface energy cannot be calculated.
# In such cases, we need to modify the surfaces of our slabs. A future release of surface.py
# will implement such modification techniques for these cases.
# Now let's generate all possible slabs for a max Miller index of 2 for LiFePO4 and see if
# any of these surfaces can be calculated to yield reasonable and accurate surface energy
# values. This may take a while.
all_slabs = generate_all_slabs(LiFePO4, 2, 10, 10, bonds={("P", "O"): 2})
print("There is a total of %s slabs generated including polar, asymmetric, and \
P-O terminated slabs" %(len(all_slabs)))

# store any slabs for calculation that satisfies our criterias
valid_slabs = []
for slab in all_slabs:
    if not slab.is_polar() and slab.is_symmetric():
        print(slab.miller_index)
        valid_slabs.append(slab)

print("Number of slabs that are nonpolar, symmetric and do not terminate P-O bonds: %s" %(len(valid_slabs)))

