"""
    Setting of the plot.
"""

# input file path.
input_file_name = r"g1040_0021.h5"
input_file_name = r"g1052.visit"
input_file_path = r"./scorpio-out/"
input_file_path = r"./scorpio-out/g1052/"


# plot setting
plot_scalar_field_names = ['den'] # field name in your data file.
plot_vector_field_names = [['bx', 'by', 'bz']] # field name in a list ['vec_x', 'vec_y' 'vec_z']

# output file path.
output_file_name = r"g1040_0021"
output_file_name = r"g1052"
output_file_path = r"./output/"

# other output settings:
# avilable options: 'png', 'jpeg'
output_file_format = r"png"

figure_width = 1024*2
figure_height = 768*2

# camera setting
animation = False


