nums = [1, 2, 3, 4]
left = 0
right = len(nums) - 1
while left < right:
    temp = nums[left]
    nums[left] = nums[right]
    nums[right] = temp
    left+=1
    right-=1

print(nums)