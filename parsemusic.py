import requests
import jsonpath

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}
print("——————————")
print("1-网易\n2-QQ\n3-酷狗\n4-酷我")
types = int(input("请选择搜索引擎："))
if types == 1:
    type = "netease"
elif types == 2:
    type = "qq"
elif types == 3:
    type = "kugou"
elif types == 4:
    type = "kuwo"
else:
    print("输入有误，程序已退出！")
    exit()
keyword = str(input("请输入搜索歌曲："))
data = {
	'input': keyword,
    'filter': 'name',
    'type': type,
    'page': '1'
}
url = "https://tool22.com/zb_tools/ajax.php?act=MusicTools"
url_html = requests.post(url, headers=headers, data=data).json()
titles = jsonpath.jsonpath(url_html, "$..title")
authors = jsonpath.jsonpath(url_html, "$..author")
urls = jsonpath.jsonpath(url_html, "$..url")
lrcs = jsonpath.jsonpath(url_html, "$..lrc")
pages = len(titles)
print("——————————")
for title, author, i in zip(titles, authors, range(1,pages+1)):
    print(f'{i}．{title} - {author}')
output = int(input("请输入下载的数字序号："))
title_song = titles[output-1]
author_song = authors[output-1]
url_song = urls[output-1]
lrc_song = lrcs[output-1]
name = title_song + " - " + author_song
url_data = requests.get(url_song, headers=headers).content
with open(name + ".lrc", "w") as p:
    p.write(lrc_song)
with open(name + ".mp3", "wb") as f:
    f.write(url_data)
    print("——————————")
    print("\33[33m{}\33[0m —— 已下载".format(name))