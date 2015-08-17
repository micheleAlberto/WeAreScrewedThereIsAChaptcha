f=open("pi.txt")
i=0
s=0
for l in f.readlines():
    for c in l:
        try:
            s+=int(c)
            i+=1
        except:
            pass
        if i==31415:
            print "somma :" ,s

f=open("pi2.txt")
i=2
s=2
#le prime due cifre sono 11 per il 3.
for l in f.readlines():
    for c in l: 
     if len(l)==73:
        try:
            s+=int(c)
            i+=1
        except:
            pass
        if i==31415:
            print "somma :" ,s

