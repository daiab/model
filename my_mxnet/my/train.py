# import my_mxnet.my.googlenet as net
import my_mxnet.my.googlenet as net
import my_mxnet.my.config as cfg
import my_mxnet.my.read_data as data
from my_mxnet.my import fit
import mxnet as mx

sym = net.Symble(input={"data": mx.symbol.Variable(name="data")},
                 input_shape=(int(cfg.batch_size / cfg.num_workers), 3, 224, 224))
fit.fit(sym.layer['softmax'], data.get_rec_iter)


# export DMLC_ROLE=worker; export DMLC_NUM_SERVER=4 ;python my_mxnet/my/train.py
# dist train:
# http://mxnet.io/how_to/multi_devices.html