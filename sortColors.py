def sortColors(nums):
    left, mid, right = 0, 0, len(nums) - 1
    while mid <= right:
        if nums[mid] == 2:
            nums[mid], nums[right] = nums[right], nums[mid]
            right -= 1
        elif nums[mid] == 0:
            nums[mid], nums[left] = nums[left], nums[mid]
            mid += 1
            left += 1
        elif nums[mid] == 1:
            mid += 1


mas = [2, 0, 1, 0, 0, 1, 2]
sortColors(mas)
print(mas)
