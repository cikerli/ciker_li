# -*- coding: utf-8 -*-
import urllib.request 
import re
import os, sys
import socket
import codecs
import random
from multiprocessing import Pool
import threading
import time
import datetime


def downLoad(imageurl,imagename):
    #设置超时时间为30s
    socket.setdefaulttimeout(30)
    try:
        urllib.request.urlretrieve(imageurl,filename=imagename)
    except socket.timeout:
        count = 1
        while count <= 5:
            try:
                urllib.request.urlretrieve(imageurl,filename=imagename)                                                
                break
            except socket.timeout:
                err_info = 'Reloading for %d time'%count if count == 1 else 'Reloading for %d times'%count
                print(err_info)
                count += 1
        if count > 5:
            print("downloading picture fialed!")
  
def craw(url):
    #设置超时时间为30s
    socket.setdefaulttimeout(30)
    #构造header
    opener = urllib.request.build_opener()
    opener.addheaders = [("user-agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")]
    urllib.request.install_opener(opener)  #安装全局header
    
    #读取网页
    html1=urllib.request.urlopen(url).read()  
    html2 = str(html1).encode('GB2312').decode('GB2312')

    #找到jpg
    pat = 'data-src=\\\\\'(.+?\.jpg)'    
    imagelist = re.compile(pat).findall(html2)

    pat1 = '<h4>(.+?)</h4>'
    title = re.compile(pat1).findall(html2)

    #转码
    titpath = title[0].encode('GBK')
    titlepath = eval(repr(titpath).replace('\\\\', '\\'))
    titpath = titlepath.decode('GBK')

    #保存路径
    path = "e:/temp/img/"+str(titpath)+"/"     #只要8个字，太长没用
    
    if os.path.exists(path)	:
        path = path[:-1] + "1/"
        os.makedirs( path )
    else:
        os.makedirs( path )

    #存储jpg
    x = 1
    threads = []
    for imageurl in imagelist:
        imagename = path+str(x)+".jpg"
        t = threading.Thread(target=downLoad,args=(imageurl,imagename))
        t.start()
        threads.append(t)
        x += 1
    for t in threads:
        t.join()
    print(path + "all jpg saved!")



def getlink(url):
    #moni liulanqi
    headers = ("user-agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    #headers = ("user-agent","Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #make opener
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())

    #make url-link
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    pat2 = '<h3><a href="(htm_data.+?)" target="_blank" id=""'
    link = re.compile(pat2).findall(data)
    for i in range(0,len(link)):
        link[i] = "https://cl.bbbck.xyz/"+link[i]

    return link

def main():
    #记录开始时间
    start = datetime.datetime.now()
    try:
        #url
        url = "https://cl.bbbck.xyz/thread0806.php?fid=16&search=&page=9"
        #get link
        linklist = getlink(url)

        #多进程Pool
        pool=Pool()
        print("多进程下载开始")
        pool.map(craw,linklist)
        pool.close()
    finally:
        

        #记录结束时间
        end = datetime.datetime.now()
        print("全部结束，共耗时：")
        print((end - start).minute)

if __name__ == '__main__':
    main()
