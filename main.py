#!/usr/bin/python
# -*- coding: UTF-8 -*-

# import http.client
#
# def PrintRequest(request):
#     ''' To print request base info '''
#     #print(request.status, request.reason )
#     #print ('Headers:',request.getheaders())
#     print(request.read())
#
# headers_tmp = {"User-Agent":'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.97 Safari/537.36'}
# conn = http.client.HTTPConnection("developer.china.linkto.king-wear.top",80)
# conn.request('GET',"","/",headers_tmp)
# content = conn.getresponse()
# PrintRequest(content)
import json
import os
import errno
import random
import time
from multiprocessing import Process

from libs import TransTool
obj = TransTool.TransTool()

results = []


def main():
    sourceJsonFile = 'data/source/jsonFile'
    targetPath = 'data/target/'
    sourceLang = 'zh-CN'

    for k, v in obj.getLanuage().items():
        parserJsonFile(sourceJsonFile, sourceLang, targetPath, k, v)

    # for k, v in obj.getLanuage().items():
    #     a = Process(target=parserJsonFile, args=(sourceJsonFile, sourceLang, targetPath, k, v))
    #     a.start()
    #     results.append(a)
        # #结束进程
    parserYiiT(sourceJsonFile,targetPath)
    print("\n" + '===============================================================\n')
    print("\t\t\t\t\t" + '翻译结束')
    print("\n" + '===============================================================\n')


def parserYiiT(sourceJsonFile, targetPath):
    """
    转化为yii2 i18n的翻译语句
    :param sourceJsonFile:
    :param targetPath:
    """
    f = open(sourceJsonFile, encoding='utf-8')
    setting = json.load(f)
    for v in setting:
        watchType = v['watchType']
        watchClassify = watchType[:4]
        watchClassify = watchClassify.lower()
        targetFilePath = targetPath + watchClassify + "_yii2i18n.php"
        wr = open(targetFilePath, "w+", encoding='utf-8')
        wr.write(encapYii2I18n(watchClassify, watchType))
        infos = v['info']
        for info in infos:
            title = info['title']
            wr.write(encapYii2I18n(watchClassify, title))
            bodys = info['body']
            for body in bodys:
                wr.write(encapYii2I18n(watchClassify, body))
        wr.close()
    f.close()


def parserJsonFile(sourceJsonFile, sourceLang, targetPath, targetLang, targeText):
    f = open(sourceJsonFile, encoding='utf-8')
    setting = json.load(f)
    for v in setting:
        watchType = v['watchType']
        watchClassify = watchType[:4]
        targetFilePath = targetPath + '/' + targeText + '/'
        if not os.path.exists(targetFilePath):
            os.makedirs(targetFilePath)
        targetFilePath += 'manual_' + watchClassify + '.php'
        wr = open(targetFilePath, "w+", encoding='utf-8')
        wr.write(beforEncap())
        #wr.write(encapStr(watchType, sourceLang, targetLang))
        infos = v['info']
        for info in infos:
            title = info['title']
            wr.write(encapStr(title, sourceLang, targetLang))
            bodys = info['body']
            for body in bodys:
                wr.write(encapStr(body, sourceLang, targetLang))
        wr.write(afterEncap())
        wr.close()
    f.close()


def encapStr(field, sourceLang, targetLang):
    tField = obj.translate(field, sourceLang, targetLang)
    print("翻译" + targetLang + "完成：原始语言：【" + field + " 】||| 目标语言：【" + tField + '】')
    return '"' + field + '" =>' + '"' + tField + '",' + "\n"


def encapYii2I18n(watchClassify, content):
    return "Yii::t(\"" + watchClassify + "\" ,\"" + content + "\"); \n"


def beforEncap():
    return "<?php \n \t $textConfig = [";


def afterEncap():
    return "];"


def mkdirP(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5 (except OSError, exc: for Python <2.5)
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise


if __name__ == "__main__":
    main()
