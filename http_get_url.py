#!/usr/bin/env python
import requests

def http_get_url():
    srcpath = "" 
    dstpath = "."
    serverName = ""
    separator = "!"
    secureName = c""
    file = open(srcpath)
    file_str = open(dstpath, 'wb')
    for url_path in file.readlines():
        url = "http://"+serverName+".b0.upaiyun.com"+url_path.strip('\n')
        req_url = requests.head(url)
        print url
        if req_url.status_code == 404:
           se_url = url+separator+secureName
           req_se_url = requests.head(se_url)
           if req_se_url.status_code == 200:
           		print se_url
           		file_str.write(url)

    file.close()
    file_str.close()


http_get_url()
