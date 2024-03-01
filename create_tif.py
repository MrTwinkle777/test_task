import os
from PIL import Image
import math


def get_images_from_folders(folders_name_list):
    images = []
    for folder_name in folders_name_list:
        if os.path.exists(folder_name):
            for file in os.listdir(folder_name):
                if file.endswith('.jpg') or file.endswith('.png') or file.endswith('.jpeg'):
                    image_path = os.path.join(folder_name, file)
                    images.append(Image.open(image_path))
    return images


def create_image_result(images, output_file_name, num_cols=5, padding=100):
    if not images:
        return None

    width = max(img.size[0] for img in images)
    height = max(img.size[1] for img in images)

    rows = math.ceil(len(images) / num_cols)
    width_result = width * num_cols + padding * (num_cols + 1)
    height_result = height * rows + padding * (rows + 1)

    result_image = Image.new('RGB', (width_result, height_result))
    for i, img in enumerate(images):
        x_offset = (width + padding) * (i % 5) + padding
        y_offset = (i // 5) * (height + padding) + padding
        result_image.paste(img, (x_offset, y_offset))

    result_image.save(output_file_name)


if __name__ == '__main__':
    input_folders_name_list = ['1369_12_Наклейки 3-D_3']
    output_file_name = 'Result.tif'
    images = get_images_from_folders(input_folders_name_list)
    create_image_result(images, output_file_name)
