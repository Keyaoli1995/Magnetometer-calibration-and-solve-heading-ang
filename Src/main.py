import Load as Ld
import mag_init


# 文件夹操作

# 导入磁力计数据
file_path = {'mag_data_p': 'C:\\User_Bynav\\lky\\测试数据\\20240729\\1\\ist.dat',
             'ins_data_p': ''}
data_mag = Ld.load_data.load_mag_data(file_path['mag_data_p'])
print(dir(Ld))
print(data_mag)
a = mag_init.Magnetormeter()
# 确定系统时间

# 匹配航向角

# 磁力计校准补偿

# 调平

# 计算磁航向角

# 转换至地理航向角