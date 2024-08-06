import Src.Directory_manage as dm
import pandas as pd
import numpy as np
import os


def load_igrf_coeff(time):
    prj_msg = dm.project_msg.project_msg()
    data_path = prj_msg['Project_path'] + '\\' + 'Data'
    file_full_path = os.path.join(data_path, 'igrf13_coeff.npy')
    if os.path.exists(file_full_path):
        igrf_coeff = np.load(file_full_path, allow_pickle=True).item()
    else:
        assert os.path.isfile(data_path + '\\igrf13_coeff.txt'), "在Data文件夹中未找到模型参数"
        igrf_coeff = {'year': list(), 'g': list(), 'h': list(), 'gh': list(), 'slope': list()}
        data = pd.read_csv(data_path + '\\igrf13_coeff.txt', sep='\s+')
        igrf_coeff['year'] = list(data.columns[3:])
        for i, year in enumerate(igrf_coeff['year']):
            length_ = np.where(data[year] != 0)
            length = length_[0][-1] + 1
            n = data['n'][length - 1]
            m = n + 1
            g = np.zeros([n, m])
            h = np.zeros([n, m])
            gh = np.zeros([length, 1])
            for j, elem in enumerate(data[year][0:length]):
                gh[j] = elem
                match data['g/h'][j]:
                    case 'g':
                        n_i = data['n'][j] - 1
                        m_i = data['m'][j]
                        g[n_i, m_i] = elem
                    case 'h':
                        n_i = data['n'][j] - 1
                        m_i = data['m'][j]
                        h[n_i, m_i] = elem
            if year is igrf_coeff['year'][-1]:
                igrf_coeff['slope'].append(1)
                gh = np.append(gh, np.zeros([1, 1]), axis=0)
            else:
                igrf_coeff['slope'].append(0)
            igrf_coeff['g'].append(g)
            igrf_coeff['h'].append(h)
            igrf_coeff['gh'].append(gh)
        np_file = os.path.join(data_path, 'igrf13_coeff_pro.npy')
        np.save(np_file, igrf_coeff)
    assert time > int(igrf_coeff['year'][0]) and time < int(igrf_coeff['year'][-1]), "igrf:time out of range."
    temp = list(map(lambda x: int(x) - time, igrf_coeff['year']))
    lastepoch = np.where(np.array(temp) < 0)[0][-1]
    nextepoch = np.where(np.array(temp) < 0)[0][-1] + 1
    lastgh = igrf_coeff['gh'][lastepoch]
    nextgh = igrf_coeff['gh'][nextepoch]
    if len(lastgh) > len(nextgh):
        smalln = len(nextgh)
        nextgh = np.zeros(shape=(len(lastgh), 1))
        nextgh[:smalln] = np.asarray(igrf_coeff['gh'][nextepoch])
    elif len(lastgh) < len(nextgh):
        smalln = len(lastgh)
        lastgh = np.zeros(shape=(len(nextgh), 1))
        lastgh[:smalln] = np.asarray(igrf_coeff['gh'][lastepoch])
    if igrf_coeff['slope'][nextepoch] == 1:
        ghslope = nextgh
    else:
        ghslope = (nextgh - lastgh) / (int(igrf_coeff['year'][nextepoch]) - int(igrf_coeff['year'][lastepoch]))
    gh_now = lastgh + ghslope * (time - int(igrf_coeff['year'][lastepoch]))
    return gh_now

