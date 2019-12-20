import re
import urllib.request
def getlink(url):
    #moni liulanqi
    headers = ("user-agent","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36")
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    #make opener
    urllib.request.install_opener(opener)
    file = urllib.request.urlopen(url)
    data = str(file.read())

    #make url-link
    pat = '(https?://[^\s)";]+\.(\w|/)*)'
    pat2 = '<a href="(htm_data.+?)" target="_blank"'
    link = re.compile(pat2).findall(data)

    #kick double
    link = list(set(link))
    return link

#url
url = "https://cl.bbbck.xyz/thread0806.php?fid=16"
#get link
linklist = getlink(url)
#for print
for link in linklist:
    linkall = url[:21]+link
    print(linkall)
print("total %d url"%len(linklist))
