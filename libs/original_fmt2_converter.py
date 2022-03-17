from libs import common
from tqdm import tqdm
import vtkmodules.all as vtk
from libs.base_original_fmt_converter import BaseOriginalFmtConverter


class OriginalFmt2Converter(BaseOriginalFmtConverter):
    def write(self):
        with open(self.out_file, mode="w") as file_obj:

            # Write points section. ---
            num_points = self.vtk_obj_data.GetNumberOfPoints()
            print("num_total_points:", num_points)

            # Write header.
            file_obj.write("[points]\n")
            file_obj.write("point_id:(x,y,z)\n")
            file_obj.write("===\n")

            # Write data.
            for point_id in tqdm(range(num_points)):
                xyz = self.object_3d.points[point_id]
                xyz_str = [str(elem) for elem in xyz]
                xyz_str = ",".join(xyz_str)

                point_info_str = str(point_id) + ":(" + xyz_str + ")\n"
                file_obj.write(point_info_str)

            # --- Write points section.

            file_obj.write("\n")

            # Write cells section. ---
            num_cells = self.vtk_obj_data.GetNumberOfCells()
            print("num_total_cells:", num_cells)

            # Write header.
            file_obj.write("[cells]\n")
            file_obj.write("cell_id:(point_id0,point_id1,...)\n")
            file_obj.write("===\n")

            # Write data.
            for cell_id in tqdm(range(num_cells)):
                cell_type = self.object_3d.cell_types[cell_id]
                cell = self.object_3d.cells[cell_id]
                cell_str = [str(point_id) for point_id in cell]
                cell_str = ",".join(cell_str)

                cell_info_str = str(cell_id) + ":(" + cell_str + ")\n"
                file_obj.write(cell_info_str)

            # --- Write cells section.

            file_obj.write("\n")

            # Write cells section. ---
            num_cells = self.vtk_obj_data.GetNumberOfCells()
            print("num_total_cells:", num_cells)

            # Write header.
            file_obj.write("[cells]\n")
            file_obj.write("cell_id:(point_id0,point_id1,...)\n")
            file_obj.write("===\n")

            # Write data.
            for cell_id in tqdm(range(num_cells)):
                cell_type = self.object_3d.cell_types[cell_id]
                cell_type_str = common.CellType2Str(cell_type)
                file_obj.write(cell_type_str)
                file_obj.write("\n")

            # --- Write cells section.
            print("Completed parsing.")


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
    writer = OriginalFmt2Converter(out_fmt1_file, stl_data)
    writer.execute()
