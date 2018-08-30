#!/usr/bin/env python

"""kmer_index.py: A k-mer index for indexing a text."""

__author__ = "Ben Langmead"

import bisect


class Index(object):
    """ Holds a substring index for a text T """

    def __init__(self, t, k):
        """ Create index from all substrings of t of length k """
        self.k = k  # k-mer length (k)
        self.index = []
        self.t = t
        for i in range(len(t) - k + 1):  # for each k-mer
            self.index.append((t[i:i+k], i))  # add (k-mer, offset) pair
        self.index.sort()  # alphabetize by k-mer

    def query(self, p):
        """ Return index hits for first k-mer of p """
        #kmerList = [p[:self.k], p[self.k:2*self.k], p[2*self.k:]]
        #print kmerList
        #  # query with first k-mer
        hits = set()
        indexhits=[]
        for l in range(3):
            start = l*self.k
            end = l*self.k+self.k
            
            kmer = p[start:end]
            print 'kmer = ' + kmer
            i = bisect.bisect_left(self.index, (kmer, -1))  # binary search
        
            while i < len(self.index):  # collect matching index entries
                if self.index[i][0] != kmer:
                    break
                index  = self.index[i][1]
                indexhits.append(index-start)
                mismatches =0
                for j in range(len(p)): 
                    #if j < start or index-start+len(p)> len(self.t):
                     #   break
                    if p[j] != self.t[index-start+j]:
                        mismatches+=1
                    if mismatches > 2:
                        break
                if mismatches <= 2 :
                    print self.t[index-start:index-start + len(p)]
                    hits.add(index-start)
                    
                i += 1
            
        return indexhits


    def approximateMacthes(self,t,p,kmer, hits, maxMismatches):
        matched =[]
        for hit in hits:
            match=True
            mismatches=0
            for i in range(len(p)-1):
                if t[hit+i] != p[i]:
                    mismatches=mismatches+1
                if mismatches > maxMismatches:
                    match=False
                    break
            if match:
                matched.append(hit)
        return matched