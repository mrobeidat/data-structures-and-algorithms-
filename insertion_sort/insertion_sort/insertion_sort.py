def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j = j - 1 
        array[j + 1] = key

if __name__ == '__main__':
    
    arr = [8, 4, 23, 42, 16, 15]
    insertionSort(arr)
    print('Sorted Array :')
    print(arr)