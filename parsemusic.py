import requests
import jsonpath

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
}
print("1-网易")
print("2-QQ")
print("3-酷狗")
print("4-酷我")
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
pages = [1,2,3,4,5,6,7,8,9,10]
print("——————————")
for title, author, page in zip(titles, authors, pages):
    print(f'{page}．{title} - {author}')

output = int(input("请输入下载的数字序号："))
if output == 1:
    hash = urls[0]
    lrc2 = lrcs[0]
    name = titles[0] + " - " +authors[0]
elif output == 2:
    hash = urls[1]
    lrc2 = lrcs[1]
    name = titles[1] + " - " +authors[1]
elif output == 3:
    hash = urls[2]
    lrc2 = lrcs[2]
    name = titles[2] + " - " +authors[2]    
elif output == 4:
    hash = urls[3]
    lrc2 = lrcs[3]
    name = titles[3] + " - " +authors[3]    
elif output == 5:
    hash = urls[4]
    lrc2 = lrcs[4]
    name = titles[4] + " - " +authors[4]
elif output == 6:
    hash = urls[5]
    lrc2 = lrcs[5]
    name = titles[5] + " - " +authors[5]
elif output == 7:
    hash = urls[6]
    lrc2 = lrcs[6]
    name = titles[6] + " - " +authors[6]
elif output == 8:
    hash = urls[7]
    lrc2 = lrcs[7]
    name = titles[7] + " - " +authors[7]
elif output == 9:
    hash = urls[8]
    lrc2 = lrcs[8]
    name = titles[8] + " - " +authors[8]
elif output == 10:
    hash = urls[9]
    lrc2 = lrcs[9]
    name = titles[9] + " - " +authors[9]    
else:
    print("输入数字序号有误")
    print("程序已退出")
    exit()
url_data = requests.get(hash, headers=headers).content
with open(name + ".lrc", "w") as f:
    f.write(lrc2)
with open(name + ".mp3", "wb") as f:
    f.write(url_data)
    print("——————————")
    print("{} —— 已下载".format(name))

    
