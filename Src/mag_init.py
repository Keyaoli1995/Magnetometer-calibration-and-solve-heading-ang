import numpy as np
import Src.Load.load_data as ld


class Magnetormeter():
    def __init__(self):
        self.data_mag = np.array([0, 0, 0, 0])

    def show_mag(self):
        print(self.data_mag)

    def read_mag_data_from(self, abs_path):
        self.data_mag = ld.load_mag_data(abs_path)
