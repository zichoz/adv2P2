map = open("map.txt.txt")
#print(type(map))
tellerNed = 0
tellerBort= 3
kart = []
#Putter inn alt i en nøstet liste
for line in map:
    line = line.replace("\n","")
    kart.append(line)


def kjoerSlede(hvorMangeBort, hvorMangeNed):
    tellerBort = 0
    antallTre = 0
    for line in kart:
        if line[tellerBort] == "#":
            antallTre += 1
        tellerBort += hvorMangeBort
        if (len(line) - 1) < tellerBort:
            diff = tellerBort - (len(line) - 1)
            tellerBort = diff - 1
    print(antallTre, "antall tre som du krasjær vi ved å gå bort,", hvorMangeBort, "og ned ", hvorMangeNed)
    return antallTre


def kjoerSledeAnnenHverGang(hvorMangeBort, hvorMangeNed):
    tellerBort = 0
    antallTre = 0
    annenhvergang = True
    #hvergangannen = False
    for line in kart:
        if annenhvergang == True:
            if line[tellerBort] == "#":
                antallTre += 1
            tellerBort += hvorMangeBort
            if (len(line) - 1) < tellerBort:
                diff = tellerBort - (len(line) - 1)
                tellerBort = diff - 1
            annenhvergang = False
            continue
        if annenhvergang == False:
            annenhvergang = True

    print(antallTre, "antall tre som du krasjær vi ved å gå bort,", hvorMangeBort, "og ned ", hvorMangeNed)
    return antallTre

kjør11 = kjoerSlede(1,1) #88
kjør31 = kjoerSlede(3, 1) #145
kjør51 = kjoerSlede(5,1) #71
kjør71 = kjoerSlede(7,1) #90
kjør12 = kjoerSledeAnnenHverGang(1,2) #2

faktoravkjør = kjør11 * kjør31 * kjør51 * kjør71 * kjør12

print("Totalt trær", faktoravkjør)
