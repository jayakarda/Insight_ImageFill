## ImageFill


ImageFill is a tool that detects the logo on a shirt and fill it with the shirt's background color. 
Sports celebrities are often fined in millions of dollars for endorsing the wrong brands. 
It can be used for Brand Management in images or videos by some of the major sports leagues like NBA or NFL.


1. ***Download the project*** https://github.com/jayakarda/Insight_ImageFill.git

   * Download YOLOv3 weights from YOLO website or *your_drive*
   
   * Convert the Darknet YOLO model to a Keras model.
   
      python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5 # to get yolo.h5(model) or download the model *your           directory*  to model_data/directory directly.

2.  ***Retrain the model for Nike Logo Detection***

    * Download Apparel Dataset to the root directory.
    
    * Parse annotation:
      python nike_annotation.py
      
    * Download YOLOv3 weights from *fill in yolo_weights” to model_data/ directory
    
    * Retrain the model (use yolo.h5 as the pretrained model)
      python train.py -a Apparel_Dataset/nike_train_data.txt -c model_data/apparel_classes.txt -o 
      model_data/nike_derived_model_new.h5
      OR download the trained model “nike_derived_model_new.h5” to model_data/ directory directly.

3. ***Test the Model***

    python yolo_video.py --model_path model_data/nike_derived_model_new.h5 --classes_path
    ./ImageFill/yolo_object_detection/Apparel_Dataset/apparel_classes.txt –image "image path"

    Example : ./ImageFill/yolo_object_detection/test_data/test_images/nike_104.JPEG
    Output will be saved at the following location:
    ./ImageFill/yolo_object_detection/results/detection_result_images
 
4. ***Retrain the model for Image Infilling***
 
    * Prepare training images and shuffle it with flist.py.
    * Modify inpaint.yml to set DATA_FLIST, LOG_DIR, IMG_SHAPES and other parameters.
    * Run python train.py.
    * In case you want to resume training at any point,  set the following variables in inpaint.yml.
      Modify MODEL_RESTORE flag in inpaint.yml. E.g., MODEL_RESTORE:
      20190205063252254845_ip-172-31-46-187_apparel_NORMAL_wgan_gp_logs
      Run python train.py.
    
5. ***Test Image Infilling****
 
    * Generate masks using the following script:
      python process_yolo_output.py
      
    * python test.py --image masked_image_nike_floral_Shirt.jpg --mask mask_nike_floral_Shirt.jpg --output
    examples/output.png --checkpoint model_logs/20190210035054081171_ip-172-31-46-187_apparel_NORMAL_wgan_gp_logs/
    
 
