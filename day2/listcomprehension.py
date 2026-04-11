nums = [1,2,3,4,5,6,7,8,9,10]

def squarelist(nums):
    sqlist = [i*i for i in nums]
    return sqlist

def oddnumlist(nums):
    oddlist = [i for i in nums if i%2!=0]
    return oddlist

print(squarelist(nums))

print(oddnumlist(nums))