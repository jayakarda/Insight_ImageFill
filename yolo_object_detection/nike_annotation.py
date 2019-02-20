import xml.etree.ElementTree as ET
from os import getcwd

import random

sets=[('nike_train'), ('nike_test')]

classes = ["nike"]


def convert_annotation(image_id, list_file):
    try:
        in_file = open('Apparel_Dataset/annotations/nike/nike_%s.xml'%(image_id))
        tree=ET.parse(in_file)
        root = tree.getroot()
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult)==1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text), int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text))
            list_file.write(" " + ",".join([str(a) for a in b]) + ',' + str(cls_id))
    except Exception:
        pass

wd = getcwd()   # current working path

# 1 arrange train, val, test dataset:
ids = list(range(1,500))
random.shuffle(ids)
train = ids[:400]
test = ids[400:]
dataset = [train, test]
k = 0
for image_set in dataset:
    subset_name = sets[k]
    k += 1
    image_ids = open('Apparel_Dataset/%s.txt'%(subset_name), 'w')
    for i in range(len(image_set)):
        image_ids.write('%d\n'%(image_set[i]))
    image_ids.close()


# 2 produce train, val, test data:
for image_set in sets:
    image_ids = open('Apparel_Dataset/%s.txt'%(image_set)).read().strip().split()
    list_file = open('Apparel_Dataset/%s_data.txt'%(image_set), 'w')
    for image_id in image_ids:
        try:
            list_file.write('Apparel_Dataset/images/nike/nike_%s.JPEG'%(image_id))
        except:
            continue
        convert_annotation(image_id, list_file)
        list_file.write('\n')
    list_file.close()
