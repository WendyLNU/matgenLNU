from  pymatgen.electronic_structure.cohp  import Cohp
from pymatgen.electronic_structure.plotter import CohpPlotter
from pymatgen.io.lobster import Cohpcar

COHPCAR_path = "E:/Python/pymatgen-master/test_files/cohp/COHPCAR.lobster"
#源代码是："COHPCAR_path = \"/Users/shyuep/repos/pymatgen/test_files/cohp/COHPCAR.lobster"
cohpcar = Cohpcar(filename=COHPCAR_path)
#获取COHPCAR文件的名称
cdata = cohpcar.cohp_data
cdata_processed = {}
#测试上传是否成功
for key in cdata:
    # PYTHON里的for循环
    c = cdata[key]
    c["efermi"] = 0
    c["energies"] = cohpcar.energies
    c["are_coops"] = False
    cdata_processed[key] = Cohp.from_dict(c)
    # 返回完整的Cohp对象
cp = CohpPlotter()
cp.add_cohp_dict(cdata_processed)
x = cp.get_plot()
x.ylim([-6, 6])
x.show()
#结果展示函数

