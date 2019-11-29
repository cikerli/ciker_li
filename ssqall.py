# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

import numpy as np
from collections import Counter
import pandas as pd
import pickle


DFall = pd.DataFrame({'red1':[int],'red2':[int],'red3':[int],'red4':[int],'red5':[int],'red6':[int],'blue':[int]})
countdx = []
with open('ssq.txt', 'r') as f:
    lines = f.readlines()
    index = 0
    for line in lines:
        line = line.strip() # 把末尾的'\n'删掉
        DFall.loc[index] = int(line[-2:]),int(line[-22:-20]),int(line[-19:-17]),int(line[-16:-14]),int(line[-13:-11]),int(line[-10:-8]),int(line[-7:-5])
        index += 1

with open('dfall.txt','wb') as s:
    pickle.dump(DFall, s)

#测试
#with open('dfall.txt', 'rb') as t:
#    dftest = pickle.load(t)

#print(type(dftest))

lanqiu = list(DFall['blue'])
length = len(lanqiu)


#统计蓝球大小号
for j in lanqiu:
    if j >8:
        countdx += [1]
    else :
        countdx += [2]

res = dict(Counter(countdx))
result = sorted(res)
print(result)
