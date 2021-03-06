is_train=True
# load the model on an epoch using the model-load-prefix
load_epoch=None
# begin epoch
# TODO: begin_epoch=load_epoch if load_epoch is not None else 0
begin_epoch=load_epoch if load_epoch is not None else 0
# model prefix
model_prefix="log/train/model"
# train record data path
data_train="/home/mpiNode/ID_MS_FACE/MS_result_selected_fileList.rec"
# test record data path
data_test=""
# the validation data
data_valid=None #"/home/mpiNode/data/img.rec"

# the batch size
batch_size=720
# key-value store type
kv_store="device" #"dist" "local"
# 1 means test reading speed without training
test_io=False
# show progress for every n batches
disp_batches=40
# list of gpus to run, e.g. 0 or 0,2,5. empty means using cpu
gpus=[0, 1, 2, 3]
# number workers
num_workers = len(gpus)
# momentum  for sgd
mom=0.9
# weight decay for sgd
wd=0.0001
# log network parameters every N iters if larger than 0
monitor=500
#the neural network to use
init_xavier=True
# report the top-k accuracy. 0 means no report.
# top_k=0


# the number of classes
num_classes=41857
# the number of training examples
num_examples=3095536
# max num of epochs
num_epochs=50
# initial learning rate
lr=0.08
pow=0.6
end_lr=0.0001
decay_nbatch=int(num_examples / batch_size) * num_epochs
# the image shape feed into the network
image_shape=(3, 224, 224)
# a tuple of size 3 for the mean rgb
rgb_mean=[255, 255, 255]
# if or not randomly crop the image
random_crop=1
max_random_l=0
random_mirror=1
data_nthreads=12

