# coding=utf-8
import tensorflow as tf
import numpy as np
from PIL import Image
import random
import logging

logging.basicConfig(level=logging.DEBUG,
                              format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                              datefmt='%b %d %Y %H:%M:%S',
                              filename='/home/mpiNode/data/write.log',
                              filemode='w')
logger = logging.getLogger(__name__)

file_name="ms_train_data.tfrecords"

tfrecords_filename = '/home/mpiNode/data/' + file_name
txt_file_dir = "/home/mpiNode/ID_MS_FACE/MS_result_selected_fileList.txt"

def _int64_feature(value):
  return tf.train.Feature(int64_list=tf.train.Int64List(value=[value]))


def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value]))


def read_path_label_pair(txt_file_path):
    # /home/daiab/test/test.csv
    f = open(txt_file_path, 'r')
    label_file_pair = []
    for line in f:
        filename, label = line[:-1].split(' ')
        label_file_pair.append((int(label), filename))
    return label_file_pair


def write_to_tfrecord(label_path_pairs):
    writer = tf.python_io.TFRecordWriter(tfrecords_filename)
    count = 0
    for img_label, img_path in label_path_pairs:
        #img = np.array(Image.open(img_path).resize((90, 90), Image.BILINEAR))
        img = np.array(Image.open(img_path))
        img_raw = img.tostring()
        example = tf.train.Example(features=tf.train.Features(feature={
            'label' : _int64_feature(img_label),
            'image_raw': _bytes_feature(img_raw)}))
        writer.write(example.SerializeToString())
        count += 1
        if count % 200 == 0:
            logger.info(count)
    writer.close()


def write():
    label_file_pair = read_path_label_pair(txt_file_dir)
    random.shuffle(label_file_pair)
    write_to_tfrecord(label_file_pair)


if __name__ == '__main__':
    write()
