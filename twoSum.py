def twoSum(nums, target):
    left = 0
    right = len(nums) - 1
    while left < right:
        summ = nums[left] + nums[right]
        if summ == target:
            return left, right
        elif summ < target:
            left += 1
        else:
            right -= 1
    return ()


mas = [3, 8, 9, 11, 16, 18, 19, 21]
print (twoSum(mas, 25))
