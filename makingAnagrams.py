'''Counter is a dict subclass for counting hashable objects. It is an unordered collection where
elements are stored as dictionary keys and their counts are stored as dictionary vallues. Counts
are allowed to be any integer value including zero or negative counts. '''
from collections import Counter
def number_needed(a, b):
	#Returns the letters in a along with their count. 
    ct_a = Counter(a)
    print(ct_a)
    #Same for b
    ct_b = Counter(b)
    print(ct_b)
    #substract the counters of the elements in b from the elements in a. Any value that is
    #different than zero in the resulting dict is not 
    ct_a.subtract(ct_b)
    print(ct_a)
    return sum(abs(i) for i in ct_a.values())

word1 = input()
word2 = input()

print(number_needed(word1, word2))