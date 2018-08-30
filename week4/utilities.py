import time
from random import randint

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's suffx in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

import itertools

def scs(ss):
    """ Returns shortest common superstring of given
        strings, which must be the same length """
    shortest_strings=[]
    
    shortest_sup = None
    permutation = 0
    for ssperm in itertools.permutations(ss):
        permutation+=1
        #print permutation
        sup = ssperm[0]  # superstring starts as first string
        for i in range(len(ss)-1):
            # overlap adjacent strings A and B in the permutation
            olen = overlap(ssperm[i], ssperm[i+1], min_length=1)
            # add non-overlapping portion of B to superstring
            sup += ssperm[i+1][olen:]
      
        if shortest_sup is None or len(sup) <= len(shortest_sup):
            shortest_sup = sup  # found shorter superstring
            #print len(sup)
            shortest_strings.append(sup)

        for string in shortest_strings:
            if len(string) > len(shortest_sup):
                shortest_strings.remove(string)

    return shortest_sup, shortest_strings   # return shortest



def pickMaximalOverlap(reads, k):
    reada,readb = None, None
    olenMax=0
    for a,b in itertools.permutations(reads,2):
        olen = overlap(a,b,min_length=k)    
        if olen > olenMax :
            reada,readb = a,b
            olenMax = olen
        
    return reada,readb,olenMax

def computeOverlaps(reads, k):
    overlapsDictionary={}
    for a,b in itertools.permutations(reads,2):
        olen = overlap(a,b,k)
        if olen > 0:
            if olen in overlapsDictionary:
                t = (a,b)
                overlapsDictionary.get(olen).add(t)
            else:
                s = set()
                t = (a,b)
                s.add(t)
                overlapsDictionary[olen] = s

    return overlapsDictionary

def addNewOverlap(overlapsDictionary, newRead, oldRead1, oldRead2, reads, k):
    reads.remove(oldRead1)
    reads.remove(oldRead2)
    for read in reads:
        olen1 = overlap(newRead, read, k)
        olen2 = overlap(read, newRead, k)
        if olen1 > 0:
            if olen1 in overlapsDictionary:
                t = (newRead,read)
                overlapsDictionary.get(olen1).add(t)
            else:
                s = set()
                t = (newRead,read)
                s.add(t)
                overlapsDictionary[olen1] = s
        if olen2 > 0:
            if olen2 in overlapsDictionary:
                t = (read,newRead)
                overlapsDictionary.get(olen2).add(t)
            else:
                s = set()
                t = (read,newRead)
                s.add(t)
                overlapsDictionary[olen2] = s

    reads.append(newRead)
    for key in overlapsDictionary.keys():
        removelist=[]
        for value in overlapsDictionary.get(key):
            a,b = value
            if a == oldRead1 or a == oldRead2 or b == oldRead1 or b == oldRead2 :
                removelist.append(value)
        for item in removelist:
            overlapsDictionary.get(key).remove(item)

    return overlapsDictionary,reads

def pickMaxOverlap(overlapsDictionary, k):
    olen = 0
    reada,readb=None,None
    for key in overlapsDictionary.keys():
        if key > olen and len(overlapsDictionary.get(key)) > 0:
            olen = key
    return olen

def greedyScs(reads, k):
    overlapsDictionary = computeOverlaps(reads, k)
    #print 'computeOverlaps'
    olen = pickMaxOverlap(overlapsDictionary,k)
    #print 'initial olen ' + str(olen)
    #print 'pickmaxoverlap'
    loop = 0
    while olen > 0 :
            #reada,readb = overlapsDictionary.get(olen).pop()
            newset,selectedread = popRandom(overlapsDictionary.get(olen))
            reada,readb = selectedread
            overlapsDictionary[olen]=newset
            newRead = reada + readb[olen:]
            overlapsDictionary, reads = addNewOverlap(overlapsDictionary, newRead, reada, readb, reads, k)    
            olen = pickMaxOverlap(overlapsDictionary,k)
            loop+=1
            #print reada
            #print readb
            #print olen
            #print loop
            #print reads     

    return ''.join(reads)

def popRandom(readSet):
    #print 'old set ' + str(len(readSet))
    setlen = len(readSet)  
    rand = randint(0,setlen)
    a = set()
    for i in range(rand-1):
        a.add(readSet.pop())
    
    selectedread = readSet.pop()

    newset = readSet.union(a)
    
    #print 'new set ' + str(len(newset))
    return newset, selectedread