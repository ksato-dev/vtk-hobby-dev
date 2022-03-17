from libs import common
from libs.original_fmt1_converter import OriginalFmt1Converter
from libs.original_fmt2_converter import OriginalFmt2Converter
from tqdm import tqdm
import vtkmodules.all as vtk


def SelectWriter(fmt_type_str, out_original_fmt_file, obj_3d_data):
    writer = None
    if fmt_type_str == "fmt1":
        writer = OriginalFmt1Converter(out_original_fmt_file, obj_3d_data)
    elif fmt_type_str == "fmt2":
        writer = OriginalFmt2Converter(out_original_fmt_file, obj_3d_data)
    return writer
    

if __name__ == "__main__":
    fmt_ext_str = "fmt2"
    # obj_3d_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.stl"
    obj_3d_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny.vtk"
    # obj_3d_file = "/home/ksato/ExternalSSD1T/dataset/vtk/test5.vtk"
    out_original_fmt_file = "/home/ksato/ExternalSSD1T/dataset/vtk/Stanford_Bunny." + fmt_ext_str

    # stl_reader = vtk.vtkSTLReader()
    obj_reader = vtk.vtkDataSetReader()
    obj_reader.SetFileName(obj_3d_file)
    obj_reader.Update()

    obj_3d_data = obj_reader.GetOutput()
    writer = SelectWriter(fmt_ext_str, out_original_fmt_file, obj_3d_data)
    writer.execute()
