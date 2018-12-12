#!/usr/bin/env python
"""
 Created by howie.hu at 2018/11/20.
"""
import numpy as np
import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data


class DataLoader():
    def __init__(self):
        mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)
        self.train_data = mnist.train.images  # np.array [55000, 784]
        self.train_labels = np.asarray(mnist.train.labels, dtype=np.int32)  # np.array [55000] of int32
        print(self.train_labels[0])
        self.eval_data = mnist.test.images  # np.array [10000, 784]
        self.eval_labels = np.asarray(mnist.test.labels, dtype=np.int32)  # np.array [10000] of int32
        print(self.eval_labels.shape)

    def get_batch(self, batch_size):
        index = np.random.randint(0, np.shape(self.train_data)[0], batch_size)
        return self.train_data[index, :], self.train_labels[index]


if __name__ == '__main__':
    DataLoader()
