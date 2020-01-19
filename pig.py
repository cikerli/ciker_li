import pandas as pd
import requests
import time
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.random}


#生成出生当年所有日期
def dateRange(a,b):
    fmt = '%Y-%m-%d'
    bgn = int(time.mktime(time.strptime(a,fmt)))
    end = int(time.mktime(time.strptime(b,fmt)))
    list_date = [time.strftime(fmt,time.localtime(i)) for i in range(bgn,end+1,3600*24)]
    return list_date

def get_json(url):
    try:
        response = requests.get(url,headers=headers)
        print(response.status_code)
        if response.status_code == 200:
            json_text=response.json()
            return json_text
        else:
            print('返回代码：'+response.status_code)
            return None
    except Exception:
        print('此页有问题！')
        return None


def get_comments(url):
    doc = get_json(url)
    if doc == None:
        print('错误get_comment!')
        return False
    else:
        dic = {}
        dic['pigprice'] = doc['pigprice']
        dic['pig_in'] = doc['pig_in']
        dic['pig_local'] = doc['pig_local']
        dic['maizeprice'] = doc['maizeprice']
        dic['bean'] = doc['bean']
        a = '-'.join(doc['time'][3])
        b = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        #print(dateRange(a,b))
        dic['time'] = dateRange(a,b)
        return pd.DataFrame(dic)

data =get_comments('http://zhujia.zhuwang.cc/index/api/chartData?areaId=140100&aa=11579357603972')

if data != False:
    data = data[180:]

    #作图
    from pylab import mpl
    import  matplotlib.pyplot as plt
    mpl.rcParams['font.sans-serif'] = ['SimHei'] # 指定默认字体
    mpl.rcParams['axes.unicode_minus']

    plt.figure(figsize=(8,10), dpi=80)
    plt.figure(1)
    ax1 = plt.subplot(311)
    plt.plot(data['time'],data['pigprice'], color="r",linestyle = "-")
    plt.xticks([data['time'][181],data['time'][270],data['time'][365]])
    price = str(data['pigprice'][365])+'元'
    plt.annotate(price, xy=(data['time'][365], data['pigprice'][365]), xytext=(data['time'][270], 35), arrowprops=dict(facecolor='black', shrink=0.1, width=0.5))
    plt.xlabel("生猪(外三元) 元/公斤")

    ax2 = plt.subplot(312)
    plt.plot(data['time'],data['maizeprice'],color="y",linestyle = "-")
    plt.xticks([data['time'][181],data['time'][270],data['time'][365]])
    plt.xlabel("玉米(15%水分) 元/吨")

    ax3 = plt.subplot(313)
    plt.plot(data['time'],data['bean'],color="g",linestyle = "-")
    plt.xlabel("豆粕(43%蛋白) 元/吨")
    plt.xticks(data['time'][1::184], rotation=0)

    plt.show()
