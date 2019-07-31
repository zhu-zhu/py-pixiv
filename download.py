import requests
import httpReq

class download():
    def __init__(self, path):
        self.path = path

    def imgDown(self, data):
        # http = httpReq.http()
        paths = self.path + data['id'] + '.jpg'
        content = requests.get(data['url'], headers = {
            'referer': data['url']
        }).content

        with open(paths, 'wb') as fb:
            fb.write(content)
            print('下载完成：' + data['id'])
            # smurl = http.postBed('https://sm.ms/api/upload', paths)
            # return smurl
