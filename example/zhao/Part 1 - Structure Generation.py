from pymatgen import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer#空间群分析器
from pymatgen.transformations.advanced_transformations import EnumerateStructureTransformation#枚举结构转换
from pymatgen.io.vasp.sets import batch_write_input, MPRelaxSet

structure = Structure.from_file("G:/Python/files/EntryWithCollCode418490.cif")#我们将首先从ICSD中发现的晶体学信息文件（CIF）中读取结构
print(structure)
#目前我们所拥有的结构是无序的，并且Li的占有率跟成分不符合，需要调整
# loop over all sites in the structure在结构中所有的位置进行循环
for i, site in enumerate(structure):
    # change the occupancy of Li+ disordered sites to 0.5（也就是把结构矩阵中的Li+那一列调整为0.5）
    if not site.is_ordered:
        structure[i] = {"Li+": 0.5}
print("The composition after adjustments is %s." % structure.composition.reduced_formula)#获得化学计量电荷平衡的L6PS5Cl。

#为了保持可排序的顺序，我们只在原始单元上执行枚举。原始单元可以使用空间群分析器获得
analyzer = SpacegroupAnalyzer(structure)
prim_cell = analyzer.find_primitive()#找到原始单元，并且作为Structure对象返回
print(prim_cell)

#我们将使用枚举结构结构转换类来枚举所有对称的不同结构。枚举结构是一个围绕枚举库的用户友好包装器，它是由HART等人编写的派生结构的FORTRAN库
enum = EnumerateStructureTransformation()
enumerated = enum.apply_transformation(prim_cell, 100)  # return no more than 100 structures
#structures = [d["structure"] for d in enumerated]
#print("%d structures returned." % len(structures))
