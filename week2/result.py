import dnafunctions
import boyermoore
import bm_preproc
import kmer_index







t= dnafunctions.readFasta('chr1.GRCh38.excerpt.fasta').values()[0]
p='GGCGCGGTGGCTCACGCCTGTAAT'

# p = 'needle'
# t = 'needle need noodle needle'
# lowercase_alphabet = 'abcdefghijklmnopqrstuvwxyz '
# #t='ATG'
# #p='ATG'
#print 'Naive ---------- ' + str(dnafunct

Ind = kmer_index.Index(t,8)

hits= Ind.query(p)
print len(sorted(hits))
print dnafunctions.naive_2mm(p,t)
#print dnafunctions.naive(t,p)



#print 'Boyer Moore ---- ' + str(boyermoore.boyer_moore(p,bm,t))