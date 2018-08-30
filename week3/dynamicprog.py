def editDistance(x, y):
    # Create distance matrix
    D = []
    for i in range(len(x)+1):
        D.append([0]*(len(y)+1))
    # Initialize first row and column of matrix
    for i in range(len(x)+1):
        D[i][0] = i
    for i in range(len(y)+1):
        D[0][i] = 0
    # Fill in the rest of the matrix
    
    for i in range(1, len(x)+1):
        for j in range(1, len(y)+1):
            distHor = D[i][j-1] + 1
            distVer = D[i-1][j] + 1
            if x[i-1] == y[j-1]:
                distDiag = D[i-1][j-1]
            else:
                distDiag = D[i-1][j-1] + 1
            D[i][j] = min(distHor, distVer, distDiag)
    # Edit distance is the value in the bottom right corner of the matrix
    #print D
    minValue = 9999999999999
    for i in range(len(y)+1):
       if D[len(x)][i] < minValue:
           #print D[len(x)][i]
           minValue = D[len(x)][i]
    #print minValue
    #print min(D[:-1][-1])
    #print D[-1][:len(y)+1]
    return min(D[-1][:len(y)+1])

def overlap(a, b, min_length=3):
    """ Return length of longest suffix of 'a' matching
        a prefix of 'b' that is at least 'min_length'
        characters long.  If no such overlap exists,
        return 0. """
    start = 0  # start all the way at the left
    while True:
        start = a.find(b[:min_length], start)  # look for b's prefix in a
        if start == -1:  # no more occurrences to right
            return 0
        # found occurrence; check for full suffix/prefix match
        if b.startswith(a[start:]):
            return len(a)-start
        start += 1  # move just past previous match

def createKmerDictionary(sequences, kmer_length=6):
    kmerDictionary = {}
    for name in sequences.keys():
        seq = sequences.get(name)
        for i in range(len(seq)-kmer_length+1):
            kmer = seq[i:i+kmer_length]
            if kmer in kmerDictionary:
                kmerDictionary.get(kmer).add(name)
            else:
                a=set()
                a.add(name)
                kmerDictionary[kmer] = a
    
    return kmerDictionary


