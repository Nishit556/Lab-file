def Merge_Sort(array):
    if len(array) > 1:
        mid = len(array)//2
        Left = array[:mid]
        Right = array[mid:]

        Merge_Sort(Left)
        Merge_Sort(Right)

        i = j = k = 0

        while i < len(Left) and j < len(Right):
            if Left[i] < Right[j]:
                array[k] = Left[i]
                i += 1
            else:
                array[k] = Right[j]
                j += 1
            k += 1

        while i < len(Left):
            array[k] = Left[i]
            i += 1
            k += 1

        while j < len(Right):
            array[k] = Right[j]
            j += 1
            k += 1
    for i in range(len(array)):
        print(array[i])
Merge_Sort([3,2,6,4,7,3])
