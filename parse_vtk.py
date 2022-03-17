import sys
sys.path.append("/home/ksato/ExternalSSD1T/VTK/build/lib/python3.8/site-packages/")

# import vtk
# from vtkmodules import *
import vtkmodules.all as vtk

object_3d_file = "/home/ksato/ExternalSSD1T/dataset/vtk/test5.vtk"
# bunny_vtk_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.vtk"


if __name__ == "__main__":
    stl_reader = vtk.vtkDataSetReader()
    stl_reader.SetFileName(object_3d_file)
    stl_reader.Update()

    stl_data = stl_reader.GetOutput()
    point0 = stl_data.GetCell(0).GetPoints().GetPoint(3)  # これでやっと頂点座標にアクセスできる。
    print(point0)
    # print(stl_data.GetPointData())
    print(type(point0))
