'''
Created on 2020年6月7日
直接调用A2的Model，注意图片的名字只能是0-num并且类型只能是png
专用所以不进行泛化
@author: Huang Jincheng
'''
import numpy as np
from A2 import model

num = np.arange(151, 161)#设置传入哪几张二维码
A = model(num)
print(A.shape[0])
unique_rows = np.unique(A, axis=0)
print(unique_rows.shape[0])
print(A.shape[0])

'''
取第一行和最后一行，数据结果:
num = 10 无重复
num = 20 无重复(1-20)
num = 20(21-40) 3张重复
num = 20(41-60) 2张重复
num = 20(61-80) 2张重复
num = 20(81-100) 3张重复
num = 50 9张有重复
num = 100 28张有重复
num = 1000 493张有重复
'''

'''
测试结果2：
10个二维码为一组的测试
第一组:无重复
第二组：无重复
第三组：无重复
第四组：无重复
第五组：无重复
第六组：无重复
第七组：无重复
第八组：无重复
第九组：无重复
第十组：无重复
'''