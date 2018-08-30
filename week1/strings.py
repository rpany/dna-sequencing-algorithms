def stringMatch(s1,s2):
    if s1==s2:
        return True
    else:
        return False

def reverseComplement(s1):
    lookup={'A':'T', 'C':'G', 'G':'C','T':'A'}
    reverse=''
    for i in range(len(s1)):
        reverse =lookup[s1[i]]+reverse
    return reverse

#print stringMatch('AAAA', 'AAAC')

print reverseComplement('ACGT')