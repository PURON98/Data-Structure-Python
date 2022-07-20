n=int(input("How many items?"))
w=int(input("Total Capacity?"))
print("Enter items weight and value in a separate line")
items=[]
for i in range (n):
    weight,value = map(int,input("Item %d : " %(i+1)).split())
    items.append([weight,value,value/weight])
sorted_items= sorted(items,key=lambda x:x[2],reverse=True)
profit = 0
for i in range(n):
    if w>=sorted_items[i][0]:
        profit+=sorted_items[i][1]
        w -= sorted_items[i][0]
    else:
        profit+=(sorted_items[i][2]*w)
        break

print(profit)
