def zeroLastNoOrder(arr):
    zeroInd = len(arr) - 1
    i = 0
    while i < zeroInd:
        if arr[zeroInd] == 0:
            zeroInd -= 1
        else:
            if arr[i] == 0:
                arr[i], arr[zeroInd] = arr[zeroInd], arr[i]
                zeroInd -= 1
            i += 1
    return arr

# 1 проход по массиву, но большее кол-во перестановок элементов
def zeroLastSaveOrderVer1(arr):
    zeroInd = 0
    n = len(arr)
    while zeroInd < n and arr[zeroInd] != 0:
        zeroInd += 1
    for i in range(zeroInd + 1, n):
        if arr[i] != 0:
            arr[i], arr[zeroInd] = arr[zeroInd], arr[i]
            zeroInd += 1
    return arr

# 2 прохода по массиву, но нет перестановок элементов
def zeroLastSaveOrderVer2(arr):
    indInsert = 0
    n = len(arr)
    for i in range(n):
        if arr[i] != 0:
            arr[indInsert] = arr[i]
            indInsert += 1
    for i in range(indInsert, n):
        arr[i] = 0
    return arr


mas1 = [0, 0, 1, 0, 3, 12]
mas2 = [0, 33, 57, 88, 60, 0, 0, 80, 99]
mas3 = [0, 0, 0, 18, 16, 0, 0, 77, 99]
mas4 = [0, 0, 0, 0, 0]
print('Initial arrays')
print(mas1, mas2, mas3, mas4, sep='\n')
print('No order')
print(zeroLastNoOrder(mas1.copy()), zeroLastNoOrder(mas2.copy()),
      zeroLastNoOrder(mas3.copy()), zeroLastNoOrder(mas4.copy()), sep='\n')
print('Save order version 1')
print(zeroLastSaveOrderVer1(mas1.copy()), zeroLastSaveOrderVer1(mas2.copy()),
      zeroLastSaveOrderVer1(mas3.copy()), zeroLastSaveOrderVer1(mas4.copy()), sep='\n')
print('Save order version 2')
print(zeroLastSaveOrderVer2(mas1.copy()), zeroLastSaveOrderVer2(mas2.copy()),
      zeroLastSaveOrderVer2(mas3.copy()), zeroLastSaveOrderVer2(mas4.copy()), sep='\n')
