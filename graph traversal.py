import numpy as np
import matplotlib.pyplot as plt
import math
from heapq import heapify, heappush, heappop
from collections import defaultdict

#Problem 1
'''
map = [[0, 0, 0],
        [0.8, 0.9, 0],
        [0, 0, 0]]

graph = {(0,0) : [(0,1)],
         (0,1) : [(0,0),(0,2)],
         (0,2) : [(0,1),(1,2)],
         (1,2) : [(0,2),(2,2)],
         (2,0) : [(2,1)],
         (2,1) : [(2,0),(2,2)],
         (2,2) : [(2,1),(1,2)]}
'''
# Problem 2 map
'''
rows = 20
cols = 30
map = np.random.rand(rows, cols) < 0.1

#

#start = (np.random.randint(0, rows), np.random.randint(0, cols))
#goal = (np.random.randint(0, rows), np.random.randint(0, cols))

start = (0, 0)
goal = (19, 29)

print(f'Start: {start}, Goal: {goal}')

def getNeighbors(u):
    neighbors = []
    for delta  in ((0, 1), (0, -1), (1, 0), (-1, 0) ):
        cand = (u[0] + delta[0], u[1] + delta[1])
        if (cand[0] >= 0 and cand[0] < len(map) and cand[1] >= 0 and cand[1] <len(map[0]) and map[cand[0]][cand[1]] < 0.3):
            neighbors.append(cand)
    return neighbors

#print(getNeighbors((2, 0)))

#plt.show()

#start = (0, 0)
#goal = (2, 0)

queue = [start]
visited = {start}
parent = {}
key = goal
path = []

plt.ion()
fig, ax = plt.subplots()

# Visualize the map
ax.imshow(map)
ax.plot(goal[1], goal[0], 'y*')
ax.plot(start[1], start[0], 'b*')


while queue:
    
    # Clear the map
    #ax.clear()

    v = queue.pop(0)

    # plot the newly discovered vertex
    ax.plot(v[1], v[0], 'g*')

    # If path to goal is complete
    if key in parent.keys():
        while key in parent.keys():
            key = parent[key]
            path.insert(0, key)

        path.append(goal)

        #print(f'Path: {path}')

        # plot the path followed
        for p in path:
            ax.plot(p[1], p[0], 'r.')


    for u in getNeighbors(v):
        if u not in visited:
            queue.append(u)
            visited.add(u)
            parent[u] = v

    plt.draw()
    plt.pause(0.05)

plt.ioff()
plt.show()
'''

# Problem 3 map

rows = 20
cols = 30
map = np.random.rand(rows, cols) < 0.1

#

start = (np.random.randint(0, rows), np.random.randint(0, cols))
goal = (np.random.randint(0, rows), np.random.randint(0, cols))

map[start] = True

if map[start] == True:
    print('Reset Start')
    map[start] = False
if map[goal] == True:
    print('Reset Goal')
    map[start] = False

#start = (0, 0)
#goal = (19, 29)

print(f'Start: {start}, Goal: {goal}')

def getNeighbors(u):
    neighbors = []
    for delta  in ((0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, 1), (-1, 0), (-1, 1)):
        cand = (u[0] + delta[0], u[1] + delta[1])
        if (cand[0] >= 0 and cand[0] < len(map) and cand[1] >= 0 and cand[1] <len(map[0]) and map[cand[0]][cand[1]] < 0.3):
            match delta:
                case (0,1) | (1, 0) | (0, -1) | (-1, 0):
                    dist = 1
                case (1, 1) | (1, -1) | (-1, 1) | (-1, 1):
                    dist = math.sqrt(2)

            neighbors.append((dist,cand))
    return neighbors

queue = [(0,start)]
heapify(queue)
visited = {start}
parent = {}
key = goal
path = []

plt.ion()
fig, ax = plt.subplots()



distances = defaultdict(lambda: float("inf"))
distances[start] = 0

# Visualize the map
ax.imshow(map)
ax.plot(goal[1], goal[0], 'y*')
ax.plot(start[1], start[0], 'b*')


while queue:
    
    # Clear the map
    #ax.clear()

    (currentdist, v) = heappop(queue)
    visited.add(v)
    #print(v)

    # plot the newly discovered vertex
    if v == start:
        ax.plot(v[1], v[0], 'r*')
    else:
        ax.plot(v[1], v[0], 'g*')

    # If path to goal is complete

    if key in parent.keys():
        while key in parent.keys():
            key = parent[key]
            path.insert(0, key)

        path.append(goal)

        print(f'Path: {path}')

        # plot the path followed
        for p in path:
            ax.plot(p[1], p[0], 'r.')
        break

    else:
        for (costv_u, u) in getNeighbors(v):
            #print(f'u: {u}, v: {v}')
            if u not in visited:
                newcost = distances[v] + costv_u

                if newcost < distances[u]:
                    distances[u] = newcost
                    heur = np.sqrt((goal[0]-u[0])**2+(goal[1]-u[1])**2)
                    heappush(queue,(newcost + heur, u))
                    parent[u] = v

        plt.draw()
        plt.pause(0.05)
        continue
    break

plt.ioff()
plt.show()