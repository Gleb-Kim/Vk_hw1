def reverseArrayLR(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def reversePartOfArray(arr, k):
    n = len(arr)
    reverseArrayLR(arr, 0, n - 1)
    reverseArrayLR(arr, 0, (k - 1) % n)
    reverseArrayLR(arr, k % n, n - 1)


mas = [1, 2, 3, 4, 5, 6, 7]
print(mas)
reversePartOfArray(mas, 3)
print(mas)
reversePartOfArray(mas, 11)
print(mas)
