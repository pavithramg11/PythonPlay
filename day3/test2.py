nums = [1,2,3,4,5, 6,7,8,10,9]

def findsum(nums):
    sum = 0
    for num in nums:
        sum+=num
    return sum

print(findsum(nums))

def greater(nums):
    return [num for num in nums if num > 5 ]

print(greater(nums))

def squares(nums):
    sqlist = [num**2 for num in nums]
    return sqlist

print(squares(nums))

def evennum(nums):
    return [ num for num in nums if num%2 == 0]

print(evennum(nums))

def oddnum(nums):
    return [ num for num in nums if num%2 != 0]

print(oddnum(nums))

print(squares(evennum(nums)))

def findmax(nums):
    max = nums[0]
    for num in nums:
        if num > max:
            max = num
    return max

print(findmax(nums))