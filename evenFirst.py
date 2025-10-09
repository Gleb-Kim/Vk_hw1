def evenFirst(arr):
    evenInd = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[evenInd] = arr[evenInd], arr[i]
            evenInd += 1


mas = [3, 2, 4, 1, 11, 8, 9]
print(mas)
evenFirst(mas)
print(mas)
