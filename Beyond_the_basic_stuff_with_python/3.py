import copy
arr = ['a','b','c','A','Z']

sr = "aeiou"
print(sum(1 if x in "aeiou" else 0 for x in sr))

arr_copy = copy.copy(arr)
arr_copy.sort(key=str.upper)
print('\t'.join(arr))

print(isinstance(1,int))
print(4 * True/2)