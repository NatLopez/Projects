# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 11:25:15 2016

@author: nlope
"""

import os 

folder = 'C://Users//nlope//Desktop//Hub Projects//DeskTracker export//Davis Reference'
with open ('C://Users//nlope//Desktop//Hub Projects//DeskTracker export//output.csv','wb') as o:
    for i in os.listdir(folder):
        with open ('C://Users//nlope//Desktop//Hub Projects//DeskTracker export//Davis Reference/'+i) as f:
            terms=["geolytics","NCDB neighborhood change database", "census boundaries"]
            o.write(f.next())
            o.write(i)
            for row in f: 
                k=0
                for t in terms: 
                    if t in row.lower():
                        #timeseries
                        print row
                        k+=1
                if k >0:
                    o.write(row)
                    print row
            o.write('\n')
                
            
