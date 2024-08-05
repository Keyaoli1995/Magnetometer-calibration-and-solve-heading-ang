from Src import Load
import datenum as dn
import math
import numpy as np


def cal_geomagnetism_s(lati, longi, altitude, date):
    """calculate geomagnetism for given latitude, longitude altitude and date"""
    """initial earth para"""
    earth_para = Load.load_earth_para.load_earth_para()
    """check input valid"""
    if isinstance(date, str):
        time = dn.datenum(date)
    check_list = [lati, longi, altitude]
    for i in check_list:
        assert type(i) is float, "仅接受Python基本浮点类型作为纬经高的输入"

    """spherical coordinate conversion"""
    costheta = math.cos((math.radians(90) - math.radians(lati)))
    sintheta = math.sin((math.radians(90) - math.radians(lati)))
    a = earth_para['Re']
    b = a * (1 - earth_para['f'])
    rho = math.hypot(a * sintheta, b * costheta)
    r = math.sqrt(altitude ** 2 + 2 * altitude * rho + (a ** 4 * sintheta ** 2 + b ** 4 * costheta ** 2) / rho ** 2)
    print(r)
    cd = (altitude +rho) / r
    sd = (a ** 2 - b ** 2) / rho * costheta * sintheta / r
    oldcos = costheta
    costheta = costheta * cd - sintheta * sd
    sintheta = sintheta * cd + oldcos * sd
    phi = math.radians(longi)

    """get proper igrf coefficients"""
    gh = Load.load_igrf_para.load_igrf_para(time)
    #nmax = math.sqrt(len(gh) + 1) - 1







if __name__ == '__main__':
    cal_geomagnetism_s(28.0, 112.0, 3.0, '2023-03-01')