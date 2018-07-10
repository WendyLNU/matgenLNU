# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:春梅
from pymatgen.ext.matproj import MPRester
from pymatgen.electronic_structure.core import Spin
#This initiliazes the Rest connection to the Materials Project db. Put your own API key if needed.
#这个初始化的其余连接到材料项目DB。如果需要的话，你可以把你自己的api键放上去。
a = MPRester("hvSDrzMafUtXE0JQ")
#load the band structure from mp-3748, CuAlO2 from the MP db
#从mp-3748加载频段带结构，从mp dB加载cualo2
bs = a.get_bandstructure_by_material_id("mp-3748")
#is the material a metal (i.e., the fermi level cross a band)
#输出是金属的材料（即费米级交叉带）
print(bs.is_metal())
#print information on the band gap
#禁带宽度(Band gap)是指一个带隙宽度(单位是电子伏特(ev))，固体中电子的能量是不可以连续取值的，而是一些不连续的能带，要导电就要有自由电子或者空穴存在，自由电子存在的能带称为导带(能导电)，自由空穴存在的能带称为价带(亦能导电)
print(bs.get_band_gap())
#print the energy of the 20th band and 10th kpoint
#打印20波段和10坐标的计算能带的能量（我只查到这个计算能带是vasp中的内容，kpoint是对应的坐标，具体对于VASP我也不是很了解）
print(bs.bands[Spin.up][20][10])
#print energy of direct band gap
print(bs.get_direct_band_gap())
#print information on the vbm
print(bs.get_vbm())

#%matplotlib inline
from pymatgen.electronic_structure.plotter import BSPlotter
plotter = BSPlotter(bs)
plotter.get_plot().show()
plotter.plot_brillouin()
