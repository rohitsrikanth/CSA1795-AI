from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    visited = set()
    queue = deque([(0, 0)])

    while queue:
        current_state = queue.popleft()
        a, b = current_state

        if current_state in visited:
            continue

        visited.add(current_state)

        if a == target or b == target:
            return current_state

        # Fill jug A
        queue.append((capacity_a, b))
        # Fill jug B
        queue.append((a, capacity_b))
        # Empty jug A
        queue.append((0, b))
        # Empty jug B
        queue.append((a, 0))
        # Pour water from jug A to jug B
        pour_to_b = min(a, capacity_b - b)
        queue.append((a - pour_to_b, b + pour_to_b))
        # Pour water from jug B to jug A
        pour_to_a = min(b, capacity_a - a)
        queue.append((a + pour_to_a, b - pour_to_a))
        for i in queue:
            if i not in(visited):
                print(i,end="")
        print()
    return "No solution found"

# Example usage
capacity_a = 4  # Capacity of jug A
capacity_b = 3  # Capacity of jug B
target = 2      # Amount of water to be measured

result = water_jug_problem(capacity_a, capacity_b, target)
print(f"Jug A: {result[0]}, Jug B: {result[1]}")
