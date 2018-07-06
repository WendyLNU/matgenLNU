import re
from pymatgen.entries.computed_entries import ComputedEntry
from pymatgen.entries.compatibility import MaterialsProjectCompatibility
from  pymatgen  import MPRester#REST API的适配器
#To do our testing, let's use the MPRester to get a sample computed entry from the Materials Project.
m = MPRester("S3lw1QomLO8bTiT7")#将API 秘钥输入适配器中，并且初始化适配器
entries = m.get_entries("LiFePO4")
entry = entries[0]
compat = MaterialsProjectCompatibility()#实现了GGA / GGA + U混合方案，允许混合条目，这应仅用于使用MaterialsProject参数进行VASP计算
compat.explain(entry)#打印显示出entry中的信息
