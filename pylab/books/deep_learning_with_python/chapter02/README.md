## 神经网络的数学基础

要想入门以及往下理解深度学习，其中一些数学概念可能是无法避免地需要你理解一番，比如：

- 张量以及运算
- 微分
- 梯度下降

### 初识神经网络

在开始之前希望你有一点机器学习方面的知识，解决问题的前提是提出问题，我们提出这样一个问题，对`MNIST数据集`进行分析，然后在解决问题的过程中一步一步地来捋清楚其中涉及到的概念

`MNIST数据集`是一份手写字训练集，出自`NIST`，相信你对它不会陌生，它是机器学习领域的一个经典数据集，感觉任意一个教程都拿它来说事，不过这也侧面证明了这个数据集的经典，这里简单介绍一下：

- 拥有60,000个示例的训练集，以及10,000个示例的测试集
- 图片都由一个28 ×28 的矩阵表示，每张图片都由一个784 维的向量表示
- 图片分为10类， 分别对应从0～9，共10个阿拉伯数字

压缩包内容如下：

- train-images-idx3-ubyte.gz:  training set images (9912422 bytes) 
- train-labels-idx1-ubyte.gz:  training set labels (28881 bytes) 
- t10k-images-idx3-ubyte.gz:   test set images (1648877 bytes) 
- t10k-labels-idx1-ubyte.gz:   test set labels (4542 bytes)

上图：

![](https://ws1.sinaimg.cn/large/007i3XCUgy1fynopykgrbj3230230415.jpg)

图片生成代码如下：

```python
%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

from keras.datasets import mnist

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

def plot_digits(instances, images_per_row=10, **options):
    size = 28
    images_per_row = min(len(instances), images_per_row)
    images = instances
    n_rows = (len(instances) - 1) // images_per_row + 1
    row_images = []
    n_empty = n_rows * images_per_row - len(instances)
    images.append(np.zeros((size, size * n_empty)))
    for row in range(n_rows):
        rimages = images[row * images_per_row : (row + 1) * images_per_row]
        row_images.append(np.concatenate(rimages, axis=1))
    image = np.concatenate(row_images, axis=0)
    plt.imshow(image, cmap = matplotlib.cm.binary, **options)
    plt.axis("off")

plt.figure(figsize=(9,9))
plot_digits(train_images[:100], images_per_row=10)
plt.show()
```

不过你不用急着尝试，接下来我们可以一步一步慢慢来分析手写字训练集

看这一行代码：

```python
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
```

`MNIST数据集`通过`keras.datasets`加载，其中`train_images`和`train_labels`构成了训练集，另外两个则是测试集：

- train_images.shape: (60000, 28, 28)
- train_labels.shape: (60000,)

我们要做的事情很简单，将训练集丢到神经网络里面去，训练后生成了我们期望的神经网络模型，然后模型再对测试集进行预测，我们只需要判断预测的数字是不是正确的即可

在用代码构建一个神经网络之前，我先简单介绍一下到底什么是神经网络，让我们从感知器开始

#### 感知器

> 感知器是Frank Rosenblatt提出的一个由两层神经元组成的人工神经网络，它的出现在当时可是引起了轰动，因为感知器是首个可以学习的神经网络

感知器的工作方式如下所示：

![](https://ws1.sinaimg.cn/large/007i3XCUgy1fynppb0u8jj30h703v74d.jpg)

左侧三个变量分别表示三个不同的二进制输入，output则是一个二进制输出，对于多种输入，可能有的输入成立有的不成立，在这么多输入的影响下，该如何判断输出output呢？Rosenblatt引入了权重来表示相应输入的重要性

![](https://ws1.sinaimg.cn/large/007i3XCUgy1fynpsklr29j30h203rq32.jpg)

此时，output可以表示为：

![](https://ws1.sinaimg.cn/large/007i3XCUgy1fynpu3rmaxj30d802d0t0.jpg)

上面右侧的式子是一个阶跃函数，就是和Sigmoid、Relu一样作用的激活函数

#### S型神经元

神经元和感知器本质上是一样的，他们的区别在于激活函数不同，比如跃迁函数改为Sigmoid函数

神经网络可以通过样本的学习来调整人工神经元的权重和偏置，从而使输出的结果更加准确，那么怎样给⼀个神经⽹络设计这样的算法呢？

![](https://ws1.sinaimg.cn/large/007i3XCUgy1fynqt6prr7j30k808o0ud.jpg)

以数字识别为例，假设⽹络错误地把⼀个9的图像分类为8，我们可以让权重和偏置做些⼩的改动，从而达到我们需要的结果9，这就是学习。对于感知器，我们知道，其返还的结果不是0就是1，很可能出现这样一个情况，我们好不容易将一个目标，比如把9的图像分类为8调整回原来正确的分类，可此时的阈值和偏置会造成其他样本的判断失误，这样的调整不是一个好的方案

所以，我们需要S型神经元，因为S型神经元返回的是[0,1]之间的任何实数，这样的话权重和偏置的微⼩改动只会引起输出的微⼩变化，此时的output可以表示为σ(w⋅x+b)，而σ就是S型函数，S型函数中S指的是Sigmoid函数，定义如下：

![](https://ws1.sinaimg.cn/large/007i3XCUgy1fynqvmhzahj30ib05q74i.jpg)

神经网络其实就是按照一定规则连接起来的多个神经元，一个神经网络由以下组件构成：

- 输入层：接受传递数据，这里应该是 784 个神经元
- 隐藏层：发掘出特征
- 各层之间的权重：自动学习出来
- 每个隐藏层都会有一个精心设计的激活函数，比如Sigmoid、Relu激活函数
- 输出层，10个输出
- 上⼀层的输出作为下⼀层的输⼊，信息总是向前传播，从不反向回馈：前馈神经网络
- 有回路，其中反馈环路是可⾏的：递归神经网络

从输入层传入`手写字训练集`，然后通过隐藏层向前传递训练集数据，最后输出层会输出10个概率值，总和为1。现在，我们可以看看`Keras`代码:

```python

```

### 说明

对本文有影响的书籍文章如下，感谢他们的付出：

- [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com/chap1.html) 第一章
- [Deep Learning with Python](https://www.amazon.com/Deep-Learning-Python-Francois-Chollet/dp/1617294438) 第二章
- [hands_on_Ml_with_Sklearn_and_TF](https://github.com/apachecn/hands-on-ml-zh)
- [hanbt零基础入门深度学习系列](https://www.zybuluo.com/hanbingtao/note/448086)
