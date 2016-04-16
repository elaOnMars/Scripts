#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
    This script scrapes the news entries from the University of Cologne.
    As the news site is not in XML format, it is a little bit tricky to parse
    the content of the site including the links. The links had to be reconstructed new.

    Usefull help sites: 
    -------------------
    Extracting attributes from HTML with lxml: 
    - http://lxml.de/tutorial.html
    - http://stackoverflow.com/questions/27070227/extracting-attributes-from-html-with-lxml
    
    
    
    Daniela Knoll - 2016-04-16
    @ElaOnMars
'''

from lxml import html
import requests

url = 'http://www.portal.uni-koeln.de/presseinformationen.html'
root_link = 'http://www.portal.uni-koeln.de/presseinformationen.html'

# Get content of URL
page_srf = requests.get(url, stream=True)
tree_srf = html.fromstring(page_srf.content)

# print("LIST :: ", tree_srf.xpath('//p[@class="bodytext"]/text()'))     # Debugging
# print("Length Headlines: ", len(tree_srf.xpath('//span[@itemprop="headline"]/text()')))      # Debugging
# print("Length Text: ", len(tree_srf.xpath('//p[@class="bodytext"]/text()')))      # Debugging

root_link = "http://www.portal.uni-koeln.de/"

print("")

count = 0
for elem in tree_srf.iter():
    # Prevent that the loop goes out of range
    if count <= len(tree_srf.xpath('//span[@itemprop="headline"]/text()'))-1:  
        
        headline = tree_srf.xpath('//span[@itemprop="headline"]/text()')[count]
        sub_headline = tree_srf.xpath('//p[@class="bodytext"]/text()')[count]
        date = tree_srf.xpath('//time[@datetime]/text()')[count]  
        
        # print("HEADLINE Type: ", headline, " :: ", type(headline))      # Get type 
                      
        if tree_srf.xpath('//span[@itemprop="headline"]/text()'):
            print("Headline: ", headline)
            # print("count headline = ", count) 
        if tree_srf.xpath('//p[@class="bodytext"]/text()'):
            print("Sub headline: ", sub_headline)
            # print("count sub headline = ", count) 
        if tree_srf.xpath('//time[@datetime]/text()'):
            print("Date published: ", date)
            # print("count date = ", count) 
            
        # The complete HTML link is missing in the source code AND in the HTML tag.
        # You need to join the link with the root link.
        # To fetch the link use lxml etree function.
        # Example link: http://www.portal.uni-koeln.de/nachricht.html?&tx_news_pi1%5Bnews%5D=4087&tx_news_pi1%5Bcontroller%5D=News&tx_news_pi1%5Baction%5D=detail&cHash=86928ed18cae61dc15e23dc48a66d037
        # Example source:
        '''
        I have:
         <div class="header">
            <h3>
              <a title="Von Grenzen und Gemeinsamkeiten " href="nachricht.html?&amp;tx_news_pi1%5Bnews%5D=4088&amp;tx_news_pi1%5Bcontroller%5D=News&amp;tx_news_pi1%5Baction%5D=detail&amp;cHash=e6eae7a260e9204754f4c431994a15ea">
                <span itemprop="headline">Von Grenzen und Gemeinsamkeiten </span>
              </a>
            </h3>
          </div>
        '''
        
        # Get HTML link out of HTML tag
        # Help: http://stackoverflow.com/questions/27070227/extracting-attributes-from-html-with-lxml
        # for link_element in tree_srf.xpath('//div[contains(@class, header)]//a[contains(@title, "Von Grenzen und Gemeinsamkeiten ")]'):
        for link_element in tree_srf.xpath('//div[contains(@class, header)]//a[contains(@title, "' + headline + '")]'):
            # Get HTML link of subtree
            href = link_element.get('href')
            link = root_link + href
            print("HREF: ", link)    
            
            # image_element = href.find('img')
            # if image_element:
                # img_src = image_element.get('src')
            
            # Terminate the current loop and resume outside this loop.
            # I use this fix as the original source code has double entries which I
            # don't like to have in the output.
            break
            
        #print("count all = ", count)      # Control counts 
        count += 1
        
        print("\n=================\n")

# Clear cache
count.clear()
elem.clear()
url.clear()
root_link.clear()
page_srf.clear()
tree_srf.clear()


# http://robotframework.org/robotframework/latest/libraries/XML.html
# http://eli.thegreenplace.net/2012/03/15/processing-xml-in-python-with-elementtree
# for elem in tree_srf.iterfind('branch/sub-branch'):
#   print elem.tag, elem.attrib


# print("============================")


## 

# If you have an ordinary XML site you can use the following construction.
# Otherwise you have to frickle with the code above!

# Finding interesting elements
for elem in tree_srf.iter():
    # Print the elements first, then you can choose what you like to print
    #print("ELEM: ", elem.tag, elem.attrib, elem.text)
    if elem.tag == 'title':
        print("TITLE: ", elem.text)
    
    if elem.tag == 'summary':
        print('summary: ', elem.text)
 
    # Bad formated HTML files view above:
        #print(tree_srf.xpath('//p[@class="bodytext"]/text()'))
        
# Clear cache
elem.clear()
