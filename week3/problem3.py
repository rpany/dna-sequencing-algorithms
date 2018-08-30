import dnafunctions
import dynamicprog


sequences,readDic = dnafunctions.readFastq('ERR266411_1.for_asm.fastq')

#print readDic.keys()
kmer = 30
# readDic = {}
# # sequences = {}
# readDic[1] = 'ABCDEFG'
# readDic[2]= 'EFGHIJ'
# readDic[3]= 'HIJABC'

#readDic = {1:'CGTACG',2: 'TACGTA', 3:'GTACGT', 4:'ACGTAC', 5:'GTACGA', 6:'TACGAT'}



# print kmerDic


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

print len(overlapPairs)
#print overlapPairs

outgoingnodes = set()
for o in overlapPairs:
    a,b= o
    outgoingnodes.add(a)
#    print readDic.get(a)[-kmer:] + ' ---- ' + readDic.get(b)[0:kmer]

print len (outgoingnodes)

