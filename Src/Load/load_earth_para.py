

def load_earth_para():
    earth_para = dict()
    earth_para['R0'] = 6371.2E3
    earth_para['Re'] = 6378137
    earth_para['f'] = 1 / 298.257223561
    earth_para['Rp'] = -(earth_para['Re'] * earth_para['f'] - earth_para['Re'])
    return earth_para
