import dnafunctions
import dynamicprog

t = dnafunctions.readGenome('chr1.GRCh38.excerpt.fasta')

p ='GCTGATCGATCGTACG'
#t ='TATTGCGTATGCGTT'
#p ='GCGTT'

#p ='AGT'
#t ='AGC'

print dynamicprog.editDistance(p,t)
