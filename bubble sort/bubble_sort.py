def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr
        
if __name__ == '__main__':
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(bubble_sort(arr))
    
    arr2 = ["a", "z", "b", "e", "c"]
    print(bubble_sort(arr2))




def buble(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]