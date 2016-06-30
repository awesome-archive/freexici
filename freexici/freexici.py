#!/usr/bin/env python
# coding:utf8
# author: broono
# email: tosven.broono@gmail.com
# requirements:
#   pip packages: requests, bs4, selenium
#   webdriver: phantomjs

import time
import os
import requests
import random
from bs4 import BeautifulSoup
from selenium import webdriver


class FreeXici(object):

    def __init__(self, pages=1):
        self.pages = pages  # number of pages to scrape
        self.baseUrl = "http://www.xicidaili.com/"  # website base url
        self.categoryList = ["nn/", "nt/", "wn/", "wt/"]  # 4 categories


DBFILE = "proxy.txt"  # local file to store scraped proxies
TESTURL = "https://www.baidu.com"  # target url to check proxies' connectivity


# main function to scrape online proxies or open local proxy file
def fetcher(pages=1, dbfile=DBFILE, expire=24):
    retList = []
    if os.path.exists(dbfile):  # if local cache exists
        # newly added: automatic update every 24 hours
        # your can change the default expire hours value
        # there is a little bit difference here on window and *ux os:
        #   on windows getctime returns the creation time in seconds
        #   yet on linux it returns the last time when the file was changed
        # thanks to stackoverflow pals pointing out this.
        life = (time.time() - os.path.getctime(DBFILE)) / 3600
        if life > expire:  # if life is over expire hours
            try:
                os.remove(DBFILE)  # remove old cache
                print "Proxy data file outdated, updating..."
                fetcher(pages, dbfile)  # re-fetch, will enter the else branch
                return
            except Exception, e:
                raise e
        with open(dbfile) as f:
            flist = f.readlines()
            for p in flist:
                p = p.strip()
                if p:
                    yield p  # yield a line/ a proxy if it's not blank
    else:  # if local cache doesn't exists
        xdl = FreeXici()
        xdl.pages = pages
        driver = webdriver.PhantomJS()
        for cat in xdl.categoryList:
            for x in range(1, xdl.pages + 1):
                url = xdl.baseUrl + cat + str(x)
                driver.get(url)
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                trs = soup.find("tbody").findAll("tr")[1:]
                for tr in trs:
                    tds = tr.findAll("td")
                    ip = tds[1].get_text().strip().encode("utf8")
                    port = tds[2].get_text().strip()
                    protocol = "http" if tds[5].get_text().strip(
                    ).lower() == "http" else "https"
                    proxies = {protocol: protocol + "://" + ip + ":" + port}
                    try:
                        resp = requests.get(
                            TESTURL, proxies=proxies, timeout=8)
                        if resp.status_code == 200:
                            retList.append(proxies.values()[0])
                            print(proxies.values()[0] + "...ok!")
                    except Exception, e:
                        print e
                        continue
                time.sleep(1)
        with open(dbfile, "w") as f:
            f.writelines("\n".join(retList))
        driver.quit()
    for ret in retList:
        yield ret


# return a random proxy string if many is default 1
# else return a generator with many proxy elements
def randomProxy(many=1):
    proxyList = [x for x in fetcher()]  # convert generator to list
    randomList = []
    #  check connectivity of this random proxy
    while True:
        proxy = random.choice(proxyList)
        if proxy not in randomList:
            try:
                proxies = {proxy.split("://")[0]: proxy}
                resp = requests.get(TESTURL, proxies=proxies)
                if resp.status_code == 200:  # make sure it's ok
                    randomList.append(proxy)
                    yield proxy
            except Exception, e:  # if something bad happends
                print e
                proxy = randomProxy()  # return a new randomProxy
                randomList.append(proxy)
            if len(randomList) == many:
                return

if __name__ == '__main__':
    proxy = randomProxy(many=20)
    for p in proxy:
        print p
