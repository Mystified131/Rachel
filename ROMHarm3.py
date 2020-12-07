#This code imports the necessary modules.

import random
import os
from PIL import Image 
import time

srchstr = 'C:\\Users\\mysti\\Media_Files\\Dreams'

contenttot= []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        contenttot.append(filepath)

totlen = len(contenttot)

totch = random.randrange(totlen)

fich = contenttot[totch]

print(fich)

finlst = []

for ctr in range(10):
 
    sublst = []

    pivstr = fich[-19:-5]

    for elem in range(totlen):
        testr = contenttot[elem]
        piv2str = testr[-8:-6]

        #As y and a cause endless replication, they are like a virus, and the program learns entropy by avoiding them

        if piv2str in pivstr and pivstr != 'y' and pivstr != 'a':
            sublst.append(testr.strip())

    if len(sublst) > 1:        

        fich = sublst[-1]

        finlst.append(sublst)

        print(sublst)

    if len(sublst) <= 1:

        totch = random.randrange(totlen)

        fich = contenttot[totch]

        finlst.append(fich)

        print(fich)

for elem in finlst:

    ellen = len(elem)
    im = random.randrange(ellen)

    dream = elem[im]

    img = Image.open(dream)
    
    img.show() 
        
    time.sleep(4)

## THE GHOST OF THE SHADOW ##
