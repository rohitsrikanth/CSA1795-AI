import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0
    def __lt__(self, other):
        return self.f < other.f
def astar(maze, start, end):
    open_list = []
    closed_list = set()
    start_node = Node(start)
    end_node = Node(end)
    heapq.heappush(open_list, start_node)
    while open_list:
        current_node = heapq.heappop(open_list)
        if current_node.position == end_node.position:
            path = []
            while current_node is not None:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]

        closed_list.add(current_node.position)

        for move in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            node_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])

            if (
                node_position[0] < 0
                or node_position[0] >= len(maze)
                or node_position[1] < 0
                or node_position[1] >= len(maze[0])
                or maze[node_position[0]][node_position[1]] == 1
                or node_position in closed_list
            ):
                continue

            new_node = Node(node_position, current_node)
            new_node.g = current_node.g + 1
            new_node.h = abs(new_node.position[0] - end_node.position[0]) + abs(new_node.position[1] - end_node.position[1])
            new_node.f = new_node.g + new_node.h
            if any(node.f <= new_node.f and node.position == new_node.position for node in open_list):
                continue

            heapq.heappush(open_list, new_node)

    return None
maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0],
    [0, 0, 0, 0, 0],
]
start = (0, 0)
end = (4, 4)

path = astar(maze, start, end)
print(path)