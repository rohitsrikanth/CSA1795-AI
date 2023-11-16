import heapq

class PuzzleNode:
    def __init__(self, state, parent, move, depth, cost):
        self.state = state
        self.parent = parent
        self.move = move
        self.depth = depth
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_solvable(board):
    inversion_count = 0
    flatten_board = [num for row in board for num in row if num != 0]
    n = len(flatten_board)

    for i in range(n - 1):
        for j in range(i + 1, n):
            if flatten_board[i] > flatten_board[j]:
                inversion_count += 1

    return inversion_count % 2 == 0

def get_blank_position(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return i, j

def heuristic(board, goal):
    h = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != goal[i][j] and board[i][j] != 0:
                h += 1
    return h

def solve_8_puzzle(initial_state, goal_state):
    if not is_solvable(initial_state):
        return "Unsolvable"

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves = ["RIGHT", "LEFT", "DOWN", "UP"]

    initial_node = PuzzleNode(initial_state, None, None, 0, 0)
    goal_node = PuzzleNode(goal_state, None, None, 0, 0)

    visited = set()
    min_heap = [initial_node]

    while min_heap:
        current_node = heapq.heappop(min_heap)
        current_state = current_node.state

        if current_state == goal_state:
            path = []
            while current_node.parent:
                path.append(current_node.move)
                current_node = current_node.parent
            path.reverse()
            return path

        visited.add(tuple(map(tuple, current_state)))

        blank_i, blank_j = get_blank_position(current_state)

        for dir, move in zip(directions, moves):
            new_i, new_j = blank_i + dir[0], blank_j + dir[1]

            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [list(row) for row in current_state]
                new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]

                if tuple(map(tuple, new_state)) not in visited:
                    new_depth = current_node.depth + 1
                    new_cost = new_depth + heuristic(new_state, goal_state)
                    new_node = PuzzleNode(new_state, current_node, move, new_depth, new_cost)
                    heapq.heappush(min_heap, new_node)

    return "No solution found"

# Example usage:
initial_state = [
    [1, 2, 0],
    [3, 4, 5],
    [6, 7, 8]
]

goal_state = [
    [1, 2, 3],
    [4, 5, 0],
    [6, 7, 8]
]

result = solve_8_puzzle(initial_state, goal_state)
if result != "Unsolvable":
    print("Solution path:")
    for step, move in enumerate(result, 1):
        print(f"Step {step}: {move}")
        
else:
    print(result)