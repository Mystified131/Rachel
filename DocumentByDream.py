#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
from RandFunct import random_number
from RandFunct2 import random_number2

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))
   

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

#srchstr = 'E:\\OriginalAudio\\Songs'

#srchstr = 'C:\\Users\\mysti\\Downloads'

#srchstr = "C:\\Users\\mysti\\Media_Files\\Sounds\\OlderSounds"

srchstr = "C:\\Users\\mysti\\Desktop\Bin\\02_NewPoems"

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".txt"):

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

totlen = len(newply)

totch = random_number(totlen)

fitch = newply[totch]

fich = str(newplyd[totch])

finlst = []

for ctr in range(50):
 
    sublst = []

    for elem in range(totlen):
        tesstr = newply[elem]
        testr = str(newplyd[elem])
        piv2str = testr[-10:-8]

        if piv2str in fich:
            sublst.append(tesstr)

    if len(sublst) > 1:   

        subl = len(sublst)    

        trok = random_number(subl) 

        fich = sublst[trok]

        finlst.append(fich)

    if len(sublst) <= 1:

        totch = random_number(totlen)

        fich = newply[totch]

        finlst.append(fich)

ounm = "Dream_Document_" + time + ".txt"

outfile = open(ounm, "w")

for docnam in finlst:

    infile = open(docnam, "r")

    plist = infile.readline()
    while plist:
        outfile.write(plist + '\n')
        plist = infile.readline()
    infile.close()
    outfile.write('\n')
    outfile.write('________________________' + '\n')
    outfile.write('\n')
    outfile.write('\n')

outfile.close()       

print("")

print("Your document is saved in the same fodler as this code.")

## THE GHOST OF THE SHADOW ##