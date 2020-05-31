import hashlib
import random
import time

import math
import requests


def getWeb():
    # 有道翻译网站请求方式为post

    # post(url,data,json) 由于大部分网站一般传递的是data,所以需要传进去data类型的数据  而且,请求时(不论是post还是get)都需要用到headers
    data = {
        "i": keywords,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": salt,
        "sign": sign,
        "ts": ts,
        "bv": bv,
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_CLICKBUTTION",
    }

    Request_url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Content-Type": 'application/x-www-form-urlencoded; charset=UTF-8',
        "Cookie": '_ntes_nnid=42f24e202bef5085589ff1bf4dc942db,1589284113983; OUTFOX_SEARCH_USER_ID_NCOO=2070162545.5107388; OUTFOX_SEARCH_USER_ID=-1235953781@223.150.182.30; JSESSIONID=aaaj4kccHFUV77sxSkOjx; ___rl__test__cookies=1590885573534',
        "Host": 'fanyi.youdao.com',
        "Origin": 'http://fanyi.youdao.com',
        "Referer": 'http://fanyi.youdao.com/',
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }

    html = requests.post(Request_url, data=data, headers=headers)

    jg = html.json()['translateResult'][0][0]
    print("你要查的词为: ", jg['src'])
    print("该词的翻译为:", jg['tgt'])

if __name__ == '__main__':

    keywords = input("请输入你想查询的单词:")  # 就是e

    r = "" + str(math.floor(time.time() * 1000))
    # r = 1590890216658
    i = int(r) + int(random.random() * 10)
    ts = r
    salt = i

    sign = hashlib.md5(("fanyideskweb" + keywords + str(i) + "Nw(nmmbP%A-r6U3EUn]Aj").encode("utf8")).hexdigest()

    # encode("")改变字符串编码格式,
    #
    # hash.digest()
    # 返回摘要，作为二进制数据字符串值
    #
    # hash.hexdigest()
    # 返回摘要，作为十六进制数据字符串值

    t = hashlib.md5((
        "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36").encode(
        "utf8")).hexdigest()
    bv = t
    getWeb()







