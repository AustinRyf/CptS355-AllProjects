#Austin Ryf - 11512650
#Intended for Windows

import random

debugging = True
def debug(*s): 
    if debugging: print(*s)

#---------------------------------------------------------------------------------------
#map & reduce
def map(f,alist):
    answer = []
    for v in alist:
        answer.append(f(v))
    return answer

def reduce(f,alist):
    if alist == []:
        return None

    answer = alist[0]
    for v in alist[1:]:
        answer = f(answer,v)
    return answer 

#---------------------------------------------------------------------------------------
#addDict

studyDict = {'355':{'Mon':3,'Wed':2,'Sat':2},
            '360':{'Mon':3,'Tue':2,'Wed':2,'Fri':10},
            '321':{'Tue':2,'Wed':2,'Thu':3},
            '322':{'Tue':1,'Thu':5,'Sat':2}}

def addDict(d):
    hoursDict = {}
    for classNum in d:
        currentClassNum = d[classNum] #grabs the classNum we are currently on
        for day in currentClassNum:
            if day in hoursDict.keys():
                hoursDict[day] += currentClassNum[day] #if the day is already in the list, we add the hours to it
            else:
                hoursDict[day] = currentClassNum[day] # otherwise it adds it to the list
    return hoursDict

#---------------------------------------------------------------------------------------
#addDictN

def reduceFunc(L, d):
    for day in L:
        if day in d.keys():
            d[day] += L[day] #if the day is already present this will add the hours to it
        else:
            d[day] = L[day] #otherwise it adds it to the list
    return d

def addDictN(L):
    if L == {}:
        return {}
    hoursDict = {}
    dictList = list(map(addDict, L)) #maps the addDict function to all the dictionaries in the list so that we can have a list of days
    hoursDict = reduce(reduceFunc, dictList) #reduces all the days into a single list of days
    return hoursDict

#---------------------------------------------------------------------------------------
#lookupVal

L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]

def lookupVal(L,k):
    for d in reversed(L1):
        for key in d:
            if key == k:
                return d[key] #if the key is the one we want, return its value

#---------------------------------------------------------------------------------------
#lookupVal2

L2 = [(0,{"x":0,"y":True,"z":"zero"}),
    (0,{"x":1}),
    (1,{"y":False}),
    (1,{"x":3, "z":"three"}),
    (2,{})]

def indexHelper(i, tL, k):
    if k in tL[i][1]:
        return tL[i][1][k] #if the key we want is in our current tuple dictionary return its value
    elif i != 0:
        i = tL[i][0]
        return indexHelper(i, tL, k) #if we are not on the first tuple of the list, recursively call the function
    elif i == 0:
        if k in tL[i][1]:
            return tL[i][1][k] #if we are on the the first tuple of the list, either return the value (if the key is present), or return None
        else:
            return None
    else:
        return None #if all else fails return None
    
def lookupVal2(tL,k):
    index = -1 #start at the back of the list
    return indexHelper(index, tL, k)

#---------------------------------------------------------------------------------------
#numPaths

def positionIsBlocked(position, blocks):
    if (position[0] > 0 and position[1] > 0):
        if not position in blocks:
            return True #if the position is not blocked and it is not outside of the grid return True
    else:
        return False #otherwise return false

def numPaths(m,n, blocks):
    position = (m,n) #sets the position
    paths = 0 #keeps track of path numbers
    if positionIsBlocked((position[0]-1 , position[1]), blocks):
        paths += numPaths(position[0]-1, position[1], blocks) #if this passes the positionIsBlocked condition with the new position, recursively call with adjusted m
    if positionIsBlocked((position[0] , position[1]-1), blocks):
        paths += numPaths(position[0], position[1]-1, blocks) ##if this passes the positionIsBlocked condition with the new position, recursively call with adjusted n
    if position == (1,1):
        return 1 #if we reach the finish return 1 for paths
    return paths #return number of paths

#---------------------------------------------------------------------------------------
#palindromes

