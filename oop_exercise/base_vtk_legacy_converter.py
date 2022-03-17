class Object3D(object):
    def __init__(self):
        self.points = list(list())
        self.cells = list(list())
        self.cell_types = list()


class BaseVtkLegacyConverter(object):
    def __init__(self):
        self.object_3d = Object3D()

    def Execute(self, in_file_name, out_file_name):
        self.ReadFile(in_file_name)
        self.Write(out_file_name)

    def ReadFile(self, in_file_name):
        """Need override."""
        pass

    def Write(self, out_file_name):
        with open(out_file_name, mode="w") as file_obj:
            # Write header. ---
            file_obj.write("# vtk DataFile Version 4.2\n")
            file_obj.write("vtk output\n")
            file_obj.write("ASCII\n")
            file_obj.write("DATASET UNSTRUCTURED_GRID\n")
            # --- Write header.

            # Write points section. ---
            num_points = len(self.object_3d.points)
            file_obj.write("POINTS " + str(num_points) + " float\n")
            for point_id in range(num_points):
                xyz = self.object_3d.points[point_id]
                xyz_str = [str(elem) for elem in xyz]
                xyz_str = " ".join(xyz_str) + " "
                file_obj.write(xyz_str)
                if (point_id+1) % 3 == 0:
                    file_obj.write("\n")
            # --- Write points section.

            file_obj.write("\n")

            # Write cells section. ---
            num_cells = len(self.object_3d.cells)
            num_cells_attributes = sum([len(cell)
                                        for cell in self.object_3d.cells])
            num_cells_attributes += num_cells
            file_obj.write("CELLS " + str(num_cells) + " " +
                           str(num_cells_attributes) + " \n")
            for cell_id in range(num_cells):
                cell = self.object_3d.cells[cell_id]
                cell_str = [str(point_id) for point_id in cell]
                cell_str = " ".join(cell_str)

                cell_info_str = str(len(cell)) + " " + cell_str + "\n"
                file_obj.write(cell_info_str)
            # --- Write cells section.

            file_obj.write("\n")

            # Write cell_types section. ---
            file_obj.write("CELL_TYPES " + str(num_cells) + "\n")
            for cell_id in range(num_cells):
                cell_type = self.object_3d.cell_types[cell_id]
                file_obj.write(str(cell_type))
                file_obj.write("\n")
           # --- Write cells section.
