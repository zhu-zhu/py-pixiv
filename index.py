import pixi

url = 'https://www.pixiv.net/ranking.php?mode=daily&content=illust'
path = './img/'

pixis = pixi.pixis(url, path)
data = pixis.run()

print(data)