def palindromes(S):
    palList = []
    currLeft = 0
    while (currLeft < len(S)):
        currRight = -1
        while currLeft < (len(S) + currRight):
            if currRight == -1:
                Slice = S[currLeft:] #sets current slice
                reversedSlice = ''.join(reversed(Slice)) #sets current reversed slice
            else:
                Slice = S[currLeft:(currRight + 1)] #sets current slice
                reversedSlice = ''.join(reversed(Slice)) #sets current reversed slice
            if Slice == reversedSlice:
                if Slice in palList:
                    break #if the palindrome is already in the list, do not enter it again
                else:
                    palList.append(Slice) #otherwise put it in the list
            currRight = currRight - 1 #increment right
        currLeft = currLeft + 1 #increment left
    palList = sorted(palList) #sort the list
    return palList #return the list of palindromes

#---------------------------------------------------------------------------------------
#iterApply
class iterApply():
    def __init__(self, n, f):
        self.integer = n #set integer
        self.function = f #set function
        self.currNum = 0 #create currNum tracker
    
    def __next__(self): 
        self.currNum = self.function(self.integer) #apply the function to the integer
        self.integer += 1 #increment integer
        return self.currNum #return the current number

squares = iterApply(1,lambda x: x**2)
triples = iterApply(1,lambda x: x**3)

#---------------------------------------------------------------------------------------
#iMerge
def iMerge(iNumbers1, iNumbers2, N):
    i = 0
    mergeList = []
    while (i < N/2):
        mergeList.append(iNumbers1.__next__()) #insert one iteration of iNumbers1
        mergeList.append(iNumbers2.__next__()) #insert one iteration of iNumbers2
        i += 1 #increment
    mergeList = sorted(mergeList) #sort the list
    return mergeList #return the list

        
#---------------------------------------------------------------------------------------
#streamRandom

class Stream(object): #given Stream class
    def __init__(self, first, compute_rest, empty= False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False

    @property
    def rest(self):
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest

def streamRandoms(k, min, max):
    def compute_rest():
        return streamRandoms(random.randint(min, max), min, max) #return created random int for rest and pass on min and max
    return Stream(k, compute_rest)

""" rStream = streamRandoms(1,1,100)
myList = []
for i in range (0,10):
    myList.append(rStream.first)
    rStream = rStream.rest
print(myList) """

#---------------------------------------------------------------------------------------
#oddStream
def oddStream(stream):
    def compute_rest():
        return oddStream(stream.rest) #return rest
    if (stream.first % 2 != 0):
        return Stream(stream.first, compute_rest) #if the current integer is odd return it
    else:
        return oddStream(stream.rest) #if it's odd call the function without returning the number

""" oddS = oddStream(streamRandoms(1,1,100))
myList2 = []
for i in range(0,100):
    myList2.append(oddS.first)
    oddS = oddS.rest
print(myList2) """

#---------------------------------------------------------------------------------------
#tests and main

def testaddDict():
    d = {'355':{'Mon':3,'Wed':2,'Sat':2},'360':{'Mon':3,'Tue':2,'Wed':2,'Fri':10},
        '321':{'Tue':2,'Wed':2,'Thu':3},'322':{'Tue':1,'Thu':5,'Sat':2}}

    d2 = {'355':{'Mon':1,'Wed':1,'Sat':1},'360':{'Mon':1,'Tue':1,'Wed':1,'Fri':1},
        '321':{'Tue':1,'Wed':1,'Thu':1},'322':{'Tue':1,'Thu':1,'Sat':1}}

    if addDict({}) != {}:
        return False
    if dict(sorted(list(addDict(d).items()))) != {'Fri': 10, 'Mon': 6, 'Sat': 4,
        'Thu': 8, 'Tue': 5, 'Wed': 6}:
        return False
    if dict(sorted(list(addDict(d2).items()))) != {'Fri': 1, 'Mon': 2, 'Sat': 2,
        'Thu': 2, 'Tue': 3, 'Wed': 3}:
        return False
    return True

def testaddDictN():
    d = [{'355':{'Mon':3,'Wed':2,'Sat':2},'360':{'Mon':3,'Tue':2,'Wed':2,'Fri':
        10},'321':{'Tue':2,'Wed':2,'Thu':3},'322':{'Tue':1,'Thu':5,'Sat':2}},
        {'322':{'Mon':2},'360':{'Thu':2, 'Fri':5},'321':{'Mon':1, 'Sat':3}},
        {'355':{'Sun':8},'360':{'Fri':5},'321':{'Mon':4},'322':{'Sat':3}}]

    d2 = [{'355':{'Mon':1,'Wed':1,'Sat':1},'360':{'Mon':1,'Tue':1,'Wed':1,'Fri':
        1},'321':{'Tue':1,'Wed':1,'Thu':1},'322':{'Tue':1,'Thu':1,'Sat':1}},
        {'322':{'Mon':1},'360':{'Thu':1, 'Fri':1},'321':{'Mon':1, 'Sat':1}}]

    if addDictN({}) != {}:
        return False
    if dict(sorted(list(addDictN(d).items()))) != {'Fri': 20,'Mon': 13,'Sat': 10,
        'Sun': 8, 'Thu': 10, 'Tue': 5, 'Wed': 6}:
        return False
    if dict(sorted(list(addDictN(d2).items()))) != {'Fri': 2,'Mon': 4,'Sat': 3,
        'Thu': 3, 'Tue': 3, 'Wed': 3}:
        return False
    return True

def testlookupVal():
    L1 = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]

    if lookupVal(L1,"x") != 2:
        return False
    if lookupVal(L1,"y") != False:
        return False
    if lookupVal(L1,"z") != "found":
        return False
    if lookupVal(L1,"t") != None:
        return False
    return True

