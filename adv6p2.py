file = open("questions.txt")
batch = []
nestedList = []
import pandas as pa

counterOfPassangersWho =0
def findCommon(list, amount):
    if len(list) == 1: #check if it is only one passanger
        print("len= 1", len(list[0]))
        return len(list[0])
    letters = ""
    lettersLst = []
    commons = []
    counter = 0
    #print()
    everyoneCommons = 0
    #print(letter)
    for x in list:
        #print(x)
        letters += x
        lettersLst.append(letters)
    #print(letters)
    #print(letters)
    print(letters)
    for l in letters: #finn de som er tilfeldig
        print(letters.count(l), l, "amount", amount)
        if letters.count(l) == amount:
            print("Det er like mange osm det er passasjer")
            counter += 1
            letters = letters.replace(l,"")
    print("finished", counter)
    return counter



for line in file:
    line = line.replace("\n", "")
    # print(line)
    batch.append(line)
    if line.strip() == "" :
        #print(line)or line == line[len(line)-1]

        #print("er ny barch")
        #print(batch)
        #batch.pop(line.index((len(line)-1)))
        batch.pop(len(line)-1)
        nestedList.append(batch)
        batch = []
        continue

    #print(batch)
print(nestedList)


    #f line.strip() == "":
     #   #print("er ny barch")
      #  nestedList.append(batch)
       # batch = []


#print(nestedList)
differentQuestions = []
differentQuestionsNr = 0
#print(nestedList)
for group in nestedList:
    #print(group)
    amountOfPeopleinGroup = 0
    for passanger in group:
        #print(passanger)
        amountOfPeopleinGroup +=1
        for letter in passanger:
            if passanger.index(letter) == 0:
                differentQuestions.append(letter)
            if letter in differentQuestions:
                differentQuestions.append(letter)
    differentQuestionsNr += len(differentQuestions)
    differentQuestions = []
    #print((group))
    #print(amountOfPeopleinGroup)
    #print(set.intersection(set(group)))
    counterOfPassangersWho += findCommon(group, amountOfPeopleinGroup)
    amountOfPeopleinGroup = 0
#print(differentQuestions)

print("passasjertotalt ", counterOfPassangersWho)
