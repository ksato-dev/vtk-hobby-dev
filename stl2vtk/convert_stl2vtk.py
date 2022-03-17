import sys
sys.path.append("/home/ksato/ExternalSSD1T/VTK/build/lib/python3.8/site-packages/")

# import vtk
# from vtkmodules import *
import vtkmodules.all as vtk

if __name__ == "__main__":
    stl_reader = vtk.vtkSTLReader()
    stl_reader.SetFileName("Stanford_Bunny.stl")
    stl_reader.Update()

    vtk_writer = vtk.vtkPolyDataWriter()
    vtk_writer.SetFileName("Stanford_Bunny.vtk")
    vtk_writer.SetFileVersion(vtk_writer.VTK_LEGACY_READER_VERSION_4_2)
    vtk_writer.SetInputData(stl_reader.GetOutput())
    vtk_writer.Update()
