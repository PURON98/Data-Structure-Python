
from collections import defaultdict
n=int(input("How many  nodes? "))
e=int(input("How many  edges? "))
adj = defaultdict(list)
print("Enter Edges information ")
for i in range(e):
    u,v = input("Edge %d: " %(i+1)).split()
    if u not in adj:
        adj[u]=[v]
    else:
        adj[u].append(v)
    if v not in adj:
        adj[v].append(u)
print(adj)
