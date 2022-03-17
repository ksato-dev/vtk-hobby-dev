import sys
sys.path.append(
    "/home/ksato/ExternalSSD1T/VTK/build/lib/python3.8/site-packages/")


class Object3D(object):
    def __init__(self):
        self.points = list(list())
        self.cells = list(list())
        self.cell_types = list()


def CellType2Str(cell_type):
    ret_str = "unkwnon"
    if cell_type == 5:
       ret_str = "tri"
    elif cell_type == 10:
       ret_str = "tetra"
    return ret_str