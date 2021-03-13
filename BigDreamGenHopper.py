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
   
srchstr = 'E:\\OriginalAudio\\Songs'

contentdat = {}

for subdir, dirs, files in os.walk(srchstr):
    for file in files:
        filepath = subdir + os.sep + file

        if  filepath.endswith(".wav") or filepath.endswith(".mp3") :

            tim = os.path.getmtime(filepath)

            contentdat[filepath] = tim

mapl = []

newplyd = []

for w in sorted(contentdat, key=contentdat.get, reverse=False):
    mapl.append(w)
    newplyd.append(contentdat[w])

#hopl = [(0, -2), (0, -1), (0, 0), (0 , 1,), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2), (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2)]

hopl = []

for obj in range(24):
    a = random_number2(-2, 2)
    b = random_number2(-2, 2)
    hopl.append((a,b))

moves = 50

fst = random_number(len(mapl))

outmap = []

for ctr in range(moves):
    hopran = random_number(len(hopl))
    aval = (sum(int(i) for i in hopl[hopran])) * 4
    fst += aval
    astr = mapl[fst]
    outmap.append(astr) 
    mapl.remove(astr)
    bighop = random_number(10)
    if bighop > 7:
        fst = random_number(len(mapl))

print(outmap)


