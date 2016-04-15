#!/usr/bin/env python
'''
  This script parses the XML files from a XML site
'''


## -*- coding: iso-8859-1 -*-
# -*- coding: utf-8 -*-

from lxml import html
import requests

# Page http://www.srf.ch/sendungen/wissenschaftsmagazin
page_srf = requests.get('http://....xml', stream=True)
tree_srf = html.fromstring(page_srf.content)

# print(tree_srf.xpath('//div[@class="module-content"]/ul/li/text()'))


for child_of_root in tree_srf:
   print("CHILD: ", child_of_root.tag, child_of_root.attrib)


# http://robotframework.org/robotframework/latest/libraries/XML.html
# http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree
# for elem in tree_srf.iterfind('branch/sub-branch'):
#   print elem.tag, elem.attrib

print("============================")
# Finding interesting elements
for elem in tree_srf.iter():
    # Print elements and tags to find the most interesting tags
    # print("ELEM: ", elem.tag, elem.attrib, elem.text)
    if elem.tag == 'title':
        print("TITLE: ", elem.text)
    if elem.tag == 'description':
        print('DESCRIPTION: ', elem.text)
    if elem.tag == 'guid':
        print("GUID (tag, attribute, text): ", elem.tag, elem.attrib, elem.text)
        print("\n====================\n")

        
print("ooooooooooooo")
for event, elem in tree_srf.iterparse():
    if event == 'end':
        if elem.tag == 'description' and elem.text == 'Wissen':
            print('DESCRIPTION: ', elem.text)
            count += 1
    elem.clear() # discard the element
    
    
## Only description tag
#count = 0
#for elem in tree_srf.iter(tag='description'):
#   print("ELEM: ", elem.tag, elem.attrib, elem.text)
#   if elem.text == 'Wissen':
#       count += 1
#print(count)
