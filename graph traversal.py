import numpy as np
import matplotlib.pyplot as plt
import math
from heapq import heapify, heappush, heappop
from collections import defaultdict
from skimage.draw import line_nd, random_shapes

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

'''




# Initialize the map
map, labels = random_shapes((200,300),20,5,num_channels=1)
#map = np.ones((200, 300)) * 255

# Define start and goal positions
q_start = (100, 150)
q_goal = (np.random.randint(0, len(map)), np.random.randint(0, len(map[0])))
q_new = (0, 0)
K_max = 1000  # Max number of vertices in the RRT
delta_q = 10

# Initialize graph with one node and no neighbors
G = {q_start: []}
k = 0

# Visualize the map
plt.ion()
fig, ax = plt.subplots()
#ax.imshow(map, cmap='gray')
ax.imshow(map)
ax.plot(q_goal[1], q_goal[0], 'y*')
ax.plot(q_start[1], q_start[0], 'g*')

# Helper functions
def get_random_node():
    return (np.random.randint(0, len(map)), np.random.randint(0, len(map[0])))

def get_nearest_node(random_node):
    keys = list(G.keys())
    distances = [((node[0] - random_node[0])**2 + (node[1] - random_node[1])**2, node) for node in keys]
    nearest_index = distances.index(min(distances))
    return distances[nearest_index][1]

def steer_node(q_near, q_rand, delta_q):
    theta = np.arctan2(q_rand[0] - q_near[0], q_rand[1] - q_near[1])
    return (q_near[0] + int(delta_q * np.sin(theta)), q_near[1] + int(delta_q * np.cos(theta)))

def check_path(map, a, b):
    (x, y) = line_nd(a, b, integer=True)
    for i in range(len(x)):
        value_at_point = map[x[i], y[i]]
        if value_at_point != 255:
            ax.plot([a[1], y[i]], [a[0], x[i]], 'm-')
            return False
        
        ax.plot(y[i], x[i], 'w.')
    return True

# RRT algorithm
print(f'Start: {q_start}, Goal: {q_goal}')

while k < K_max and q_new != q_goal:

    if map[q_start] != 255 or map[q_goal] != 255:
        print(f"Start or Goal point is not valid (not 255). Start: {map[q_start]}, Goal: {map[q_goal]}")
        exit() 

    if np.random.rand() < 0.1:
        q_rand = q_goal
    else:
        q_rand = get_random_node()

    q_near = get_nearest_node(q_rand)
    q_new = steer_node(q_near, q_rand, delta_q)

    if check_path(map, q_near, q_new) == False:
        continue

    dist_q_near2q_new = (q_near[0] - q_new[0])**2 + (q_near[1] - q_new[1])**2

    if np.sqrt((q_new[0] - q_goal[0])**2 + (q_new[1] - q_goal[1])**2) < delta_q:
        q_new = q_goal

    if 0 <= q_new[0] < len(map) and 0 <= q_new[1] < len(map[0]):
        G[q_near].append((dist_q_near2q_new, q_new))
        if q_new not in G:
            G[q_new] = []
        G[q_new].append((dist_q_near2q_new, q_near))

        ax.plot(q_new[1], q_new[0], 'c.')
        ax.plot([q_near[1], q_new[1]], [q_near[0], q_new[0]], 'c-')

        k += 1

    plt.draw()
    plt.pause(0.1)

# A* algorithm
queue = [(0, q_start)]
heapify(queue)
visited = set()
parent = {}
path = []
distances = defaultdict(lambda: float("inf"))
distances[q_start] = 0

while queue:
    (currentdist, v) = heappop(queue)
    visited.add(v)

    if v == q_goal:
        while v in parent:
            path.insert(0, v)
            v = parent[v]
        path.insert(0, q_start)
        path.append(q_goal)
        break

    for (cost, u) in G[v]:
        if u not in visited:
            new_cost = distances[v] + cost
            if new_cost < distances[u]:
                distances[u] = new_cost
                heappush(queue, (new_cost, u))
                parent[u] = v

for p in path:
    ax.plot(p[1], p[0], 'r.')
    #path.append(p)

print(f'Path: {path}')

plt.ioff()
plt.show()
