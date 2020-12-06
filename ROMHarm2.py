#This code imports the necessary modules.

import random
import shutil
import os
from subprocess import call

srchstr = 'C:\\Users\\mysti\\Media_Files\\Sounds\\Acid_Loops'

contenttot= []

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        fil = file[:4]

        contenttot.append(fil.lower())

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

        if pivstr == piv2str and pivstr != 'y' and pivstr != 'a':
            sublst.append(testr.strip())

    if len(sublst) > 1:        

        fich = sublst[-1]

    if len(sublst) <= 1:

        totch = random.randrange(totlen)

        fich = contenttot[totch]

    finlst.append(fich)

    print(fich)

print(finlst)

#call(["python", "DJProcessor.py"])

## THE GHOST OF THE SHADOW ##
