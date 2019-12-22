#coding=utf-8

#问：下载百度贴吧的图片？
import re
import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context



class DownloadImage(object):

    def __init__(self,url):
        self.url = url
        
    def download(self):

        req = urllib.request.urlopen(url)
        body = req.read()
        print(body)

        pattern_image = b'src="(.*?\.jpg)"'
        matchs = re.findall(pattern_image, body)


        index = 1
        for match in set(matchs):
            try:
                print(match)
                req = urllib.request.urlopen(match.decode())
                body = req.read()
                file_name= "./%s.jpg" % index
                index += 1
                
                f = open(file_name, 'wb')
                f.write(body)
                f.close()
            except Exception as e:
                pass

        

if __name__ == "__main__":
    url = "https://tieba.baidu.com/p/1457328558#!/l/p1"
    image = DownloadImage(url)
    image.download()




            
            

