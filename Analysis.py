'''
Created on 2020年6月7日
二维码的黑白块转化为0,1
数据灰度值阈值为127
@author: Huang Jincheng
'''
import numpy as np
from PIL import Image


def pretreatment(ima):
    ima = ima.convert('L')  # 转化为灰度图像
    im = np.array(ima)  # 转化为二维数组
    for i in range(im.shape[0]):  # 转化为二值矩阵
        for j in range(im.shape[1]):
            if im[i, j] >= 127:#阈值127
                im[i, j] = 1  #白色是1
            else:
                im[i, j] = 0
    return im


ima = Image.open('1.png')  # 读入图像
im = pretreatment(ima)  # 调用图像预处理函数
print(im.shape)
#删掉最上面36行和最下面36行
im = np.delete(im, np.arange(36), axis=0)
#删除最后36行，方法二直接读,推荐这种
im = im[:-36, :]
#消除左右白边，左右也都是36个
im = im[:, 36:-36]
#以上已经消除了所有无用信息
print(im.shape)
# for i in im:
#     print(i)
'''
目前找到规律刚开始全部为1是二维码的白边，9个连续的1代表白块，9个连续的0代表黑块
并且定位符的边长是63，即7个黑点
'''
#第一行除了定位符全取,和最后一行除定位符相加
A1 = im[0]
A1 = A1[63:-63]
A2 = im[-1]
A2 = A2[63:]
A = np.hstack((A1, A2))#A即为提取出的特征
A = A.reshape([1, -1])
print(A.shape[1])
print(A)