import asyncio
import os
from mxget.provider import qq
 

def main():
   
   while 1:
      n = 0
      songname = input('歌曲名称(退出输入0）： ')
      if songname == '0':
         break
      
      loop = asyncio.get_event_loop()
      resp = loop.run_until_complete(qq.search_song(songname))
      print(resp)
      print('序号         歌名           歌手            id')
      for num in resp.songs:
          print('%3d %25s %25s %25s'%(n,resp.songs[n].name,resp.songs[n].artist,resp.songs[n].id))
          n +=1

      while 1:
         index = int(input('选择哪首:(重新选歌输入10010） '))
         if index == 10010:
            break
         elif index >n-1 or index <0:
            print('请输入正确序号！！！')
            continue
         song = resp.songs[index].id
         song = 'mxget song --'+song
         os.system(song)

   loop.close()


if __name__ == '__main__':
    main()
