#!/usr/bin/python3
# coding: utf-8

# https://pythonprogramming.net/parse-website-using-regular-expressions-urllib/
import urllib.request
import re

url = 'http://podcasts.srf.ch/wissenschaft_drs_2_mpx.xml'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'<description>(.*?)</description>',str(respData))
#print(paragraphs)

for eachDescr in paragraphs:
    print("\n", eachDescr)
