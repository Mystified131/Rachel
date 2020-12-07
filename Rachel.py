#This code imports the necessary modules.

from flask import Flask, render_template, session
import random
import os
import webbrowser

#This code configures the web app.

app = Flask(__name__)
app.config['DEBUG'] = True

app.secret_key = 'noiiugliarfarfar3irg'

@app.route('/', methods=['POST', 'GET'])
def sessstart():
    session['slide'] = 'C:\\Users\\mysti\\Media_Files\\Dreams\\20181012_164535.jpg'
    return render_template('slideshow.html')

#This code constructs the player page. It chooses an item randomly from a set of lists, and, after processing, opens a player page and cues up the item.

@app.route('/player', methods=['POST', 'GET'])
def make_player():
     
    contenttot = []

    contentmus = []

    infile = open("AutoPlayList2.txt", "r")

    plist = infile.readline()
    while plist:
        contentmus.append(plist)
        plist = infile.readline()
    infile.close()

    atracknum1 = random.randrange(0,len(contentmus))
    atrack1 = contentmus[atracknum1]

    infile = open("AutoPlayList.txt", "r")

    plist = infile.readline()
    while plist:
        contenttot.append(plist)
        plist = infile.readline()
    infile.close()

    totlen = len(contenttot)

    fich = session['slide']

    sublst = []

    pivstr = fich[-19:-5]

    for elem in range(totlen):
        testr = contenttot[elem]
        piv2str = testr[-8:-6]

        if piv2str in pivstr:
            sublst.append(testr.strip())

    if len(sublst) > 1:     

        lslen = len(sublst)   

        pl = random.randrange(lslen)

        fich = sublst[pl]

    if len(sublst) <= 1:

        totch = random.randrange(totlen)

        fich = contenttot[totch]

    while(session['slide'] == fich):
      
        totch = random.randrange(totlen)

        fich = contenttot[totch]

    session['slide'] = fich

    return render_template('slideshow.html', toplay1 = fich, toplay2 = atrack1)

webbrowser.open('http://localhost:5000')

## THE GHOST OF THE SHADOW ##

if __name__ == "__main__":
     app.run()