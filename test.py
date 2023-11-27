

import os

def get_image_paths(folder_path):
    image_paths = []
    for file in sorted(os.listdir(folder_path)):

        relative_path = os.path.join(folder_path, file)
        image_paths.append(relative_path[21:])
    return image_paths

# Specify the folder path where your images are stored
folder_path = '/Users/hughlau/bella/pic'

# Get a list of relative paths of images in the existing order
image_paths = get_image_paths(folder_path)
print(image_paths)