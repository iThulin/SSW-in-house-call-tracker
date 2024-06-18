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
'''
rows = 20
cols = 30
map = np.random.rand(rows, cols) < 0.1

#

start = (np.random.randint(0, rows), np.random.randint(0, cols))
goal = (np.random.randint(0, rows), np.random.randint(0, cols))

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
                    heappush(queue,(newcost, u))
                    parent[u] = v

        plt.draw()
        plt.pause(0.05)
        continue
    break

plt.ioff()
plt.show()
'''

# Week 2 Implementing RRT

map = np.ones((200, 300))*255

q_start = (100, 150)
q_goal = (np.random.randint(0, len(map)), np.random.randint(0, len(map[0])))
q_new = (0,0)
K_max = 100 # Max number of vertices in the RRT
delta_q = 10


# initialize graph with one node and no neighbors
G = {q_start : []}
k = 0

# Visualize the map
plt.ion()
fig, ax = plt.subplots()
ax.imshow(map)
ax.plot(q_goal[1], q_goal[0], 'y*')
ax.plot(q_start[1], q_start[0], 'b*')



# Helper functions
def get_random_node():
    rand_node = (np.random.randint(0, len(map)), np.random.randint(0, len(map[0])))
    return rand_node

def get_nearest_node(random_node):
    distances = [((node[0] - random_node[0])**2 + (node[1] + random_node[1])**2,(node[0], node[1])) for node in G]
    nearest_index = distances.index(min(distances))
    print(f'\nG: {G}')
    print(f'Distances: {distances}')
    print(f'Index: {nearest_index}')
    print(f'tuple: {distances[nearest_index]}')
    return distances[nearest_index][1]


def steer_node(q_near, q_rand, delta_q):
    theta = np.arctan2(q_rand[0] - q_near[0], q_rand[1] - q_rand[1])
    q_new = (q_near[0] + int(delta_q * np.sin(theta)), q_near[1] + int(delta_q * np.cos(theta)))
    return q_new

print(f'Start: {q_start}, Goal: {q_goal}')

while k < K_max and q_new != 1: #q_goal and k < K_max:
    
    q_rand = get_random_node()
    print(f'q_rand: {q_rand}')

    ax.plot(q_rand[1], q_rand[0], 'r.')

    #q_near = nearest vertex to q_rand that is already in G
    q_near = get_nearest_node(q_rand)
    print(f'q_near: {q_near}')

    ax.plot(q_near[1], q_near[0], 'y.')

    q_new = steer_node(q_near, q_rand, delta_q)

    dist_q_near2q_new = (q_near[0] - q_new[0])**2 + (q_near[1] - q_new[1])**2
    dist_q_rand2q_near = (q_rand[0] - q_near[0])**2 + (q_rand[1] - q_near[1])**2

    print(f'dist_q_near2q_new: {dist_q_near2q_new}, dist_q_rand2q_near: {dist_q_rand2q_near}')


    #q_new = compute a new configuration by moving delta_q from q_near into the direction of q_rand
            # or use q_rand if closer to q_near than delta_q
    
    # If q_new < than delta_q from q_goal:
        #q_new = q_goal

    # If edge between qnear and q_new is collision free
        # Add q_new to G
        # Add an edge between q_near and q_new
        # INcrement k
    

    # get neighbors of nearest nodes
    neighbors = G[q_near]
    print(neighbors)
    neighbors.append(q_rand)
    print(neighbors)

    G[q_near] = neighbors

    G[q_rand] = [q_near]


    k += 1

    plt.draw()
    plt.pause(0.5)

plt.ioff()
plt.show()