import re
total = ''
date = ''
deli = ' '
regextotal = "^\s*total:?\s+(\$?\d*\.?\d*$)"
regexdate =  "date:?(\s+[0-9]{1,2}\\/[0-9]{1,2}\\/[0-9]{4})"
regexadress = "^(\\d{1,}) [a-zA-Z0-9\\s]+(\\,)? [a-zA-Z]+(\\,)? [A-Z]{2} [0-9]{5,6}$"
ptotal = re.compile(regextotal)
pdate = re.compile(regexdate)
with open('a.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        if(len(line)>0):
            mline = line.lower()
            m =  ptotal.search(mline)
            if m:
                total = m.group(1)
            m2 = pdate.search(mline)
            if m2:
                date = m2.group(1)
            #print(mline)
print("Date : ",date)
print("Total : ",total)