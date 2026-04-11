def mysum(numlist):
    total = 0
    for i in numlist :
        if i%2 == 0 and i >=0 :
            total += i
    return total

nums = [1,2,3,4,5]

print(mysum(nums))