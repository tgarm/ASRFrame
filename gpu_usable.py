import tensorflow as tf

if tf.test.gpu_device_name():
    print('GPU device: {}'.format(tf.test.gpu_device_name()))
else:
    print("GPU not used")
