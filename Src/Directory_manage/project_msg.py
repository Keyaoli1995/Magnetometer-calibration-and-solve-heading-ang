import os


def project_msg():
    pth_lib = dict()
    pth_lib['sys_name'] = os.name
    basename = os.path.basename(os.path.dirname(__file__))
    abspath = os.path.abspath(os.path.dirname(__file__))
    while basename != 'Src':
        basename = os.path.basename(os.path.dirname(abspath))
        abspath = os.path.dirname(abspath)
    Project_path = os.path.dirname(abspath)
    pth_lib['Project_path'] = Project_path
    Project_1st_directory = os.listdir(Project_path)
    pth_lib['Project_1st_directory'] = Project_1st_directory
    return pth_lib
