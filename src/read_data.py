# -*- coding: utf-8 -*-
"""MHD Visualization
    Methods to read data files.
"""
import os
import errno


def read_visit_file(file_path, file_name, VisIt):
    """Read visit file from the given full/relative path of the file & the visit module.

    Args:
        file_path (str): the relative path of the file.
        file_name (str): the name of the input file.
        VisIt (Any): VisIt module

    Returns:
        None
    """

    # Check if the extension valid.
    if os.path.splitext(file_name)[1] not in [".visit"]:
        raise OSError(r"File type %s is not supported" % (os.path.splitext(file_name)[1]))

    # Join the file path and file name.
    input_file_full_path = os.path.join(file_path, file_name)

    # Check if the input file exist.
    print("Checking if the input file exist...")
    if not os.path.exists(input_file_full_path):
        raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), input_file_full_path)

    # Read file and check if VisIt could successfully open the file.
    print("Reading file %s" % (input_file_full_path))
    if not VisIt.OpenDatabase(input_file_full_path):
        print("wtf?")
    return

def read_h5_file(file_path, file_name, VisIt):
    """Read visit file from the given full/relative path of the file & the visit module.

    Args:
        file_path (str): the relative path of the file.
        file_name (str): the name of the input file.
        VisIt (Any): VisIt module

    Returns:
        None
    """


    # Check if the extension valid.
    if os.path.splitext(file_name)[1] not in [".h5", ".xdmf"]:
        raise OSError("File is not supported")

    # Join the file path and file name.
    input_file_full_path = os.path.join(file_path, file_name)
    """Full/relative path with file name"""

    # Check if the input file exist.
    if not os.path.exists(input_file_full_path):
        raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), input_file_full_path)

    # Read file and check if VisIt could successfully open the file.
    print("Reading file %s" % (input_file_full_path))
    if not VisIt.OpenDatabase(input_file_full_path, 0, "Pixie"):
        raise OSError(errno.ENOENT, os.strerror(errno.ENOENT), input_file_full_path)

    return

if __name__ == "__main__":
    print(__doc__)