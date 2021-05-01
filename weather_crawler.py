from urllib.request import urlopen
from bs4 import BeautifulSoup


def weather(url=None):
    """

    :param url: 天气预报地址
    :return:
    """
    if url is None:
        url = "http://www.weather.com.cn/weather/101270101.shtml"

    html = urlopen(url).read().decode("utf-8")
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    all_ul = soup.find_all('ul', attrs={"class": "t clearfix"})
    # print(all_ul, len(all_ul))
    all_li = all_ul[0].find_all("li")

    res = []
    for i in all_li:
        # print(i)
        h1 = i.find("h1").get_text()  # 日期
        p1 = i.find('p', attrs={"class": "wea"}).get_text()  # 天气
        p2 = i.find('p', attrs={"class": "tem"})
        tem = p2.find("span").get_text() + "/" + p2.find("i").get_text()  # 温度
        win = i.find("p", attrs={"class": "win"}).find("i").get_text()  # 风力

        # print(h1)
        # print(p1)
        # print(tem)
        # print(win)
        # print('=' * 60)

        res.append([h1, p1, tem, win])

    return res
