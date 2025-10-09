def reverseArray(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


mas = [3, 8, 6, 9, 9, 8, 6]
print(mas)
reverseArray(mas)
print(mas)
