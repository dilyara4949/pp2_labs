n = int(input())
myDict = {
}

for i in range(n): # read the input
    stud, mon = map(str, input().split())
    if stud in myDict:  # check if key is alredy exist or not
        myDict[stud] += int(mon)
    else:
        myDict[stud] = int(mon)
listOfMon = list(myDict.values())
listOfMon.sort()

maxx = listOfMon[-1] # maximum compensation

listOfNames = list(myDict.keys())
listOfNames.sort()

for i in listOfNames: #printing by sorted dict
    if maxx - myDict[i] == 0:
        print(i, 'is lucky!')
    else:
        print(i, 'has to receive', maxx - myDict[i], 'tenge')
