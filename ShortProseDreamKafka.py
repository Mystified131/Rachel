#This code imports the necessary modules.

import random
import os
from collections import defaultdict
import datetime
import re
from unidecode import unidecode
from string import digits

#this code retrieves the date and time from the computer, to create the timestamp

right_now = datetime.datetime.now().isoformat()
list = []

for i in right_now:
    if i.isnumeric():
        list.append(i)

time = ("".join(list))
   
#srchstr = "C:\\Users\\mysti\\Desktop\Bin\\02_NewPoems"

srchstr = "C:\\Users\\mysti\\Desktop\\Bin\\Texts"

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".txt") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

newply = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    newply.append(w)
    newplyd.append(contentdat[w])

totlen = len(newply)

totch = random.randrange(totlen)

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

        trok = random.randrange(subl) 

        fich = sublst[trok]

        finlst.append(fich)

    if len(sublst) <= 1:

        totch = random.randrange(totlen)

        fich = newply[totch]

        finlst.append(fich)

txlst = []

wdlst = []

for docnam in finlst:

    sublst = []

    par = ""

    with open(docnam, "r") as f:
        try:
            par = f.read()
        except:
            print("Unicode error")

    sublst = par.split()

    for elem in sublst:

        elem2 = elem.strip()

        if elem2[0] != "." and elem2[0] != "!" and elem2[0] != "?":

            wdlst.append(elem2)

subl = []

bigl = []

sub2 = []

lam = len(wdlst)

for x in range(20):
    y = random.randrange(lam)
    adstr = wdlst[y]
    if len(adstr) > 5:
        sub2.append(wdlst[y])

sennum = 0

for elem in wdlst:
    if len(subl) > 0:

        subl.append(elem)

    if len(subl) == 0:

        elem2 = elem[0].upper() + elem[1:]
        subl.append(elem2)

    if elem.endswith(".") or elem.endswith("!") or elem.endswith("?") :
        flg = 0
        for elem3 in subl:
            if elem3 in sub2:
                    flg += 1
        if flg > 0:
            bigl.append(subl)
            sennum += 1
            parran = random.randrange(5)
            if parran > 3 and sennum > 4 and len(subl) > 4:
                bigl.append('\n')
                bigl.append('\n')
                sennum = 0

        subl = []

ctr = len(bigl)

if ctr > 1000:
    ctr = 1000

lim = ctr - 5

polst = []

for x in range (ctr):
    lin = random.randrange(lim)

    rem = random.randrange(1,3)

    for y in range(rem):

        polst.append(bigl[lin + y])

    polst.append("")

bigstr = ""


for elem in polst:
    for elem2 in elem:

        if elem != '\n':

            bigstr += elem2 + " "


        if elem == '\n':

            bigstr += elem2 


endstr = unidecode(bigstr)
endstr2 = endstr.replace("THE CASTLE", "")
endstr3 = endstr2.replace("ANOTHER VERSION", "")

remove_digits = str.maketrans('', '', digits)
endstr5 = endstr3.translate(remove_digits)


ounm = "Short_Prose_Dream_" + time + ".txt"

oun = "Short Prose Dream " + time 

outfile = open(ounm, "w")

outfile.write(oun + '\n')

outfile.write( '\n')

try:
    outfile.write(endstr5 + '\n')
except:
    print("")
    print("Unicode error")

outfile.close()       

print("")

print("Your document is saved in the same folder as this code.")

## THE GHOST OF THE SHADOW ##