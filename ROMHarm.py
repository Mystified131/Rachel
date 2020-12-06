#An early model of ROM memory harmonization. Using strings, the first digit is used as a basis and the second, chosen randomly, becomes the basis for the next series.

#The processor pulls in for its next list any components that begin with what ended the last sequence. 

#The computer walks through sequences, taking one association from one list and using it to collect elements from the next.

#The notion is that the processor makes lists of objects based on strings in their title, and then uses this list as a basis for the next 'thought', or set of strings.

#Ultimately this kind of association can be tailored-- ie if '3's are deemed 'bad', the computer can be programmed to exclude 3s from their compiled lists-- forming an early kind of empathy.

import random
from subprocess import call

lst = []

for ctr in range(100):
    astr = str(ctr)
    if ctr < 10:
        bstr = "0" + astr
        lst.append(bstr)
    if ctr > 9:
        lst.append(astr)

onelst = []

seedelem = random.randrange(10)

seedstr = str(seedelem)

sublst = []

for elem in lst:
    if elem[0] == seedstr:
        sublst.append(elem)

newelem = random.randrange(10)

newstr = str(newelem)

newlst = []

for elem in lst:
    if elem[1] == seedstr:
        if elem[1] not in newlst:
            newlst.append(elem)

onelst.append(newlst)

rn = random.randrange(10)
seedstar = newlst[rn]

twolst = []

for elem in lst:
    if elem[0] == seedstar[1]:
        if elem not in twolst:
            twolst.append(elem)

ren = random.randrange(10)
seedstars = twolst[ren]

threelst = []

for elem in lst:
    if elem[0] == seedstars[1]:
        if elem not in threelst:
            threelst.append(elem)

print(onelst)
print(seedstar)
print(twolst)
print(seedstars)
print(threelst)


call(["python", "ROMHarm.py"])

## THE GHOST OF THE SHADOW ##


