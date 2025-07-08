def find_match_index(pos, possible_moves):
    for i in range(len(possible_moves)):
        if possible_moves[i] == pos:
            return i

# Auto-walk using Dijkstra Algorithm
map = [
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '#', '#', '*'],
    ['*', '#', '*', '#', '*'],
    ['*', '*', '*', '#', '*'],
]

print('map:')
for row in map:
    for col in row:
        print(col, end=' ')
    print()
print()

# Translate map to graph
map_size_x = len(map[0])
map_size_y = len(map)

adj_matrix = [[0 for _ in range(map_size_x * map_size_y)] for _ in range(map_size_x * map_size_y)]

possible_moves = []
for i in range(map_size_x):
    for j in range(map_size_y):
            possible_moves.append([i, j])

start_position = [3, 2]
target_position = [1, 4]

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2

    if map[x1][y1] == '#' or map[x2][y2] == '#':
        return 0

    return abs(x1 - x2) + abs(y1 - y2)

graph_size = map_size_x * map_size_y

for idx_p, pivot in enumerate(possible_moves):
    for idx_c, compare in enumerate(possible_moves):

        if map[pivot[0]][pivot[1]] == '#' or map[compare[0]][compare[1]] == '#':
            continue

        if (get_distance(pivot, compare) == 1):
            adj_matrix[idx_c][idx_p] = 1

def get_path(predecessors, start_vertex, end_vertex):
    path = []
    current = find_match_index(end_vertex, possible_moves)
    while current is not None:
        path.insert(0, trace_back_position(current))
        current = predecessors[current]
        if current == find_match_index(start_vertex, possible_moves):
            path.insert(0, trace_back_position(find_match_index(start_vertex, possible_moves)))
            break
    return path
    print(path)
    return '->'.join(str(path))  # Join the vertices with '->'

def trace_back_position(adjacentIdx):
    x = int((adjacentIdx - (adjacentIdx % map_size_x)) / map_size_x)
    y = int(adjacentIdx % map_size_x)
    return [x, y]

def dijkstra(start_vertex_data):
    start_vertex = find_match_index(start_vertex_data, possible_moves)
    distances = [float('inf')] * graph_size
    distances[start_vertex] = 0
    visited = [False] * graph_size
    predecessors = [None] * graph_size

    for _ in range(graph_size):
        min_distance = float('inf')
        u = None
        for i in range(graph_size):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i

        if u is None:
            break

        visited[u] = True

        for v in range(graph_size):
            if adj_matrix[u][v] != 0 and not visited[v]:
                alt = distances[u] + adj_matrix[u][v]
                if alt < distances[v]:
                    distances[v] = alt
                    predecessors[v] = u

    return distances, predecessors

distances, predecessors = dijkstra(start_position)
path = get_path(predecessors, start_position, target_position)

new_map = map.copy()
for walkPos in path:
    new_map[walkPos[0]][walkPos[1]] = 'o'

print('walking path:')
for row in new_map:
    for col in row:
        print(col, end=' ')
    print()
print()

# print('distances: ')
# print(distances)