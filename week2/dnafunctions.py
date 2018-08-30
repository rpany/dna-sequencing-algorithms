def phred33ToQ(q):
    return ord(q)-33

def createHist(qualities):
    hist = []
    for j in range(len(qualities[0])):
        hist.append(0)

    for qual in qualities:
        i=0
        for phred in qual:
            q = phred33ToQ(phred)
            hist[i]+=q
            i+=1
    return hist

def naive(p, t):
    totalpatterns=[p]
  #  if reverseComplement(p) != p:
   #     totalpatterns.append(reverseComplement(p))

    occurrences = []
    numOfAlignments=0
    numOfComparisons=0
    for pat in totalpatterns:
        for i in range(len(t) - len(pat) + 1):  # loop over alignments
            numOfAlignments+=1
            match = True
            for j in range(len(pat)):  # loop over characters
                numOfComparisons+=1
                if t[i+j] != pat[j]:  # compare characters
                    match = False
                    break
            if match:
                occurrences.append(i)  # all chars matched; record
    return occurrences,numOfAlignments,numOfComparisons


def naive_2mm(p, t):
    occurrences = []
    for i in range(len(t) - len(p) + 1):  # loop over alignments
        match = True
        noOfMimatches = 0
        for j in range(len(p)):  # loop over characters
            if t[i+j] != p[j]:  # compare characters
                noOfMimatches+=1
                if noOfMimatches>2:
                    match = False
                    break
        if match:
                occurrences.append(i)  # all chars matched; record
    return occurrences

def reverseComplement(s):
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'N': 'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t

def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.rstrip()
    return genome


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()  # skip name line
            seq = fh.readline().rstrip()  # read base sequence
            fh.readline()  # skip placeholder line
            qual = fh.readline().rstrip() # base quality line
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

def readFasta(filename):
    try:
        file1 = open(filename,"r")
    except IOError:
        print('unable to open file ' + filename)

    seqs={}
    count =0
    for line in file1:
        line = line.rstrip() 
        if line[0] == '>':
            words=line.split()
            name = words[0][1:]
            seqs[name]=''
        else:
            seqs[name]=seqs[name]+line

    file1.close()
    return seqs

