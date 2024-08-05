import Src.Directory_manage as dm
import os
import re


def load_igrf_para(time):
    print("load_igrf_para func")
    prj_msg = dm.project_msg.project_msg()
    data_path = prj_msg['Project_path'] + '\\' + 'Data'
    assert os.path.isfile(data_path+'\\igrf13_coeff.txt'), "在Data文件夹中未找到模型参数"
    igrf_coeff = {'year': list(), 'g': list(), 'h': list(), 'gh': list(), 'slope': list()}
    with open(data_path+'\\igrf13_coeff.txt', 'r') as f:
        file_len = len(f.readlines())
        f.seek(0,0)
        count_ = 0
        count_e = 0
        while count_ < file_len:
            line = f.readline().strip()
            count_ += 1
            if line.startswith('g/h'):
                patten = r'\d+(?=\.)'
                yaer = re.findall(patten, line)
                patten = r'\d+(?=20-)(?<=20-)\d+'
                year_last = re.findall(patten, line)
                print(yaer)
    print(igrf_coeff)
