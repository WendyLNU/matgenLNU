from pymatgen import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.transformations.advanced_transformations import EnumerateStructureTransformation
from pymatgen.io.vasp.sets import batch_write_input, MPRelaxSet
structure = Structure.from_file("D:/Program Files (x86)/python2/file/EntryWithCollCode418490.cif")
# （获取文件 当在自己电脑中调试的时候需要将相关的路径统一一下）
print(structure)
# loop over all sites in the structure
for i, site in enumerate(structure):
    # （enumerate 为枚举类型）
    # change the occupancy of Li+ disordered sites to 0.5
    if not site.is_ordered:
        structure[i] = {"Li+": 0.5}
print("The composition after adjustments is %s." % structure.composition.reduced_formula)
analyzer = SpacegroupAnalyzer(structure)
#   SpacegroupAnalyzer为空间群分析  晶体内部结构中全部对称要素的集合称为 “空间群” 。
#   一切晶体结构中总共只能有230种不同的对称要素组合方式，即230个空间群所谓点空间群，
#   是由一个平移群和一个点群对称操作组合而成的，它的一般对称操作可以写成（R | t (αβγ)），其中R表示点群对称操作，t(αβγ)表示平移操作
#   为了保持可排序的顺序，我们只在原始单元上执行枚举。原始单元可以使用*空间群分析器*获得
prim_cell = analyzer.find_primitive()
print(prim_cell)
enum = EnumerateStructureTransformation() # 变换枚举结构
enumerated = enum.apply_transformation(prim_cell, 90)  # 在这需要限制返回结构的数量
structures = [d["structure"] for d in enumerated]
print("%d structures returned." % len(structures))