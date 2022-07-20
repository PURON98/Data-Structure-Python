n=int(input("How many items?"))
w=int(input("Total Capacity?"))
print("Enter items weight and value in a separate line")
items=[]
for i in range (n):
    weight,value = map(int,input("Item %d : " %(i+1)).split())
    items.append([weight,value,value/weight])
sorted_items= sorted(items,key=lambda x:x[2],reverse=True)
print(sorted_items)
profit = 0
for element in sorted_items:
    if element[0]<=w:
        profit+=element[1]
        w = element[0]
    else:
        profit+=element[2]*w
    break

print(profit)
