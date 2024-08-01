import numpy as np
import re


def load_mag_data_debug(file_abs_path):
    file = open(file_abs_path, 'r')
    file_content = file.readlines()
    file.close()
    row_count = len(file_content)
    patten = r'\d+.\d+'
    numbers_list = re.findall(patten, file_content[0])
    column_count = len(numbers_list)
    data_mag = np.zeros((row_count, column_count))
    data_mag[0, :] = np.asarray(numbers_list, np.float64)
    for i, line in enumerate(file_content[1:]):
        numbers_list = re.findall(patten, file_content[i + 1])
        data_mag[i + 1, :] = np.asarray(numbers_list, np.float64)
    return data_mag


def load_mag_data_device(file_abs_path):
    file = open(file_abs_path, 'r')
    file_content = file.readlines()
    file.close()
    row_count = len(file_content)
    patten = r'\-?\w+\.?\w+'
    numbers_list = re.findall(patten, file_content[0])
    column_count = len(numbers_list)
    data_mag = np.zeros((row_count, column_count))
    for i, line in enumerate(file_content):
        numbers_list = re.findall(patten, file_content[i])
        time_dec = int(numbers_list[0], 16)
        data_mag[i, 0] = np.uint64(time_dec)
        data_mag[i, 1:] = np.asarray(numbers_list[1:], np.float64)
    return data_mag


def load_mag_data(file_abs_path):
    keywords_argv = file_abs_path.split("\\")
    match keywords_argv[-1]:
        case 'ist.dat':
            data_mag = load_mag_data_device(file_abs_path)
        case _:
            data_mag = load_mag_data_debug(file_abs_path)
    return data_mag
