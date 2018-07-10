
# coding: utf-8
# # 介绍 Introduction
# 本笔记本演示了如何使用pymatgen接口获取材料项目中的各种数据。（This notebook demonstrates how you can obtain various data from the Materials Project using pymatgen's interface to the Materials API.）
from pymatgen import MPRester, Composition
import re
import pprint
# Make sure that you have the Materials API key. Put the key in the call to
# MPRester if needed, e.g, MPRester("MY_API_KEY")
mpr = MPRester("hvSDrzMafUtXE0JQ") #将API 秘钥输入适配器中，并且初始化适配器，需要自己申请。
comp = Composition("Fe2O3")# 获得带有材料标识的结构， 假设你想找到所有与fe2o3类似的化学计量结构
anon_formula = comp.anonymized_formula
# We need to convert the formula to the dict form used in the database.
anon_formula = {m.group(1): int(m.group(2)) 
                for m in re.finditer(r"([A-Z]+)(\d+)", anon_formula)}
data = mpr.query({"anonymous_formula": anon_formula}, 
                 properties=["task_id", "pretty_formula", "structure"])
print(len(data))  #Should show ~600 data.比较慢，多等一会儿。
# data now contains a list of dict. This shows you what each dict has.
# Note that the mp id is named "task_id" in the database itself.
pprint.pprint(data[0])
# # 得到“能带结构”（Getting band structures）
# 能带结构是相当大的物体。不建议你一次下载大量的绷带结构，而是直接下载你需要的。Band structures are fairly large objects. It is not recommended that you download large quantities of bandstructures in one shot, but rather just download the ones you need.
bs = mpr.get_bandstructure_by_material_id("mp-20470")#这个是material上对应的编号，需要自己去查找写自己需要的
from pymatgen.electronic_structure.plotter import BSPlotter
# %matplotlib inline
plotter = BSPlotter(bs)
plotter.show()
elastic_data = mpr.query({"elasticity": {"$exists": True}},
                         properties=["task_id", "pretty_formula", "elasticity"])
print(len(elastic_data))
pprint.pprint(elastic_data[0])
# # More resources
# In general, almost any data can be obtained from MP using the MPRester, either via the high-level functions or the very powerful "query" method.
# For more complex queries, you can refer to the documentation for the Materials API at https://github.com/materialsproject/mapidoc.
# # Fitting structures
# Pymatgen has its own structure matching algorithm, which we have used to effectively reduce the 130,000 structures in ICSD to ~60,000 - 70,000 structures. It is fast and accurate. Here's an example of how it works.
from pymatgen.analysis.structure_matcher import StructureMatcher
m = StructureMatcher() # You can customize tolerances etc., but the defaults usually work fine.
s1 = data[0]["structure"]
print(s1)
s2 = s1.copy()
s2.apply_strain(0.1)
print(s2)
print(m.fit(s1, s2))
# For something more challenging, let's see how many structures are similar to Gd2O3
matches = []
for d in data:
    if m.fit_anonymous(d["structure"], s1):
        matches.append(d)
# The above fitting took a few seconds. We have 32 similar structures.
print(len(matches))
# Let's see a few of the matches.
pprint.pprint(matches[0])
pprint.pprint(matches[1])
pprint.pprint(matches[2])

