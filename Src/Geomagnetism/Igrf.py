from Src import Load
import numpy as np
import datenum as dn

def cal_geomagnetism_s(lati, longi, altitude, date):
    """initial earth para"""
    earth_para = Load.load_earth_para.load_earth_para()
    """check input valid"""
    if isinstance(date, str):
        time = dn.datenum(date)
    check_list = [lati, longi, altitude]
    for i in check_list:
        assert type(i) is not np.ndarray, "仅接受Python基本类型作为纬经高的输入"




if __name__ == '__main__':
    cal_geomagnetism_s(1, 2, 3, '2024-08-01')