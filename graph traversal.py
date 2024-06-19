import numpy as np
import matplotlib.pyplot as plt
import math
from heapq import heapify, heappush, heappop
from collections import defaultdict
from skimage.draw import line_nd, random_shapes


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
ax.imshow(map, cmap='gray')
#ax.imshow(map)
ax.plot(q_goal[1], q_goal[0], 'y*')
ax.plot(q_start[1], q_start[0], 'g*')

# Maximize the window
manager = plt.get_current_fig_manager()
try:
    manager.window.showMaximized()
except AttributeError:
    # For other backends where showMaximized is not available
    manager.resize(*manager.window.maxsize())

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
        
        #ax.plot(y[i], x[i], 'w.')
    return True

# RRT algorithm
print(f'Start: {q_start}, Goal: {q_goal}')

while k < K_max and q_new != q_goal:

    if map[q_start] != 255 or map[q_goal] != 255:
        print(f"Start or Goal point is not valid (not 255). Start: {map[q_start]}, Goal: {map[q_goal]}")
        exit() 

    if np.random.rand() < 0.001:
        q_rand = q_goal
    else:
        q_rand = get_random_node()

    q_near = get_nearest_node(q_rand)
    q_new = steer_node(q_near, q_rand, delta_q)

    dist_q_near2q_new = (q_near[0] - q_new[0])**2 + (q_near[1] - q_new[1])**2

    if np.sqrt((q_new[0] - q_goal[0])**2 + (q_new[1] - q_goal[1])**2) < delta_q:
        q_new = q_goal

    if check_path(map, q_near, q_new) == False:
        continue

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

for p in range(0, len(path) - 1):
    ax.plot(path[p][1], path[p][0], 'r.')
    ax.plot([path[p][1], path[p+1][1]],[path[p][0], path[p+1][0]], 'r-')


print(f'Path: {path}')

plt.ioff()
plt.show()
