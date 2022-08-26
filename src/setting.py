# -*- coding: utf-8 -*-
"""Setting of the plot."""

# input file path.
INPUT_FILE_NAME = r"g1040_0021.h5"
"""str: File name of the input file"""
INPUT_FILE_NAME = r"g1052.visit"
"""str: File name of the input file"""
INPUT_FILE_PATH = r"./scorpio-out/"
"""str: Full/relative path of the input file"""
INPUT_FILE_PATH = r"C:/Users/hinhi/OneDrive/OneDrive - The Chinese University of Hong Kong/exchange/mhd-visualization/mhd-visualization/mhd-visualization/scorpio-out/g1052/"
"""str: Full/relative path of the input file"""


# plot setting
PLOT_SCALAR_FIELD_NAMES = ['den']
"""List[str]: Saclar field name in your data file."""
PLOT_VECTOR_FIELD_NAMES = []
"""List[List[str]]: Vector field name in a list ['vec_x', 'vec_y' 'vec_z']."""


# Camera setting.
CAMERA_MODE = 1
"""Output mode setting

    1. fix camera, time evolve
    2. moving camera, sngle snapshot
    3. moving camera, time evolve
    4. fix camera, single snapshopt
"""


# Output file path.
OUTPUT_FILE_NAME = r"g1040_0021"
"""str: Prefix of the output file"""
# OUTPUT_FILE_NAME = r"g1052"
"""str: Prefix of the output file"""
OUTPUT_FILE_PATH = r"./output/"
"""str: Output path of the file"""


# Output format:
OUTPUT_FILE_FORMAT = r"png"
"""str: Output file format, options: `png`, `jpg`"""
FIGURE_WIDTH = 1024*2
"""int: Width of the figure (px)"""
FIGURE_HEIGHT = 768*2
"""int: Height of the figure (px)"""

if __name__ == "__main__":
    print(__doc__)
