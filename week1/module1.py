import dnafunctions
import matplotlib.pyplot as plt

p ='AGGAGGTT'
sequence = dnafunctions.readGenome('lambda_virus.fa')
#sequence = 'ACTTACTTGATAAAGT'

seq,qual = dnafunctions.readFastq('ERR037900_1.first1000.fastq')

hist = dnafunctions.createHist(qual)
print hist

plt.bar(range(len(hist)),hist)
plt.show()


