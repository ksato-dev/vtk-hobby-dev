from libs import common
import vtkmodules.all as vtk

object_3d_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.stl"
# bunny_vtk_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.vtk"

if __name__ == "__main__":
    stl_reader = vtk.vtkSTLReader()
    stl_reader.SetFileName(object_3d_file)
    stl_reader.Update()

    stl_data = stl_reader.GetOutput()
    point0 = stl_data.GetCell(0).GetPoints().GetPoint(0)  # これでやっと頂点座標にアクセスできる。
    print(point0)
    # print(stl_data.GetPointData())
    print(type(point0))

    # vtk_writer = vtk.vtkPolyDataWriter()
    # vtk_writer.SetFileName(bunny_vtk_file)
    # vtk_writer.SetFileVersion(vtk_writer.VTK_LEGACY_READER_VERSION_4_2)
    # vtk_writer.SetInputData(stl_reader.GetOutput())
    # vtk_writer.Update()
