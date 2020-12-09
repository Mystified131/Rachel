#This code imports the necessary modules.

import random
import shutil
import os
from subprocess import call

srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

contenttot= []

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        fil = file[:4]

        tim = os.path.getctime(filepath)

        lst = fil.lower()

        contentdat[lst] = tim

        contenttot.append(lst)

#print(contenttot)

totlen = len(contenttot)

totch = random.randrange(totlen)

fich = contenttot[totch]

print(fich)

finlst = []

for ctr in range(100):
 
    sublst = []

    pivstr = fich[-1:]

    for elem in range(totlen):
        testr = contenttot[elem]
        piv2str = testr[0]

        #As y and a cause endless replication, they are like a virus, and the program learns entropy by avoiding them

        if pivstr == piv2str and pivstr != 'y' and pivstr != 'a':
            sublst.append(testr.strip())

            print(contentdat[testr])

    if len(sublst) > 1:        

        fich = sublst[-1]

        finlst.append(sublst)

        print(sublst)

    if len(sublst) <= 1:

        totch = random.randrange(totlen)

        fich = contenttot[totch]

        finlst.append(fich)

        print(fich)

print(finlst)

#call(["python", "DJProcessor.py"])

## THE GHOST OF THE SHADOW ##
