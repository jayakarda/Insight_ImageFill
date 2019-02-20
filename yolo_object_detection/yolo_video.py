import sys
import argparse
from yolo import YOLO, detect_video
from PIL import Image
import cv2
import numpy
import ntpath
import os

def detect_img_in_dir(yolo):
    test_img_dir= input('Input Test Images Directory:')
    with open('../gan_infilling/bbox_coordinates.txt', 'a') as the_file:
        the_file.truncate(0)
    for filename in os.listdir(test_img_dir):
        if filename.endswith(".JPEG") or filename.endswith(".jpg"):
            try:
                image = Image.open(test_img_dir+filename)
            except:
                print('Open Error! Try again!')
            else:
                with open('results/output/bbox_coordinates.txt', 'a') as the_file:
                    the_file.write("{0},".format(filename))
                r_image = yolo.detect_image(image)
                #r_image.show()
                opencvImage = cv2.cvtColor(numpy.array(r_image), cv2.COLOR_RGB2BGR)
                cv2.imwrite('results/detection_result_images/test_image.jpg',opencvImage)
    yolo.close_session()

def detect_img(yolo):
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        pass
    else:
        with open('../gan_infilling/bbox_coordinates.txt', 'w') as the_file:
            the_file.write("{0},".format(img))
        r_image = yolo.detect_image(image)
        #r_image.show()
        opencvImage = cv2.cvtColor(numpy.array(r_image), cv2.COLOR_RGB2BGR)
        cv2.imwrite('results/detection_result_images/test_image.jpg',opencvImage)
    yolo.close_session()

FLAGS = None

if __name__ == '__main__':
    # class YOLO defines the default value, so suppress any default here
    parser = argparse.ArgumentParser(argument_default=argparse.SUPPRESS)
    '''
    Command line options
    '''
    parser.add_argument(
        '--model_path', type=str,
        help='path to model weight file, default ' + YOLO.get_defaults("model_path")
    )

    parser.add_argument(
        '--anchors', type=str,
        help='path to anchor definitions, default ' + YOLO.get_defaults("anchors_path")
    )

    parser.add_argument(
        '--classes_path', type=str,
        help='path to class definitions, default ' + YOLO.get_defaults("classes_path")
    )

    parser.add_argument(
        '--gpu_num', type=int,
        help='Number of GPU to use, default ' + str(YOLO.get_defaults("gpu_num"))
    )

    parser.add_argument(
        '--image', default=False, action="store_true",
        help='Image detection mode, will ignore all positional arguments'
    )
    parser.add_argument(
        "--output", nargs='?', type=str, default="./results/detection_result_images",
        help = "Image output path")
    '''
    Command line positional arguments -- for video detection mode
    '''
    parser.add_argument(
        "--input", nargs='?', type=str,required=False,default='./results/test_video.mp4',
        help = "Video input path"
    )

    # parser.add_argument(
#         "--output", nargs='?', type=str, default="./results/detection_result_images",
#         help = "[Optional] Video output path"


    FLAGS = parser.parse_args()
    print(vars(FLAGS))

    if FLAGS.image:
        """
        Image detection mode, disregard any remaining command line arguments
        """
        print("Image detection mode")
        if "input" in FLAGS:
            print(" Ignoring remaining command line arguments: " + FLAGS.input + "," + FLAGS.output)
        detect_img(YOLO(**vars(FLAGS)))
    elif "input" in FLAGS:
        print('FLAGS.output: ',FLAGS.output)
        detect_video(YOLO(**vars(FLAGS)), FLAGS.input, FLAGS.output)
    else:
        print("Must specify at least video_input_path.  See usage with --help.")
