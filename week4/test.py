import utilities
import dnafunctions
import collections

strings1 = ['ABC', 'BCA', 'CAB']
strings2 = ['CCT', 'CTT', 'TGC', 'TGG', 'GAT', 'ATT']
strings3 = ['CAGTFGSFHAGHGDSD','CAGTFGSFHAGHGDSD','CAGTFGSFHAJJJJJJJJGHGDSD', 'GCATGHJHDJHDGADGFDGSGDHHSG', 'TAGHJGJDHJTTHJGJGJSGGHGDJ', 'GATTGHJJGJSGJGDSHJGHD', 'CGHJHJSCGHHKD', 'GGGCHGJSJFJGSG']

sequences,readDic = dnafunctions.readFastq('ads1_week4_reads.fq')



#sequences = strings3
# scs,st =  utilities.scs(sequences)
# print scs
# print 'Length of genome ' + str(len(scs))


print len(sequences)

a = set()
for s in sequences:
     a.add(s)
k=30
# #overlapsDic =  utilities.computeOverlaps(sequences,k)
# #print utilities.pickMaxOverlap(overlapsDic,k)

 
# #print len(a)
# #sequences.find('CTGAGCTTGACATAGTTGTTAGACGTACAGCAGGGCTCAATGAAAAACTGGTGTTCTACAACAACACCCCACTAACCCTCCTCACACCTTGGAGAAAGGT')
smallestgenome  = utilities.greedyScs(list(a),k)
for k in range(30,29,-1):
    genome = utilities.greedyScs(list(a),k)
    if len(genome) < len(smallestgenome):
        smallestgenome = genome
    print 'Loop ' + str(k)
    print 'Lenth of genome ' + str(len(genome))
    

d = collections.defaultdict(int)
print 'Final Result'

print 'Smallest Genome length ' + str(len(smallestgenome))
for c in smallestgenome:
    d[c] += 1
print d