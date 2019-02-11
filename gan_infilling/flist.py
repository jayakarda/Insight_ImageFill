import cv2
import argparse
import os
from random import shuffle
from distutils.dir_util import copy_tree

parser = argparse.ArgumentParser()
parser.add_argument('--folder_path', default='training_data', type=str, help='The folder path')
parser.add_argument('--train_filename', default='data_flist/apparel/train_shuffled.flist', type=str, help='The output filename.')
parser.add_argument('--validation_filename', default='data_flist/apparel/validation_shuffled.flist', type=str, help='The output filename.')
parser.add_argument('--is_shuffled', default='1', type=int, help='Needed to shuffle')

def image_resize(input_image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    image = cv2.imread(input_image, 3)
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image

    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    resized = cv2.resize(image, dim, interpolation = inter)
    return resized

# if __name__ == "__main__":
#     args = parser.parse_args()
#     # get the list of directories
#     dirs = os.listdir(args.folder_path)
#     dirs_name_list = []
#     # make 2 lists to save file paths
#     training_file_names = []
#     validation_file_names = []
#     # print all directory names
#     for dir_item in dirs:
#         # modify to full path -> directory
#         dir_item = args.folder_path
#         # print(dir_item)
#         original_image_folder = os.listdir(dir_item + "/images")
#         for image in original_image_folder:
#             if image.endswith(".JPEG") or image.endswith(".jpg"):
#                 resized_img = image_resize(image, 256, 256)
#                 train_image = dir_item + "/training" + "/" + training_item
#                 training_file_names.append(train_image)
#         # training_folder = os.listdir(dir_item + "/training")
#         # for training_item in training_folder:
#         #     training_item = dir_item + "/training" + "/" + training_item
#         #     training_file_names.append(training_item)
#
#         validation_folder = os.listdir(dir_item + "/validation")
#         for validation_item in validation_folder:
#             validation_item = dir_item + "/validation" + "/" + validation_item
#             validation_file_names.append(validation_item)
#     # print all file paths
#     with open(args.train_filename, 'w') as f:
#         for i in training_file_names:
#             f.write(i)
#             f.write('\n')
#     with open(args.validation_filename, 'w') as f:
#         for i in validation_file_names:
#             f.write(i)
#             f.write('\n')
if __name__ == "__main__":
    args = parser.parse_args()
    # get the list of directories
    dirs = os.listdir(args.folder_path)
    dirs_name_list = []
    # make 2 lists to save file paths
    training_file_names = []
    validation_file_names = []
    # print all directory names
    for dir_item in dirs:
        # modify to full path -> directory
        dir_item = args.folder_path
        # print(dir_item)
        original_image_folder = os.listdir(dir_item + "/images")
        for image in original_image_folder:
            if image.endswith(".JPEG") or image.endswith(".jpg"):
                resized_image = image_resize(dir_item + "/images" + "/" + image, 256, 256)
                cv2.imwrite(dir_item + "/training" + "/" + image, resized_image)
                train_image = dir_item + "/training" + "/" + image
                training_file_names.append(train_image)

        validation_folder = os.listdir(dir_item + "/validation")
        for validation_item in validation_folder:
            validation_item = dir_item + "/validation" + "/" + validation_item
            validation_file_names.append(validation_item)
    # print all file paths
    with open(args.train_filename, 'w') as f:
        for i in training_file_names:
            f.write(i)
            f.write('\n')
    with open(args.validation_filename, 'w') as f:
        for i in validation_file_names:
            f.write(i)
            f.write('\n')
