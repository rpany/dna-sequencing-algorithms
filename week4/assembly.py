import dnafunctions
import dynamicprog
import utilities
import dnafunctions


sequences,readDic = dnafunctions.readFastq('ads1_week4_reads.fq')


kmer = 30

kmerDic = dynamicprog.createKmerDictionary(readDic,kmer)
print len(kmerDic)
overlapPairs=[]
for name in readDic.keys():
    #print name
    seq = readDic.get(name)
    #print seq
    km = seq[-kmer:]
    #print km    
    sequenceSet = kmerDic.get(km)
    #print sequenceSet
    for s in sequenceSet:
        if name!=s:
            if dynamicprog.overlap(readDic.get(name),readDic.get(s),kmer) != 0:
                t=name,s
                overlapPairs.append(t)

#print len(overlapPairs)
print overlapPairs

outgoingnodes = set()
for o in overlapPairs:
    a,b= o
    outgoingnodes.add(a)
#    print readDic.get(a)[-kmer:] + ' ---- ' + readDic.get(b)[0:kmer]

print len (outgoingnodes)





# sequences,readDic = dnafunctions.readFastq('ads1_week4_reads.fq')

# print len(sequences)

# print len(utilities.greedyScs(sequences,kmer))

