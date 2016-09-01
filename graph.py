graph = {
    'A': set(['B', 'C']),
    'B': set(['C', 'D']),
    'C': set(['D']),
    'D': set(['C']),
    'E': set(['F']),
    'F': set(['C'])}

def find_path(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if start not in graph:
        return None

    for node in graph[start]:
        if node not in path:
            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path

    return None

def depth_first_search(graph, start):
    visited, stack = set(), [start]

    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return visited

def breadth_first_search(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend((graph[vertex] - visited))

    return visited

def shortest_path(graph, start, end):

    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for child in graph[vertex] - set(path):
            if child == end:
                return path + [child]
            else:
                queue.append((child, path + [child]))

    return None

    
print depth_first_search(graph, 'A')
print breadth_first_search(graph, 'A')

print shortest_path(graph, 'A', 'D')
