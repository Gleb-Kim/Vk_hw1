def reverseArrayLR(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def reversePartOfArray(arr, k):
    n = len(arr)
    if n == 0:
        return
    rem = k % n
    if rem == 0:
        return
    reverseArrayLR(arr, 0, n - 1)
    reverseArrayLR(arr, 0, rem - 1)
    reverseArrayLR(arr, rem, n - 1)


mas = [1, 2, 3, 4, 5, 6, 7]
print(mas)
reversePartOfArray(mas, 7)
print(mas)
reversePartOfArray(mas, 3)
print(mas)
mas = []
reversePartOfArray(mas, 3)
print(mas)
