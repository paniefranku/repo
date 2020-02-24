import csv
import sys
import glob
import os

# CSV folder
path = 'C:/Users/Admin/Desktop/kody/'

for root,dirs,_ in os.walk(path):
    for d in dirs:
        path_sub = os.path.join(root,d)
        for filepath in glob.glob(os.path.join(path_sub, '*.csv')):
            address = os.path.split(filepath)[0] # get the path of the all csv
            name = os.path.split(filepath)[1] # get the name of the all csv file
            if not name.startswith('output'): # filter out unwanted .csv files
                src = (address + '\\' + name) # absolute path
                print (src)
                with open(src) as f:
                    content = csv.reader(src, delimiter=",") # opened csv files
                    print (content)
                    number = input ('wprowadź kod invalid: ')
                    for (row) in content:
                        if number == (row[10]):
                                print (row[1])
                        else:
                            for (row) in content(1):
                                if number == (row[10]):
                                    print (row[1])