# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 11:19:47 2017

@author: natlopez
"""
import requests
import bs4
import os
import csv

url = 'https://www.nga.org/cms/stateaddresses'
response = requests.get(url)
html = response.text

#print (html)

soup = bs4.BeautifulSoup(html, "lxml")
#print (soup)
tr = soup.findAll('tr')
#print (tr)
#print (tr[0].findAll('p'))

#os.makedirs('C:/Users/natlopez/Desktop//gubernatorial_ssa')
parent_file="C:/Users/natlopez/Desktop/gubernatorial_ssa//2017_gubernatorial_ssa"
##creates master csv_file
with open (parent_file+'.csv','w', newline='') as outputFile:
    outputWriter=csv.writer(outputFile)
    outputWriter.writerow(['State', 'Date', 'URL'])
    for t in tr[1:]: 
        row = t.findAll('p')
        state=row[0].get_text()
        date=row[1].get_text()
        new_row = [state, date]
        for link in t.findAll('a', href=True):
            new_row.append (link["href"])
            ssa_speech=requests.get(link['href'])
            if ((link["href"])[-3:])=="pdf":
                with open (parent_file + "_" + state + "_" + "_" +date +'.pdf','wb') as o:
                    o.write(ssa_speech.content)
            else:
                with open (parent_file + "_" + state + "_" + "_" +date +'.txt','w', encoding='utf-8') as o:
                    o.write(ssa_speech.text)
                

#                ssa_speech_txt=ssa_speech.text
##                print(ssa_speech_txt)
##                unicode_str=ssa_speech_txt.decode("windows-1252")
##                encoded_str=unicode_str.encode('utf8')
#                o.write(ssa_speech_txt)
#            print (requests.get(link["href"]))
#        print (new_row)
        outputWriter.writerow(new_row)
        
##outputs individual txt files w/ speeches

        

