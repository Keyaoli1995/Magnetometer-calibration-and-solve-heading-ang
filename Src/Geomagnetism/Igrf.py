from Src import Load
import Src.Geomagnetism.datenum as dn
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
    cd = (altitude +rho) / r
    sd = (a ** 2 - b ** 2) / rho * costheta * sintheta / r
    oldcos = costheta
    costheta = costheta * cd - sintheta * sd
    sintheta = sintheta * cd + oldcos * sd
    phi = math.radians(longi)

    """get proper igrf coefficients"""
    gh = Load.load_igrf_para.load_igrf_coeff(time)
    nmax = math.sqrt(len(gh) + 1) - 1

    """cos(m*phi) and sin(m*phi)"""
    cosphi = np.cos(np.array([i for i in range(1,int(nmax) + 1)]) * phi)
    sinphi = np.sin(np.array([i for i in range(1,int(nmax) + 1)]) * phi)
    Pmax = (nmax + 1) * (nmax + 2) / 2

    """magetic field calculation"""
    Br = 0
    Bt = 0
    Bp = 0
    P = np.zeros(shape=(int(Pmax), 1))
    P[0] = 1
    P[2] = sintheta
    dP = np.zeros(shape=(int(Pmax), 1))
    dP[0] = 0
    dP[2] = costheta
    m = 1
    n = 0
    coefindex = 1
    a_r = (earth_para['R0'] / r) ** 2
    for Pindex in range(2, int(Pmax)):
        if n < m:
            m = 0
            n = n + 1
            a_r = a_r * (earth_para['R0'] / r)
        if m < n and Pindex != 3:
            last1n = Pindex - n
            last2n = Pindex - 2 * n + 1
            P[Pindex - 1] = (2 * n - 1)/np.sqrt(n**2 - m**2) * costheta * P[last1n - 1] - np.sqrt(((n - 1)**2 - m**2) / (n**2 - m**2)) * P[last2n - 1]
            dP[Pindex - 1] = (2 * n - 1)/np.sqrt(n**2 - m**2) * (costheta * dP[last1n - 1] - sintheta * P[last1n - 1]) - np.sqrt(((n - 1)**2 - m**2) / (n**2 - m**2)) * dP[last2n - 1]
        elif Pindex != 3:
            lastn = Pindex - n - 1
            P[Pindex - 1] = np.sqrt(1 - 1/(2 * m)) * sintheta * P[lastn - 1]
            dP[Pindex - 1] = np.sqrt(1 - 1/(2 * m)) * (sintheta * dP[lastn - 1] + costheta * P[lastn - 1])
        if m == 0:
            coef = a_r * gh[coefindex - 1]
            Br = Br + (n + 1) * coef * P[Pindex -1]
            Bt = Bt - coef * dP[Pindex - 1]
            coefindex = coefindex + 1
        else:
            coef = a_r * (gh[coefindex - 1] * cosphi[m - 1] + gh[coefindex] * sinphi[m - 1])
            Br = Br + (n + 1) * coef * P[Pindex -1]
            Bt = Bt - coef * dP[Pindex - 1]
            if sintheta == 0:
                Bp = Bp - costheta * a_r * (-gh[coefindex - 1] * sinphi[m - 1] + gh[coefindex] * cosphi[m - 1]) * dP[Pindex - 1]
            else:
                Bp = Bp - 1/sintheta * a_r * m * (-gh[coefindex - 1] * sinphi[m - 1] + gh[coefindex] * cosphi[m - 1]) * P[Pindex - 1]
            coefindex = coefindex + 2
        m = m + 1
    Bx = -Bt
    By = Bp
    Bz = -Br

    Bx_old = Bx
    Bx = Bx * cd + Bz * sd
    Bz = Bz * cd - Bx_old * sd
    
    return Bx, By, Bz








if __name__ == '__main__':
    Bx, By, Bz = cal_geomagnetism_s(38.0, 105.0, 100.0, '2019-08-01')
    print(Bx, By, Bz)