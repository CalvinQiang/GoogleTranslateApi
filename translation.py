#! usr/bin/python
# coding=utf-8
# -*- coding:cp936 -*-Z
import re
import urllib
import urllib.request
from multiprocessing import Process
import json

from libs.Py4Js import *


def open_url(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24'}
    req = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(req)
    transJson = json.loads(response.read())
    return transJson


def translate(content, tk, sourceLanguage, targetLanguage):
    if len(content) > 4891:
        print("翻译的长度超过限制！！！")
        return

    content = urllib.parse.quote(content)

    url = "http://translate.google.cn/translate_a/single?client=t" \
          "&sl=" + sourceLanguage + "&tl=" + targetLanguage + "&hl=" + sourceLanguage + "&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
                                                                                        "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
                                                                                        "&srcrom=0&ssel=0&tsel=0&kc=2&tk=%s&q=%s" % (
                                                                                        tk, content)

    result = open_url(url)
    # 这里拼接返回的翻译
    transArr = result[0]
    transStr = ""
    for tStr in transArr:
        tempStr = str(tStr[0])
        transStr += tempStr
    return transStr[:-4]





######################################
#   patterStr       正则表达式
#   txtFile      翻译原文件
#   targetFile      翻译目标文件
#   sourceLanguage  翻译原语言
#   targetLanguage  翻译目标语言
######################################
def file2array(patterStr,sourceFile, targetFile, sourceLanguage, targetLanguage):
    fr = open(sourceFile, encoding='utf-8')
    wr = open(targetFile, "w+", encoding='utf-8')
    arrayOlines = fr.readlines()
    js = Py4Js()
    i = 0
    for line in arrayOlines:
        #time.sleep(1)
        newLine = line.strip()
        patter = re.match(patterStr, newLine)
        if (patter == None):
            wr.write(newLine + "\n")
            continue

        ######### 安卓
        startStr = patter.group(1)
        replaceStr = patter.group(3)
        endStr = patter.group(4)
        ######### iOS
        # startStr = patter.group(1)
        # replaceStr = patter.group(3)
        # endStr = patter.group(4)
        # 获取TK值
        tk = js.getTk(replaceStr)
        transStr = translate(replaceStr, tk, sourceLanguage, targetLanguage)
        print(replaceStr)
        print(transStr)
        print("----------------------------------")
        # if (i >= 5):
        #     break
        # i += 1
        wr.write(startStr + transStr + endStr + "\n")
    fr.close()
    wr.close()


def main():
    baseDir = './translate/'
    # iOS
    #sourceFile = 'Localizable.strings'
    # android
    sourceFile = 'registration-agreement.html'
    # sourceFile = 'privacy-policy.html'
    sourceLanguage = 'zh-CN'
    # iOS翻译
    #patterStr = r'("(.*)"[\s]*=[\s]*")(.*)(";)'
    # 安卓翻译
    # patterStr = r'(^<(.*)>)(.*)(</(.*)>$)'
    # 网页翻译
    patterStr = r'(^<([\w])>)(.*)(</([\w])>$)'
    language = {}
    # language['zh-CN'] = '中国'
    # language['ja'] = '日语'
    # language['fr'] = '法语'
    # language['de'] = '德语'
    # language['es'] = '西班牙'
    # language['pt'] = '葡萄牙'
    # language['it'] = '意大利'
    language['nl'] = '荷兰'
    # language['ru'] = '俄语'
    # language['pl'] = '波兰'
    # language['tr'] = '土耳其'
    # language['hi'] = '印度'
    # language['ar'] = '阿拉伯'
    # language['iw'] = '希伯来'
    # language['uk'] = '乌克兰'

    # language['en'] = 'en'
    # language['fr'] = 'fr'
    # language['de'] = 'de'

    # language['ru'] = 'ru'
    # language['ar'] = 'ar'
    # language['es'] = 'es'
    # language['hi'] = 'hi'
    # language['it'] = 'it'
    # language['ja'] = 'ja'
    #
    # language['nl'] = 'nl'
    # language['pl'] = 'pl'
    # language['pt'] = 'pt'
    # language['tr'] = 'tr'
    #
    # language['uk'] = 'uk'
    # language['iw'] = 'iw'
    results = []
    for v, k in language.items():
        a = Process(target=file2array, args=(patterStr, sourceFile, baseDir+k + '.html', sourceLanguage, v))
        a.start()
        results.append(a)

    #结束进程

if __name__ == "__main__":
    main()
