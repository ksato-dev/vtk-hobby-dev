import sys
sys.path.append(
    "/home/ksato/ExternalSSD1T/VTK/build/lib/python3.8/site-packages/")
import vtkmodules.all as vtk
from base_vtk_legacy_converter import BaseVtkLegacyConverter


class STLToVtkLegacyConverter(BaseVtkLegacyConverter):
    def ReadFile(self, in_file_name):
        obj_reader = vtk.vtkSTLReader()
        obj_reader.SetFileName(in_file_name)
        obj_reader.Update()

        vtk_obj_data = obj_reader.GetOutput()
        # Pack points into object_3d.points.
        num_points = vtk_obj_data.GetNumberOfPoints()
        print("num_total_points:", num_points)
        for point_id in range(num_points):
            point = vtk_obj_data.GetPoint(point_id)  # これでやっと頂点座標にアクセスできる。
            x = point[0]
            y = point[1]
            z = point[2]
            self.object_3d.points.append([x, y, z])

        # Pack cell into object_3d.cells.
        num_cells = vtk_obj_data.GetNumberOfCells()
        print("num_total_cells:", num_cells)
        for cell_id in range(num_cells):
            # print("cell:", cell_id)
            cell_data = vtk_obj_data.GetCell(cell_id)
            cell_point_ids = vtk.vtkIdList()
            vtk_obj_data.GetCellPoints(cell_id, cell_point_ids)
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


if __name__ == "__main__":
    in_bunny_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.stl"
    # in_bunny_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny_usg.4.2.vtk"
    out_bunny_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/stl_to_vtk_legacy.vtk"

    converter = STLToVtkLegacyConverter()
    converter.Execute(in_bunny_obj_file, out_bunny_obj_file)
