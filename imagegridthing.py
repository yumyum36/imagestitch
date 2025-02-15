# - 6/7/2023 - https://stackoverflow.com/questions/20038648/writting-a-file-with-multiple-images-in-a-grid
import math
import os
import matplotlib.pyplot as plt

# Config:
images_dir = 'C:/Users/-/Pictures/Cool Pics/Games/CCG/TESL/Cards/TESLCardImages/07-Neutral'
result_grid_filename = 'C:/Users/-/Pictures/Cool Pics/Games/CCG/TESL/Cards/1Output/Neutralgrid.png'
result_figsize_resolution = 100 # 1 - 100px ->Controls resolution/filesize, lower to decrease

images_list = os.listdir(images_dir)
images_count = len(images_list)
print('Images: ', images_list)
print('Images count: ', images_count)

# Calculate the grid size:
grid_size = math.ceil(math.sqrt(images_count))

# Create plt plot:
fig, axes = plt.subplots(grid_size, grid_size, figsize=(result_figsize_resolution, result_figsize_resolution), layout="compressed")
#added ", layout="compressed" " as a last parameter to move the image closer together. It works, but gives me a weird error message.
#fixed error message by commenting out another line
fig.patch.set_alpha(0.0)
#sets background to be transparant: https://stackabuse.com/how-to-change-plot-background-in-matplotlib/


current_file_number = 0
for image_filename in images_list:
    x_position = current_file_number % grid_size
    y_position = current_file_number // grid_size

    plt_image = plt.imread(images_dir + '/' + images_list[current_file_number])
    axes[x_position, y_position].imshow(plt_image)
    axes[x_position, y_position].axis('off')
    #Previous line based on: https://stackoverflow.com/questions/25862026/turn-off-axes-in-subplots
    axes[x_position, y_position].patch.set_alpha(0.0)
    #added to make background transparant
    print((current_file_number + 1), '/', images_count, ': ', image_filename)

    current_file_number += 1

#plt.subplots_adjust(left=0.0, right=1.0, bottom=0.0, top=1.0)
plt.savefig(result_grid_filename)

#sys.exit(0)
#Thank you John for the code suggestion of return 0
