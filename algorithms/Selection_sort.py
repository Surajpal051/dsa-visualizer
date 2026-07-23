## Selection sorting

def selection_sort(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr

print(selection_sort([86, 14, 6, 51, 35, 43, 65, 30, 27, 33, 72, 12, 93, 31, 37, 76, 53, 61, 87, 64, 79, 52, 10, 69, 95, 99, 42, 74, 23, 58, 59, 36, 40, 75, 63, 97, 1, 3, 57, 48, 29, 9, 62, 68, 7, 38, 60, 82, 8, 50]))