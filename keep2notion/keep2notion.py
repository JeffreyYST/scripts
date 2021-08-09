#!/usr/bin/env python 

import gkeepapi 
keep = gkeepapi.Keep()
success = keep.login('')
# gnotes = keep.all()
import datetime
import pickle 
gnotes = pickle.load(open('gnotes.txt', 'rb'))

for note in gnotes:

    print(note.title)
    pageTitle = note.title.replace("/", "_") if (note.title) else note.timestamps.created.strftime('%Y-%d-%m_%H_%M_%S')
    f = open("imports/"+pageTitle+".md", "w", encoding="utf8")
    f.write("# "+pageTitle+"\n\n")
    f.write("Content\n")
    text = note.text.replace('\u2610', '\n-')
    text = text.replace('\u27a5', '&rarr;')
    text = text.replace('\u2264', '$leq$')
    print(text)
    f.write(text)

    for img in note.images:
        link = keep.getMediaLink(img)
        print(link+"\n")
        f.write('\n['+link+']')
        f.write('('+link+')\n\n')


    f.write("\n")
    
    f.close()
    print('\n')

