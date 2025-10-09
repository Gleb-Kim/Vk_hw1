def sortBinaryArrayVer1(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 0:
             left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[right] = 1
            arr[left] = 0
            left += 1
            right -= 1

def sortBinaryArrayVer2(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] == 1:
            arr[right], arr[left] = arr[left], arr[right]
            right -= 1
        else:
            left += 1


mas1 = [0, 1, 1, 0, 1, 0, 1, 0]
print(mas1)
sortBinaryArrayVer1(mas1)
print(mas1, '\n')
mas2 = [1, 1, 1, 0, 1, 0, 1, 0]
print(mas2)
sortBinaryArrayVer1(mas2)
print(mas2)
