def mergeSortedArrays(arr1, arr2):
    i, j = 0, 0
    mergeMas = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            mergeMas.append(arr1[i])
            i += 1
        else:
            mergeMas.append(arr2[j])
            j += 1
    mergeMas.extend(arr1[i:])
    mergeMas.extend(arr2[j:])
    return mergeMas


mas1 = [3, 8, 10, 11]
mas2 = [1, 7, 9]
print(mergeSortedArrays(mas1, mas2))
