def search(list1, n):
    for i in range(len(list1)):
        if n == list1[i]:
            print("Element is found at index : ", i)
            break
    else:
        print("Element not found")


l = int(input("List length: "))
print("Type Elements one by one:")
list1 = [int(input()) for i in range(l)]
n = int(input("Type key you want to search : "))
search(list1, n)
