import os
from collections import namedtuple
import cv2
import numpy as np
import ntpath


def create_image_mask(input_image, l,t,r,b,output_dir):
    img = cv2.imread(input_image)
    cv2.rectangle(img, (l,t ), (r, b), (255, 255, 255), -1)
    cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    masked_image_path = os.path.join("{0}".format(ntpath.basename(input_image)))
    print (masked_image_path)
    cv2.imwrite(masked_image_path, img)
    return masked_image_path

def read_bbox_output(file_path):
    with open(file_path) as the_file:
        for line in the_file:
            words = line.split(',')
            image = words[0]
            l= int(words[1])
            t= int(words[2])
            r= int(words[3])
            b = int(words[4])
    return image,l,t,r,b

def resize_bbox_and_image(input_image, l,t,r,b):

    image = cv2.imread(input_image, 3)
    y_ = image.shape[0]
    x_ = image.shape[1]
    targetSize = 256

    x_scale = targetSize / x_
    y_scale = targetSize / y_
    #print(x_scale, y_scale)

    img = cv2.resize(image, (targetSize, targetSize));
    #print(img.shape)
    img = np.array(img);

    # original frame as named values
    (origLeft, origTop, origRight, origBottom) = (l,t,r,b)

    x = int(np.round(origLeft * x_scale))
    y = int(np.round(origTop * y_scale))
    xmax = int(np.round(origRight * x_scale))
    ymax = int(np.round(origBottom * y_scale))

    #cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
    #cv2.rectangle(img, (x,y), (xmax, ymax), (255, 255, 255), -1)
    file_path = os.path.join(output_dir,"masked_image_")
    cv2.imwrite(file_path+"{0}".format(ntpath.basename(input_image)), img)

    # Create the basic black image
    mask = np.zeros(img.shape, dtype = "uint8")
    cv2.rectangle(mask, (x,y), (xmax, ymax), (255, 255, 255), -1)
    file_path = os.path.join(output_dir,"mask_")
    cv2.imwrite(file_path+"{0}".format(ntpath.basename(input_image)),mask)

if __name__ == '__main__':
    file_path ='bbox_coordinates.txt'
    output_dir = 'examples/apparel'
    input_image, l,t,r,b = read_bbox_output(file_path)
    masked_image_path= create_image_mask(input_image, l,t,r,b, output_dir)
    resize_bbox_and_image(masked_image_path, l,t,r,b)
