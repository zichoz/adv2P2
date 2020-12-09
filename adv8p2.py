import copy
class Accumulator:
    def __init__(self):
        self._accumulator = 0
    def acc(self, value):
        if value[0] == "+":
            value = value.lstrip("+")
            self._accumulator += int(value)
        if value[0] == "-":
            value = value.lstrip("-")
            self._accumulator -= int(value)



file = open("program.txt")
things = []
log = []

for line in file:
    line = line.replace("\n", "")
    line = line.split(" ")
    #print(line)
    things.append(line)


print(things)

#accum = Accumulator()

#print(accum._accumulator)
#ints = [2,3,4,5]
"""
for ints, code in enumerate(actions):
    print(code, ints)
    if code[0] == "acc":
        print("acc")
        log.append(actions.index(code))
        accum.acc(code[1])
    #print(val)
    #if code[0] == "jmp":

i = ""
"""
iterators = []
iterator = 0
i = 0
counter = 0
#print("før loop", actions[3])


def runThrough(actions):
    i= 0
    log = []
    accum = Accumulator()

    while not (i in log):
        #print(i)
        if i == 645:
            print("Endelig accumulator: ", accum._accumulator)
            return True
        #counter += 1
        #print(actions)
        #print(type(i))
        #print("accumulator", accum._accumulator, "i", i, log, "er dette", actions[i])
        # print(actions[i][0]
        # continue
        #print(actions[i][0])
        if actions[i][0] == "acc":
            #print("er acc", actions[i][1])
            log.append(i)
            # print(i, "test")
            accum.acc(actions[i][1])
            #print(accum._accumulator)
            #print("legger til i +1")
            i += 1
            continue
        if actions[i][0] == "jmp":
            #print("er jump", actions[i][1], " i ", i)
            derp = actions[i][1].split(" ")
            #print(derp, "derp")
            # print(actions[i][1][0][0]) #+ or -
            #print(actions[i][1][0][0], "skal være ++")
            if actions[i][1][0][0] == "+":
                #print(actions[i][1])
                #print(derp)
                derp = derp[0].lstrip("+")
                #print(derp, "++++")
                log.append(i)
                #print(i, "som blir lagt til i log")
                #print((int(actions[i][1])), "test")
              #  print("går i pluss")
               # print(i)
                i += int(derp)
                
                continue
            if actions[i][1][0][0] == "-":
                derp = actions[i][1].lstrip("-")
                #print(derp, "derpppp", actions[i][1])
                # print(i)
                log.append(i)
                i -= int(derp)
                #print("går i minus")
                #print(i)
                continue
        if actions[i][0] == "nop":
            #print("er nop", actions[i][1])
            log.append(i)
            i += 1
            continue


#runThrough(actions)

#print(runThrough(["23","23","2,3",",32"]))
#print(actions)


riktigListe =[]
huskeX = 0
for x in range(0,646):
    newlist = copy.deepcopy(things)
   # print("startet looop med x: ", x, (newlist[x]))
    #print(newlist)
    #print("gammel liste", things)
    if newlist[x][0] == "jmp":
        newlist[x][0] = "nop"
        if runThrough(newlist) == True:
            riktigListe = newlist
            huskeX = x

    #print("har loopet igjennom")

print("X", x, riktigListe)
#print(runThrough(actions))

riktigListe =[]
huskeX = 0
for x in range(0,646):
    newlist = copy.deepcopy(things)
    #print("startet looop med x: ", x, (newlist[x]))
    #print(newlist)
    #print("gammel liste", things)
    if newlist[x][0] == "nop":
        newlist[x][0] = "jmp"
        if runThrough(newlist) == True:
            riktigListe = newlist
            huskeX = x

    #print("har loopet igjennom")

print("X", x, riktigListe)
#print(runThrough(actions))

"""
riktigListe =[]
huskeX = 0
for x in range(646):
    print(x)
    newlist = actions
    print("startet looop med x: ", x, (newlist[x]))
    if newlist[x][0] == "nop":
        newlist[x][0] = "jmp"
        if runThrough(newlist) == True:
            riktigListe = newlist

print(riktigListe)
"""
