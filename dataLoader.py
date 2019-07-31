import re

class loader():
    def __init__(self, text, path):
        self.text = text
        self.path = path
        self.urlRe = r'https://i\.pximg\.net/c/240x480/img-master/img/\d{4}/\d{2}/\d{2}/\d{2}/\d{2}/\d{2}/.*?\.\w{3}'
        self.idRe = r'\d{8}'
        self.allData = []

    def urlLoader(self):
        print('数据处理中')
        compiler = re.compile(self.urlRe)
        self.imgUrl = compiler.findall(self.text)
        return self.urlId()

    def urlId(self):
        compiler = re.compile(self.idRe)
        for i in self.imgUrl:
            id = compiler.findall(i)
            self.dataDeal(i, id[0])
        
        print('数据处理完成')
        return self.allData
        # dow = download.download(self.allData, self.path)
        # dow.imgDown()

    def dataDeal(self, url, id):
        self.allData.append({
            'id': id,
            'url': url,
            'illust': 'https://www.pixiv.net/member_illust.php?mode=medium&illust_id=' + id
        })
