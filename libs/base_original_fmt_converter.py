from libs import common
from tqdm import tqdm
import vtkmodules.all as vtk
from abc import ABCMeta, abstractmethod

class BaseOriginalFmtConverter(metaclass=ABCMeta):
    def __init__(self, out_file, vtk_obj_data):
        self.out_file = out_file
        self.vtk_obj_data = vtk_obj_data
        self.object_3d = common.Object3D()

    def execute(self):
        print("Now parsing...")
        self.parse()
        print("Done parsing.")
        print("")
        print("Now writing...")
        self.write()
        print("Done writing.")

    def parse(self):
        # Pack points into object_3d.points.
        num_points = self.vtk_obj_data.GetNumberOfPoints()
        print("num_total_points:", num_points)
        for point_id in tqdm(range(num_points)):
            point = self.vtk_obj_data.GetPoint(point_id)  # これでやっと頂点座標にアクセスできる。
            x = point[0]
            y = point[1]
            z = point[2]
            self.object_3d.points.append([x, y, z])

        # Pack cell into object_3d.cells.
        num_cells = self.vtk_obj_data.GetNumberOfCells()
        print("num_total_cells:", num_cells)
        for cell_id in tqdm(range(num_cells)):
            # print("cell:", cell_id)
            cell_data = self.vtk_obj_data.GetCell(cell_id)
            cell_point_ids = vtk.vtkIdList()
            self.vtk_obj_data.GetCellPoints(cell_id, cell_point_ids)
            num_cell_point_ids = cell_point_ids.GetNumberOfIds()

            cell_point_id_pylist = list()  # python-list
            for local_point_id in range(num_cell_point_ids):
                global_point_id = cell_point_ids.GetId(local_point_id)
                cell_point_id_pylist.append(global_point_id)
            self.object_3d.cells.append(cell_point_id_pylist)

            # Pack cell_type into object_3d.cell_types.
            cell_type = cell_data.GetCellType()
            # print(cell_type)
            self.object_3d.cell_types.append(cell_type)

        print("Completed parsing.")

    @abstractmethod
    def write(self):
        pass


if __name__ == "__main__":
    # obj_3d_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.stl"
    obj_3d_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.vtk"
    # obj_3d_file = "/home/ksato/ExternalSSD1T/dataset/vtk/test5.vtk"
    out_fmt1_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.fmt1"

    # stl_reader = vtk.vtkSTLReader()
    obj_reader = vtk.vtkDataSetReader()
    obj_reader.SetFileName(obj_3d_file)
    obj_reader.Update()

    stl_data = obj_reader.GetOutput()
    writer = BaseOriginalFmtConverter(out_fmt1_file, stl_data)
    writer.execute()
