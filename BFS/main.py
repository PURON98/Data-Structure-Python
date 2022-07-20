from collections import defaultdict
from queue import Queue

n = int(input("n = "))
e = int(input("e = "))
adj = defaultdict(list)
for i in range(e):
    u, v = input("Edge %d: " % (i + 1)).split()
    adj[u].append(v)
    adj[v].append(u)
visited = set()
q = Queue(maxsize=n)
s = input("Enter source node: ")
q.put(s)
visited.add(s)
print("BFS : ")
while not q.empty():
    u = q.get()
    print(u, end=' ')

    for element in adj[u]:
        if element not in visited:
            q.put(element)
            visited.add(element)
