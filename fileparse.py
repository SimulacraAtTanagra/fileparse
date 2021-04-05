# -*- coding: utf-8 -*-
"""
Created on Wed Jan 15 11:09:59 2020

@author: sayers
"""

#this is the code to strip and flash-audit cjr files

import pandas
import os
import math
import glob


directory_in_str = 'S:\\Downloads'
def main():
    df = pandas.DataFrame().astype('object')                #makes it so things can be stored in df that are lists
    directory = os.fsencode(directory_in_str)           #defines directory as indicated string
    os.chdir(directory)                                 #navigate to directory specified
    for file in os.listdir(directory):                  #iterates over all the files here
        filename = os.fsdecode(file)                    #specifies filename from file
        if filename.endswith(".b"):                  #isolates epub for further action
            try:
                df = df.append(corpus_processing(epub_to_text(filename)),ignore_index=True)  #appends results of function to df
            except:
                print(filename,"produced an error. Continuing.")        #or lets you know it couldn't
        elif filename.endswith(".pdf"):                  #isolates epub for further action
            try:
                df = df.append(corpus_processing(pdf_to_text(filename)),ignore_index=True)  #appends results of function to df
            except:
                print(filename,"produced an error. Continuing.")        #or lets you know it couldn't

        else:
            continue
    else:
        df.to_csv('summaryoutput.csv',index=False)      #writes dataframe to csv file to save memory

#main()

df = pandas.DataFrame().astype('object')                #makes it so things can be stored in df that are lists
directory = os.fsencode(directory_in_str)           #defines directory as indicated string
os.chdir(directory)                                 #navigate to directory specified
for file in os.listdir(directory):                  #iterates over all the files here
    filename = os.fsdecode(file)                    #specifies filename from file
    if file.glob(".*"):                  #isolates epub for further action
        try:
            print(filename)
        except:
            print(filename,"produced an error. Continuing.")        #or lets you know it couldn't
list_of_files = glob.glob(directory_in_str+'/'+ 'full_file'+'*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print latest_file

for file in os.listdir(directory): 
    x= (max(glob.glob(directory_in_str+'/'+ 'full_file'+'*')),key=os.path.getctime)
    print(x)