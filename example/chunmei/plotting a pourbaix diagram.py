# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:春梅
# Import necessary tools from pymatgen
from pymatgen import MPRester
from pymatgen.analysis.pourbaix_diagram import PourbaixDiagram, PourbaixPlotter
# %matplotlib inline
# Initialize the MP Rester
mpr = MPRester("hvSDrzMafUtXE0JQ")##将API 秘钥输入适配器中，并且初始化适配器，需要自己申请。
# Get all pourbaix entries corresponding to the Cu-O-H chemical system.
entries = mpr.get_pourbaix_entries(["Cu"])
# Construct the PourbaixDiagram object
pbx = PourbaixDiagram(entries)
# Get an entry stability as a function of pH and V
entry = [e for e in entries if e.entry_id == 'mp-1692'][0]
print("CuO's potential energy per atom relative to the most",
      "stable decomposition product is {:0.2f} eV/atom".format(
          pbx.get_decomposition_energy(entry, pH=7, V=-0.2)))
plotter = PourbaixPlotter(pbx)
plotter.get_pourbaix_plot().show()
plt = plotter.plot_entry_stability(entry)
plt.show()
# Get all pourbaix entries corresponding to the Fe-O-H chemical system.
entries = mpr.get_pourbaix_entries(["Bi", "V"])
# Construct the PourbaixDiagram object
pbx = PourbaixDiagram(entries, comp_dict={"Bi": 0.5, "V": 0.5},
                      conc_dict={"Bi": 1e-8, "V": 1e-8}, filter_solids=True)
# Construct the pourbaix analyzer
plotter = PourbaixPlotter(pbx)
plt = plotter.get_pourbaix_plot()
plt.show()
bivo4_entry = [entry for entry in entries if entry.entry_id=="mp-613172"][0]
plt = plotter.plot_entry_stability(bivo4_entry)
bio2_entry = [entry for entry in entries if entry.entry_id=="mp-557993"][0]
plt = plotter.plot_entry_stability(bio2_entry)

