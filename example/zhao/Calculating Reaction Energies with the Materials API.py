from pymatgen.ext.matproj import MPRester#REST API的适配器
from pymatgen import Composition#可以非常灵活的处理化学元素
from pymatgen.entries.computed_entries import ComputedEntry#从数据获取的数据生成的ComputedEntries列表，主要用于管理数据的
from pymatgen.core.units import FloatWithUnit#相关化学计算的单位转换功能
from pymatgen.analysis.reaction_calculator import ComputedReaction#通过化学反应物和化学反应生成物生成化学反应的类

#This initializes the REST adaptor. Put your own API key in if necessary.
a = MPRester("S3lw1QomLO8bTiT7")#将API 秘钥输入适配器中，并且初始化适配器

#得到包含Ca.C O三种元素的所有化学式的所有条目
all_entries = a.get_entries_in_chemsys(['Ca', 'C', 'O'])#获取MP数据库中的所有ComputedEntries列表

#找出所有条目中能量最低的化学式信息
def get_most_stable_entry(formula):
    relevant_entries = [entry for entry in all_entries if entry.composition.reduced_formula == Composition(formula).reduced_formula]
    relevant_entries = sorted(relevant_entries, key=lambda e: e.energy_per_atom)
    return relevant_entries[0]

CaO = get_most_stable_entry("CaO")
CO2 = get_most_stable_entry("CO2")
CaCO3 = get_most_stable_entry("CaCO3")

reaction = ComputedReaction([CaO, CO2], [CaCO3])#得到化学反应
energy = FloatWithUnit(reaction.calculated_reaction_energy, "eV atom^-1")#计算化学反应的能量，并且转换单位

print("Caculated")
print(reaction)
print("Reaction energy = {}".format(energy.to("kJ mol^-1")))


# The following portions demonstrate how to get the experimental values as well.
exp_CaO = a.get_exp_entry("CaO")#获得ExpEntry对象，可用于实验数据分析
exp_CaCO3 = a.get_exp_entry("CaCO3")

#Unfortunately, the Materials Project database does not have gas phase experimental entries. This is the value from NIST. We manually create the entry.
#这是一个气相实验，而且数据库没有关于这个的数据条目，所以我们要自己创建
#NIST是化学信息的标准参考数据库
exp_CO2 = ComputedEntry("CO2", -393.51)#Exp entries should be in kJ/mol.

exp_reaction = ComputedReaction([exp_CaO, exp_CO2], [exp_CaCO3])

print("Experimental")
print(exp_reaction)
print("Reaction energy = {} kJ mol^-1".format(exp_reaction.calculated_reaction_energy))