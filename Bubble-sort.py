arr = [23, 12, 45, 67, 34, 89 , 7]
# arr = input("Enter the elements of the array separated by spaces: ").split()
n = len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]

print("Sorted array is:", arr)