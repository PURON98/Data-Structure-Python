def binary_search(list, low, high, k):
    if high >= low:
        mid = (high + low) // 2
        if list[mid] == k:
            return mid
        elif list[mid] > k:
            return binary_search(list, low, mid - 1, k)
        elif list[mid] < k:
            return binary_search(list, mid + 1,high, k)
    else:
        return -1


l = int(input("List size: "))
print('Type the elements one by one : ' )
list = [int(input()) for i in range(l)]
k = int(input('Type the element to search:'))
result = binary_search(list, 0, len(list) - 1, k)
if result != -1:
    print("Element found at index ", str(result))
else:
    print("Element no found")