def testlookupVal2():
    L2 = [(0,{"x":0,"y":True,"z":"zero"}),
        (0,{"x":1}),
        (1,{"y":False}),
        (1,{"x":3, "z":"three"}),
        (2,{})]

    if lookupVal2(L2,"x") != 1:
        return False
    if lookupVal2(L2,"y") != False:
        return False
    if lookupVal2(L2,"z") != "zero":
        return False
    if lookupVal2(L2,"t") != None:
        return False
    return True

def testnumPaths():
    if numPaths(2,2,[(2,1)]) != 1:
        return False
    if numPaths(3,3,[(2,3)]) != 3:
        return False
    if numPaths(4,3,[(2,2)]) != 4:
        return False
    if numPaths(10,3,[(2,2),(7,1)]) != 27:
        return False
    return True

def testpalindromes():
    if palindromes('cabbbaccab') != ['abbba', 'acca', 'baccab', 'bb', 'bbb', 
        'cabbbac', 'cc']:
        return False
    if palindromes(' bacdcabdbacdc') != ['abdba', 'acdca', 'bacdcab', 'bdb', 
        'cabdbac', 'cdc', 'cdcabdbacdc', 'dcabdbacd']:
        return False
    if palindromes(' myracecars') != ['aceca', 'cec', 'racecar']:
        return False
    return True

#main
if __name__ == '__main__':
    passedMsg = "%s passed"
    failedMsg = "%s failed"
    if testaddDict():
        print(passedMsg % 'addDict')
    else:
        print(failedMsg % 'addDict')
        
    if testaddDictN():
        print(passedMsg % 'addDictN')
    else:
        print(failedMsg % 'addDictN')

    if testlookupVal():
        print(passedMsg % 'lookupVal')
    else:
        print(failedMsg % 'lookupVal')

    if testlookupVal2():
        print(passedMsg % 'lookupVal2')
    else:
        print(failedMsg % 'lookupVal2')

    if testnumPaths():
        print(passedMsg % 'testnumPaths')
    else:
        print(failedMsg % 'testnumPaths')

    if testpalindromes():
        print(passedMsg % 'palindromes')
    else:
        print(failedMsg % 'palindromes')