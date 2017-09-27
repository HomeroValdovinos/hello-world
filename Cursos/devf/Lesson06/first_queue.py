from collections import deque

# First In, First Out

queue= deque(["Eric", "Jhon", "Michael"])
print queue

queue.append("Terry")
print queue

queue.append("Graham")
print queue

queue.popleft()
queue.popleft()

print queue

