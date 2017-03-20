# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 10:38:30 2016

@author: nlope
"""

import os

folder = 'C://Users//nlope//Desktop//Data_Files'

for i in os.listdir(folder):
    if i =="Original_Files":
#        print i
        new_folder=folder+"//"+i
      #  print new_folder
        #look at ALL the data files
        #x=each individual data file in main directory, i.e. Test
        for x in os.listdir(folder+"//"+i):
            #print x
            #creates new files that corresponds to original file where edits will be stored if file does not exist yet
            if os.listdir(folder+"//"+"Updated_Files") == []: 
                os.makedirs(folder+"//"+"Updated_Files"+"//"+x)
                print x
            else: 
                for z in os.listdir(folder+"//"+"Updated_Files"):
                    if not os.path.exists(folder+"//"+"Updated_Files"+"//"+x):
                        os.makedirs(folder+"//"+"Updated_Files"+"//"+x)
                        print x
                
            #goes into each original sub-directory to search for specific file (i.e. header or README)    
            for sub_dir in os.listdir(folder+"//"+i+"//"+x):
                print sub_dir
                #changes to Header file
                if sub_dir=="Header.txt":
                    with open (folder+"//"+i+"//"+x+"//"+sub_dir) as f:
                        header=f.read()
#                        #find where change needs to be made in txt file
#                        #add change
                        newheader="STANDARD HEADING: "+header
                        #saves changes to new txt file in the updated_file 
                        update_file = open(folder+"//"+'Updated_Files'+"//"+x+"//"+sub_dir,'w')
                        update_file.write(newheader) 
                        update_file.close() 
                          #changes to Header file
                if sub_dir=="README.txt":
                    with open (folder+"//"+i+"//"+x+"//"+sub_dir) as f:
                        readme=f.read()
#                        #find where change needs to be made in txt  
                        #regex here
                        
                        
                        
#                        #add change
                        updates="STANDARD HEADING: "+readme
                        #saves changes to new txt file in the updated_file 
                        update_file = open(folder+"//"+'Updated_Files'+"//"+x+"//"+sub_dir,'w')
                        update_file.write(updates) 
                        update_file.close() 
                                                
                                                
                        

#                
#                if sub_dir=="README.txt":
#                    with open (folder+"//"+i+"//"+x+"//"+sub_dir) as f:
#                        readme=f.read()
#                        print readme      
           # with open('C://Users//nlope//Desktop//Data_Files//'+i)as orig_f:
    
     

    
    #with open (i,'wb') as o:
    #for i in os.listdir(folder):

