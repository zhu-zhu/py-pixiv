import requests
import dataLoader

class http():
    
    def getRequest(self, url):
        print('准备爬取页面')
        rText = requests.get(url)
        print('页面爬取完成')
        return rText

    def postBed(self, url, path):
        files = {
            'smfile': open(path, 'rb')
        }
        reponse = requests.post(url, files = files)
        print(path)
        print(reponse.json())
        return reponse.json()['data']['url']