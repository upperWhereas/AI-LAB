def manhattan(state, goal):
    h = 0

    for i in range(9):

        if state[i] == 0:
            continue

        current_row = i // 3
        current_col = i % 3

        goal_pos = goal.index(state[i])

        goal_row = goal_pos // 3
        goal_col = goal_pos % 3

        h += abs(current_row - goal_row)
        h += abs(current_col - goal_col)

    return h


def moves(state):

    result = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    directions = [
        (-1, 0), # up
        (1, 0), # down
        (0, -1), # left
        (0, 1) # right
    ]

    for dr, dc in directions:

        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:

            new_blank = new_row * 3 + new_col

            new_state = list(state)

            new_state[blank], new_state[new_blank] = \
                new_state[new_blank], new_state[blank]

            result.append(tuple(new_state))

    return result


def astar(start, goal, heuristic):

    states = [(start, 0, [start])]

    while states:

        # Find state with smallest f
        best = 0

        for i in range(len(states)):

            f1 = states[i][1] + heuristic(states[i][0], goal)
            f2 = states[best][1] + heuristic(states[best][0], goal)

            if f1 < f2:
                best = i

        current, g, path = states.pop(best)

        # Goal reached
        if current == goal:
            return path

        # Generate possible moves
        for next_state in moves(current):

            new_g = g + 1

            new_path = path + [next_state]

            states.append(
                (next_state, new_g, new_path)
            )

    return None

def main():
    print("Enter initial state (use 0 for blank):")
    start = tuple(map(int, input().split()))

    print("Enter goal state (use 0 for blank):")
    goal = tuple(map(int, input().split()))

    path = astar(start, goal, manhattan)

    if path is None:
        print("No solution found")
    else:
        print("\nSolution found!")

        for state in path:
            print(state[:3])
            print(state[3:6])
            print(state[6:9])
            print()

if __name__ == "__main__":
    main()

    USN_Week3_A*_MisplacedTiles
USN_Week3_A*_ManhattanDistance