def misplaced_tiles(state, goal):

    h = 0

    for i in range(9):

        # Ignore the blank tile
        if state[i] == 0:
            continue

        if state[i] != goal[i]:
            h += 1

    return h


def moves(state):

    result = []

    blank = state.index(0)

    row = blank // 3
    col = blank % 3

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
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

    visited = set()

    while states:

        # Find state with smallest f = g + h
        best = 0

        for i in range(len(states)):

            f1 = states[i][1] + heuristic(states[i][0], goal)
            f2 = states[best][1] + heuristic(states[best][0], goal)

            if f1 < f2:
                best = i

        current, g, path = states.pop(best)

        # Skip already visited states
        if current in visited:
            continue

        visited.add(current)

        # Goal reached
        if current == goal:
            return path

        # Generate possible moves
        for next_state in moves(current):

            if next_state not in visited:

                new_g = g + 1
                new_path = path + [next_state]

                states.append(
                    (next_state, new_g, new_path)
                )

    return None


def print_state(state):

    print(
        state[0], state[1], state[2]
    )

    print(
        state[3], state[4], state[5]
    )

    print(
        state[6], state[7], state[8]
    )


def main():

    print("Enter initial state (use 0 for blank):")
    start = tuple(map(int, input().split()))

    print("Enter goal state (use 0 for blank):")
    goal = tuple(map(int, input().split()))

    path = astar(start, goal, misplaced_tiles)

    if path is None:

        print("\nNo solution found")

    else:

        print("\nSolution found!")
        print("Number of moves:", len(path) - 1)
        print()

        for state in path:

            print_state(state)
            print()


if __name__ == "__main__":
    main()