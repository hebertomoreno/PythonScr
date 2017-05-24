from collections import Counter
def areSimilar(A, B):
	return sorted(A) == sorted(B) and sum(a != b for a, b in zip(A, B)) < 3

print(areSimilar([1,1,3],[3,1,1]))
print(areSimilar([1,1,3],[1,3,1]))
print(areSimilar([4,3,2,1],[1,2,3,4]))
print(areSimilar([1,1,1,1,1,1,1,1,1,1,5],[5,1,1,1,1,1,1,1,1,1,1]))
print(areSimilar([1,2,3,3,3,3,5,5,5,3,5],[1,2,3,5,3,3,5,3,5,3,5]))
print(areSimilar([1,1,2],[2,1,2]))