a=(1,2,3,4,5,6,6,7,7,8,9,9,0,2,34,1,1,)
max=max(a)
indexmax=a.index(max)
min=min(a)
indexmin=a.index(min)
sum=sum(a)
# a.reverse()
# print(a)        it cannot be reversed as it is immutable
# a.sort()        same for sort it cannot be sorted
print(indexmax,max)
print(indexmin,min)
print(sum)
print(a)
