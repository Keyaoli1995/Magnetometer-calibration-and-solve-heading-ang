import Src.Directory_manage as dm
import Src.mag_init

"""这是一个练习代码"""
# 文件夹操作 os 模块 练习
prj_msg = dm.project_msg.project_msg()
print(prj_msg)
ist_8310 = Src.mag_init.Magnetormeter()
ist_8310.show_mag()
ist_8310.read_mag_data_from("C:\\User_Bynav\\lky\\测试数据\\20240729\\1\\ist.dat")
ist_8310.show_mag()
