from libs import common
import vtkmodules.all as vtk

in_bunny_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.stl"
# in_bunny_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny_usg.vtk"
out_bunny_obj_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny_usg.4.2.vtk"

if __name__ == "__main__":
    reader = vtk.vtkSTLReader()
    # reader = vtk.vtkDataSetReader()
    reader.SetFileName(in_bunny_obj_file)
    reader.Update()

    poly2usg = vtk.vtkAppendFilter()
    poly2usg.AddInputData(reader.GetOutput())
    poly2usg.Update()

    writer = vtk.vtkUnstructuredGridWriter()
    # writer = vtk.vtkPolyDataWriter()
    writer.SetFileName(out_bunny_obj_file)
    # writer.SetFileVersion(vtk.vtkDataSetWriter.VTK_LEGACY_READER_VERSION_4_2)
    writer.SetFileVersion(writer.VTK_LEGACY_READER_VERSION_4_2)
    writer.SetInputData(poly2usg.GetOutput())
    writer.Update()
