import random
import urllib
import urllib.request

from libs.Py4Js import *


class TransTool:
    def __init__(self, headers=None, charset=None, proxy=None):
        if headers == None:
            self.headers = self.getheaders()
        else:
            self.headers = headers
        if charset == None:
            self.charset = 'utf-8'
        else:
            self.charset = charset
        self.proxy = proxy

    def getheaders(self):
        user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1" 
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]
        UserAgent = random.choice(user_agent_list)
        headers = {'User-Agent': UserAgent}
        return headers

    def proxys(self):
        proxy_list = [
            '183.30.197.179:9797',
            '115.223.219.76:9000',
            '117.90.137.229:9000',
            '218.89.97.189:9000',
            '219.150.189.212:9999',
        ]
        proxy = random.choice(proxy_list)
        return {"http":proxy}

    def openUrl(self, url):
        headers = self.headers
        ######################## 加入代理服务器 - begin ################################
        if self.proxy != None:
            self.proxy = self.proxy
            print('使用代理服务器:')
            print(self.proxy)
            req = urllib.request.Request(url=url, headers=headers)
            proxy_handler = urllib.request.ProxyHandler(self.proxy)
            opener = urllib.request.build_opener(proxy_handler)
            urllib.request.install_opener(opener)

            response = urllib.request.urlopen(req)
            data = response.read().decode(self.charset)
        ######################## 加入代理服务器 - End ##################################
        else:
            req = urllib.request.Request(url=url, headers=headers)
            response = urllib.request.urlopen(req)
            data = response.read().decode(self.charset)
        return data

    def translate(self, content, sourceLanguage, targetLanguage):
        if len(content) > 4891:
            print("翻译的长度超过限制！！！")
            return
        js = Py4Js()
        tk = js.getTk(content)
        content = urllib.parse.quote(content)

        url = "http://translate.google.cn/translate_a/single?client=t" \
              "&sl=" + sourceLanguage + "&tl=" + targetLanguage + "&hl=" + sourceLanguage + "&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                                                                                            "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                                                                                            "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (
                                                                                                tk, content)

        result = self.openUrl(url)

        end = result.find("\",")
        if end > 4:
            return result[4:end]
        return ''

    def dataFromFile(self, sourceFile):
        fr = open(sourceFile, encoding='utf-8')
        arrayOlines = fr.readlines()
        fr.close()
        return arrayOlines

    def dataFromJsonFile(self, sourceFile):
        fr = open(sourceFile, encoding='utf-8')
        arrayOlines = fr.readlines()
        jsonStr = ''
        return jsonStr.join(arrayOlines)

    def dataToFile(self, arrayOlines, targetFile):
        wr = open(targetFile, "w+", encoding='utf-8')
        for line in arrayOlines:
            newLine = line.strip()
            wr.write(newLine + "\n")

    def getLanguageCode(self):
        language = {}
        language['en'] = 'en'
        language['fr'] = 'fr'
        language['de'] = 'de'
        language['ru'] = 'ru'
        language['ar'] = 'ar'
        language['es'] = 'es'
        language['hi'] = 'hi'
        language['it'] = 'it'
        language['ja'] = 'ja'
        language['nl'] = 'nl'
        language['pl'] = 'pl'
        language['pt'] = 'pt'
        language['tr'] = 'tr'
        language['uk'] = 'uk'
        language['iw'] = 'iw'
        return language

    def getLanuage(self):
        language = {}
        # language['zh-CN'] = '中国'
        # language['en'] = '英语'
        # language['ja'] = '日语'
        # language['fr'] = '法语'
        # language['de'] = '德语'
        # language['es'] = '西班牙'
        # language['pt'] = '葡萄牙'
        # language['it'] = '意大利'
        language['nl'] = '荷兰'
        language['ru'] = '俄语'
        language['pl'] = '波兰'
        language['tr'] = '土耳其'
        # language['hi'] = '印度'
        # language['ar'] = '阿拉伯'
        # language['iw'] = '希伯来'
        # language['uk'] = '乌克兰'
        return language
