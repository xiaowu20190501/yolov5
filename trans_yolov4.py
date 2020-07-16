import argparse
import pdb

from models.yolo import Model

# cmd = python trans_yolov4.py --cfg=models/yolov4.yaml --weights=/home/alvinox/workspace/data/weights/yolov4.weights

def load_conv(buf, start, conv_model):
    num_w = conv_model.weight.numel()
    num_b = conv_model.bias.numel()
    conv_model.bias.data.copy_(torch.from_numpy(buf[start:start + num_b]))
    start = start + num_b
    conv_model.weight.data.copy_(torch.from_numpy(buf[start:start + num_w]).reshape(conv_model.weight.data.shape))
    start = start + num_w
    return start

def load_conv_bn(buf, start, conv_model, bn_model):
    num_w = conv_model.weight.numel()
    num_b = bn_model.bias.numel()
    bn_model.bias.data.copy_(torch.from_numpy(buf[start:start + num_b]))
    start = start + num_b
    bn_model.weight.data.copy_(torch.from_numpy(buf[start:start + num_b]))
    start = start + num_b
    bn_model.running_mean.copy_(torch.from_numpy(buf[start:start + num_b]))
    start = start + num_b
    bn_model.running_var.copy_(torch.from_numpy(buf[start:start + num_b]))
    start = start + num_b
    conv_model.weight.data.copy_(torch.from_numpy(buf[start:start + num_w]).reshape(conv_model.weight.data.shape))
    start = start + num_w
    return start

def trans_yolov4(opt):

    model = Model(opt.cfg)
    weights = opt.weights

    fp     = open(weightfile, 'rb')
    header = np.fromfile(fp, count=5, dtype=np.int32)
    buf    = np.fromfile(fp, dtype=np.float32)
    fp.close()

    start = 0
    pdb.set_trace()
    for m in model.modules():
        print(m)

    torch.save()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default='models/yolov4.yaml', help='*.cfg path')
    parser.add_argument('--weights', type=str, default='', help='initial weights path')

    opt = parser.parse_args()

    trans_yolov4(opt)
