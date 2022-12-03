#impoertieren der benötigten Bibliotheken
import random
import matplotlib.pyplot as plt
import numpy as np

#Definieren der Grundvariablen
E = 3600
xPvalue = 0
xEvalue = 0
yEvalue = 0

#Definieren der benötigten Listen
xPliste = [0]
yPliste = [0]

xEliste = []
yEliste = []

for a in range(15):
    dt = random.randrange(1,10)
    P = E/dt
    
    xPvalue = xPvalue + dt
    yPvalue = P
    
    xEvalue = (xEvalue + dt)
    yEvalue = (yEvalue + E)
    
    #Werte den Listen hinzufügen
    xPliste.append(xPvalue)
    yPliste.append(yPvalue)
    
    xEliste.append(xEvalue)
    yEliste.append(yEvalue)
        
print(xPliste)
print(yPliste)
print(xEliste)
print(yEliste)



fp = open("write_demos.txt", 'a')
for item in xPliste:
        # write each item on a new line
        fp.write("%s\n" % item)
        
xPliste = []
fp = open("write_demos.txt", 'r')
for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = float(line[:-1])

        # add current item to the list
        xPliste.append(x)
        
fp = open("write_demos - Kopie.txt", 'a')
for item in yPliste:
        # write each item on a new line
        fp.write("%s\n" % item)
        
yPliste = []
fp = open("write_demos - Kopie.txt", 'r')
for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
        x = float(line[:-1])

        # add current item to the list
        yPliste.append(x)



fig, ax = plt.subplots()

ax.step(xPliste,yPliste)
plt.ylabel('Leistung [W]')
plt.xlabel('Zeit [s]')
plt.show()

plt.plot(xEliste,yEliste)
plt.ylabel('Energie [Ws]')
plt.xlabel('Zeit [s]')
plt.show()


