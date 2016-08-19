from threading import stack_size
import urllib.request
import urllib.error
import pymysql
import urllib
import socket
import re

stack_size(32768 * 16)

socket.setdefaulttimeout(60)


def get_Page(url, intf, time=5):
    global data
    try:
        webPage = urllib.request.urlopen(url, timeout=60)
        data = webPage.read()
        data = data.decode('UTF-8')
        urllib.request.urlcleanup()
    except Exception as what:
        if time > 0:
            get_Page(url, time - 1)
        else:
            print("Totaly Failed", what)
            intf = True
            return 'f'
    except urllib.error.HTTPError as e:
        print(e.code)
        if e.code == 404:
            intf = True
            return 'f'
        else:
            get_Page(url, time - 1)
            intf = False

    print("url ===========>>>>" + url)
    return data


conn = pymysql.connect(host='localhost', user='root', passwd='Zhl0714hl', db='Avmoo', charset='utf8')
cur = conn.cursor()

threads = []
count = 118411
page = 3948
tf = False
intf = False
while (True):
    url = 'https://avmo.pw/cn/released/page/'
    url += str(page)
    data = get_Page(url, intf)
    if intf:
        break

    page += 1

    titlearry = re.compile(r'title="(.+?)">').findall(data)
    faxingshijianarry = re.compile(r'/ <date>(.+?)<\/date>').findall(data)
    fanhaoarry = re.compile(r'><date>(.+?)<\/date').findall(data)

    urlarry = re.compile(r'<a class="movie-box" href="(.+?)"').findall(data)

    l_en = len(urlarry)


    for i in range(0,l_en) :

        url = urlarry[i]
        tf = False
        for x in threads:
            if url == x:
                tf = True
                break
            else:
                continue
        if tf:
            continue

        data = get_Page(url, tf)
        if tf:
            break

        if faxingshijianarry[i] == []:
            faxingshijian = "None"
        else:
            faxingshijian = faxingshijianarry[i]

        if fanhaoarry[i] == []:
            fanhao = "None"
        else:
            fanhao = fanhaoarry[i]

        if titlearry[i] == []:
            title = "None"
        else:
            titlie = titlearry[i]

        changduarry = re.compile(r'长度:</span>(.+?)<\/p').findall(data)
        if changduarry == []:
            changdu = "None"
        else:
            changdu = changduarry[0]

        zhizaoarry = re.compile(r'studio/(.+?)">(.+?)<').findall(data)
        if zhizaoarry == []:
            zhizao = "None"
        else:
            zhizao = re.compile(r'studio/(.+?)">(.+?)<').findall(data)[0][1]

        faxingarry = re.compile(r'label/(.+?)">(.+?)<\/a>').findall(data)
        if faxingarry == []:
            faxing = "None"
        else:
            faxing = faxingarry[0][1]

        xiliearry = re.compile(r'series/(.+?)">(.+?)<\/a>').findall(data)
        if xiliearry == []:
            xilie = "None"
        else:
            xilie = xiliearry[0][1]

        leibiearry = re.compile(r'genre/(.+?)">(.+?)<').findall(data)
        leibie = ""
        for l in range(0, len(leibiearry)):
            leibie += leibiearry[l][1] + ","

        Artistsisnull = re.compile(r'star/(.+?)">').findall(data)
        Artists = ""
        artistsimg = ""
        if Artistsisnull == []:
            Artists = "None"
            artistsimg = "None"
        else:
            Artistsarry = re.compile(r'<span>(.+?)<\/span>').findall(data)
            Artistsimgarry = re.compile(r'src="(.+?)" title="">').findall(data)
            for a in Artistsarry:
                Artists += a + ","
            for A in Artistsimgarry:
                artistsimg += A + ","


        bigsimple = ""
        simple = ""
        titleimg = ""
        indeximg = ""
        simplearry = re.compile(r'<img src="https://jp.netcdn.space/digital/video/(.+?)\/').findall(data)
        if simplearry == []:
            titleimg = "None"
            bigsimple = "None"
            simple = "None"
            titleimg = "None"
        else:
            titleimg = "https://jp.netcdn.space/digital/video/" + simplearry[0] + "/" + simplearry[0] + "pl.jpg"
            indeximg = "https://jp.netcdn.space/digital/video/" + simplearry[0] + "/" + simplearry[0] + "ps.jpg"
            if len(simplearry) < 2:
                bigsimple = "None"
                simple = "None"
            else:
                for s in range(1, len(simplearry)):
                    simple += "https://jp.netcdn.space/digital/video/" + simplearry[0] + "/" + simplearry[0] + "-" + str(
                        s) + ".jpg,"
                    bigsimple += "https://jp.netcdn.space/digital/video/" + simplearry[0] + "/" + simplearry[
                        0] + "jp-" + str(s) + ".jpg,"


        sql = "INSERT INTO api_avmoo_api values('%d','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')"
        cur.execute(sql % (
            count, indeximg, titleimg, fanhao, faxingshijian, changdu, zhizao, faxing, xilie, leibie, Artists,artistsimg,simple,
            bigsimple))
        conn.commit()
        print(count)
        count += 1

cur.close()
conn.close()
