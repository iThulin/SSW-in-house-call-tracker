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

# Week 2 Implementing RRT

map = np.ones((200, 300))*255

q_start = (100, 150)
q_goal = (np.random.randint(0, len(map)), np.random.randint(0, len(map[0])))
q_new = (0,0)
K_max = 1000 # Max number of vertices in the RRT
delta_q = 10


# initialize graph with one node and no neighbors
G = {q_start : []}
k = 0

# Visualize the map
plt.ion()
fig, ax = plt.subplots()
ax.imshow(map)
ax.plot(q_goal[1], q_goal[0], 'y*')
ax.plot(q_start[1], q_start[0], 'g*')



# Helper functions
def get_random_node():
    rand_node = (np.random.randint(0, len(map)), np.random.randint(0, len(map[0])))
    return rand_node

def get_nearest_node(random_node):
    keys = list(G.keys())
    #print(f'\nkeys: {keys}\n')
    distances = [((node[0] - random_node[0])**2 + (node[1] - random_node[1])**2,(node[0], node[1])) for node in keys]
    nearest_index = distances.index(min(distances))
    for entry in G:
        print(f'{entry}: {G[entry]}')
    #print(f'\nDistances: {distances}')
    #print(f'Index: {nearest_index}')
    #print(f'tuple: {distances[nearest_index]}')
    return distances[nearest_index][1]    


def steer_node(q_near, q_rand, delta_q):
    theta = np.arctan2(q_rand[0] - q_near[0], q_rand[1] - q_near[1])
    q_new = (q_near[0] + int(delta_q * np.sin(theta)), q_near[1] + int(delta_q * np.cos(theta)))
    return q_new

print(f'Start: {q_start}, Goal: {q_goal}')

while k < K_max and q_new != q_goal:
    
    # Generate a random point, the nearest point, and the new point to add to graph
    q_rand = get_random_node()
    q_near = get_nearest_node(q_rand)
    q_new = steer_node(q_near, q_rand, delta_q)

    # Print points in question
    #print(f'q_rand: {q_rand}')
    #print(f'q_near: {q_near}')
    #print(f'q_new : {q_new}')

    dist_q_near2q_new = (q_near[0] - q_new[0])**2 + (q_near[1] - q_new[1])**2
    dist_q_rand2q_near = (q_rand[0] - q_near[0])**2 + (q_rand[1] - q_near[1])**2

    #print(f'dist_q_near2q_new: {dist_q_near2q_new}, dist_q_rand2q_near: {dist_q_rand2q_near}')


    #q_new = compute a new configuration by moving delta_q from q_near into the direction of q_rand
            # or use q_rand if closer to q_near than delta_q

    if dist_q_rand2q_near < dist_q_near2q_new:
        q_new = q_rand
        #print(f'overide q_new: {q_new}')


    # Check if q_new is < delta_q from goal
    dist_q_new2q_goal = np.sqrt((q_new[0]-q_goal[0])**2+(q_new[1]-q_goal[1])**2)    
    
    if dist_q_new2q_goal < delta_q:        
        q_new = q_goal



    # If edge between q_near and q_new is collision free   
    if 0 <= q_new[0] < len(map) and 0 <= q_new[1] < len(map):

        # Add q_new to graph
        G[q_near].append(q_new)
        G[q_new] = [q_near]

        # plot new point and line from q_near -> q_new
        ax.plot(q_new[1], q_new[0], 'c.')
        ax.plot([q_near[1], q_new[1]], [q_near[0], q_new[0]], 'c-')

        # Increment number of vertices in graph
        k += 1

    plt.draw()
    plt.pause(.1)

plt.ioff()
plt.show()