import csv

with open("model.csv") as fd:
    rd = csv.reader(fd, delimiter="\t")
    f = open("model.xml", "w")
    f.write('<INVENTORY>\n')
    next(rd)
    for row in rd:
        if len(row[0]) == 0:
            break
        f.write('<ITEM>\n')
        f.write('<ITEMTYPE>P</ITEMTYPE>\n')
        f.write('<ITEMID>{}</ITEMID>\n'.format(row[0]))
        f.write('<COLOR>{}</COLOR>\n'.format(row[4]))
        f.write('<QTYFILLED>{}</QTYFILLED>\n'.format(row[8]))
        f.write('<CONDITION>N</CONDITION>\n')
        f.write('</ITEM>\n')
    f.write('</INVENTORY>\n')
    f.close()