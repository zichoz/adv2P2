class PassPort:
    def __init__(self, list):
        self._informasjon = list
        self._byr = None # tatt
        self._iyr = None # tatt
        self._eyr = None# tatt
        self._hgt = None# tatt
        self._hcl = None # tatt
        self._ecl = None # tatt
        self._pid = None # tatt
        self._cid = None # tatt

    def leggTilInfomrmasjonIpass(self):
        for info in self._informasjon:
            #print(info.split(":"))
            info = info.split(":")
            if info[0] == "byr": #kontrollert
                if int(info[1]) >= 1920 and int(info[1]) <= 2020 and len(info[1]) == 4:
                    self._byr = int(info[1])

            elif info[0] == "iyr": #kontrolert
                if int(info[1]) >= 2010 and int(info[1]) <= 2020:
                    self._iyr = int(info[1])#fiksa
                    #print(self._iyr)
            elif info[0] == "eyr":
                if int(info[1]) >= 2010 and int(info[1]) <= 2030 and len(info[1]) == 4:
                    self._eyr = int(info[1]) #fiksa
                    #print(self._eyr)
            elif info[0] == "hgt":
                if "cm" in info[1]:
                    #print(info[1])
                    info[1] = int(info[1].replace("cm",""))
                    #print(info[1])
                    if info[1] >=150 and info[1] <=193:
                        self._hgt = info[1]
                elif "in" in info[1]:
                    info[1] = int(info[1].replace("in", ""))
                    if info[1] >= 59 and info[1] <= 76:
                        #print(type(info[1]))
                        self._hgt = info[1]
                        #print(self._hgt)
            elif info[0] == "hcl":
                #print(info[1])
                hcl = info[1]
                if hcl[0] == "#":
                    #print("#")
                    info[1] = info[1].replace("#", "")
                    hcl = hcl.replace("#", "")
                    if len(info[1]) == 6:
                        test = True
                        for x in hcl:
                            #print(x)
                            if x not in ["a", "b", "c", "d", "e", "f", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]:
                                print(x)
                                test = False
                        if test == True:
                            self._hcl = info[1]
                            #print(self._hcl)
            elif info[0] == "ecl":
                #print(info[0], info[1])
                if info[1] == "amb" or info[1] == "blu" or info[1] == "brn" or info[1] == "gry" or info[1] == "grn" or info[1] == "hzl" or info[1] == "oth":
                    self._ecl = info[1]
                    #print(self._ecl)
            elif info[0] == "pid":
                #print(info[1])
                #info[1] = info[1].lstrip("0")
                #print(info[1])
                testNot = True
                for x in info[1]:
                    print(x)
                    if x not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                        testNot = False
                if len(info[1]) == 9 and (testNot == True):
                    self._pid = int(info[1])
            elif info[0] == "cid":
                self._cid = info[1]




file = open("passports.txt")

passord = []
teller=0
batch = []
passObjekter = []
validPassobjekter = []
print("start")
counter = 0
for line in file: #sortere inn batchvis i en nøstet liste
    line = line.replace("\n", "")

    if line == "":
        passord.append(batch)
        print(batch)
        batch = []
        print("\n")
        counter +=1
        continue
    batch.append(line)
    #print(line)
   # #print(line)


for i in passord:
    #print(passord.index(i))
    #print(i)
    #x = ""
    passord[passord.index(i)] = (" ".join(i)) #fikser så hvert element i listen inneholder en batch
   # print(passord[passord.index(i)])

print(passord[0])

for i in passord:
    #print(i.split(" "))
    passord[passord.index(i)] = i.split(" ")


for i in passord:
    nyttPassObjekt = PassPort(i)
    nyttPassObjekt.leggTilInfomrmasjonIpass()
    passObjekter.append(nyttPassObjekt)

teller = 0
for o in passObjekter:
    teller +=1
    #print(o._pid)
   # print(o)
    if (o._byr != None) and (o._iyr != None) and (o._eyr != None) and (o._hgt != None) and (o._hcl != None) and (o._ecl != None) and (o._pid != None) and (o._cid != None):
        validPassobjekter.append(o)
    elif (o._byr != None) and (o._iyr != None) and (o._eyr != None) and (o._hgt != None) and (o._hcl != None) and (o._ecl != None) and (o._pid != None) and (o._cid == None):
        validPassobjekter.append(o)
        #print("mangler cid men godkjennes")


print("Antall godkjente prosjekter", len(validPassobjekter))

print("antall passord totalt", len(passord))
print(teller)

print(counter)


int
