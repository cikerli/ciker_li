# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
#解决中文显示问题
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False

import pandas as pd
import pickle
import numpy as np
from collections import Counter

countdx = []   #统计大小号
numb = 0       #蓝球号码
lanqiu = []    #蓝球列表
count = []
position = []
same = 0        #相同次数
countlg = []  #大小号间隔


#以DataFrame格式读取全部数据
with open('dfall.txt', 'rb') as t:
    DFall = pickle.load(t)
lanqiu = list(DFall['blue'])
length = len(lanqiu)

#蓝球最近50次统计
def count50(mylist):
    plt.title('蓝球最近50次统计')
    cou = []
    for i in range(1,17):
        cou += [mylist[:50].count(i)]
    return cou


#统计蓝球大小号
def dxcount(mylist):
    plt.title('统计蓝球大小号')
    dxco = []
    for j in mylist:
        if j >8:
            dxco += [1]
        else :
            dxco += [2]
    return dxco

#统计大小号间隔
def lgcount(mylist):
    plt.title('统计大小号间隔')
    lgco = []
    for i in range(1,len(mylist)):
        if mylist[i] == mylist[i-1]:
            same += 1
        else :
            lgco += [same]
            same = 0
    return lgco
        
#统计n#蓝球出现间隔
def countjgn(n):
    st = '统计%d号蓝球出现间隔'%(n)
    plt.title(st)
    p1 = 0
    p2 = 0
    count1 = []
    po = []
    while True:
        try:
            p1 = lanqiu[p2:].index(n)+1
            p2 += p1
            count1 += [p1]
                         
        except ValueError:
            break
    res = dict(Counter(count1))
    result = sorted(res)
    for j in range(len(result)):
        k = result[j]
        po += [res[k]]

    return result,po



#显示大小号间隔
#position = countlg[:100]
#plt.bar(range(len(position)),position , align='center')



#统计各蓝球间隔超过n期次数，50期不出现概率3.97%
def countdayu(n):
    plt.title('统计各蓝球间隔超过%d期次数'%(n))
    po = []
    for i in range(1,17):
        p2 = 0
        p3 = 0
        count50 = 0
        
        while True:
            try:
                p1 = lanqiu[p3:].index(i)+1
                if p1 > n:
                    count50 += 1
                p3 += p1
                if p1 > p2:
                    p1,p2 = p2,p1
            
            except ValueError:
                po += [count50]
                break
    return po


   

#统计各蓝球出现最长间隔
def countjgmax():
    plt.title('统计各蓝球出现最长间隔')
    po = []
    for i in range(1,17):
        p2 = 0
        p3 = 0

        while True:
            try:
                p1 = lanqiu[p3:].index(i)+1
                p3 += p1
                if p1 > p2:
                    p1,p2 = p2,p1
            
            except ValueError:
                po += [p2]
                break
    return po



#蓝球最近出现时间统计
def zuijin():
    po = []
    plt.title('蓝球最近出现时间统计')
    for i in range(1,17):
        p1 = lanqiu[0:].index(i)+1
        po += [p1]
    return po


result,position = countjgn(11)

pmax = position.index(max(position))+1

plt.bar(range(len(result)),position , align='center')
plt.xticks(range(len(result)), result)

#绘制柱状图
#plt.bar(range(1,17),position,)
plt.bar(pmax-1,position[pmax-1],color =['r'])

# 在柱状图上显示具体数值, ha参数控制水平对齐方式, va控制垂直对齐方式
for x, y in enumerate(position):
    plt.text(x, y , '%s' % y, ha='center', va='bottom')
    
#设置x轴
#new_ticks = np.linspace(1, 16, 16)
#plt.xticks(new_ticks)

# 为两条坐标轴设置名
plt.xlabel("间隔距离")
plt.ylabel("出现次数")

# 添加标题
#plt.title('13#蓝球间隔次数统计')

plt.show()  

