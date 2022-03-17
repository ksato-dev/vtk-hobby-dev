from base_vtk_legacy_converter import BaseVtkLegacyConverter
import sys
sys.path.append(
    "/home/ksato/ExternalSSD1T/VTK/build/lib/python3.8/site-packages/")
import vtkmodules.all as vtk


class STLToVtkLegacyConverter(BaseVtkLegacyConverter):
    def ReadFile(self, in_file_name):
        obj_reader = vtk.vtkSTLReader()
        obj_reader.SetFileName(in_file_name)
        obj_reader.Update()

        vtk_obj_data = obj_reader.GetOutput()
        # Pack points into object_3d.points.
        num_points = vtk_obj_data.GetNumberOfPoints()
        for point_id in range(num_points):
            point = vtk_obj_data.GetPoint(point_id)  # これでやっと頂点座標にアクセスできる。
            x = point[0]
            y = point[1]
            z = point[2]
            self.object_3d.points.append([x, y, z])

        # Pack cell into object_3d.cells.
        num_cells = vtk_obj_data.GetNumberOfCells()
        for cell_id in range(num_cells):
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
            cell_type_str = self.CellTypeFromVtk2Str(cell_type)
            self.object_3d.cell_types.append(cell_type_str)

    def CellTypeFromVtk2Str(self, cell_type):
        ret_str = "unkwnon"
        if cell_type == 5:
            ret_str = "tri"
        elif cell_type == 10:
            ret_str = "tetra"
        return ret_str


if __name__ == "__main__":
    # in_bunny_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.stl"
    # out_bunny_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/stl_to_vtk_legacy.vtk"
    in_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/teapot.stl"
    out_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/stl_to_vtk_legacy.vtk"

    converter = STLToVtkLegacyConverter()
    converter.Execute(in_obj_file, out_obj_file)
