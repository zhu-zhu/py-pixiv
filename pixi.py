import httpReq
import dataLoader
import download

class pixis():
    def __init__(self, url, path):
        self.url = url
        self.path = path
        self.data = []
        
    def run(self):
        http = httpReq.http()
        self.rText = http.getRequest(self.url)
        self.allData = self.dataLoader()
        self.imgDow()
        return self.allData

    def dataLoader(self):
        loader = dataLoader.loader(self.rText.text, self.path)
        return loader.urlLoader()

    def imgDow(self):
        dow = download.download(self.path)
        print('数据下载')
        for i in self.allData:
            dow.imgDown(i)
        print('done')