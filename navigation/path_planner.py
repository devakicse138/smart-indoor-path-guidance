# navigation/path_planner.py

from collections import deque


# Indoor map
# Each location is connected to nearby locations.

BUILDING_MAP = {
    "Entrance": ["Reception"],
    "Reception": ["Entrance", "Main Corridor"],
    "Main Corridor": ["Reception", "Classroom 1", "Laboratory", "Staircase"],
    "Classroom 1": ["Main Corridor", "Classroom 2"],
    "Classroom 2": ["Classroom 1"],
    "Laboratory": ["Main Corridor", "Lab 2"],
    "Lab 2": ["Laboratory"],
    "Staircase": ["Main Corridor", "First Floor"],
    "First Floor": ["Staircase", "Classroom 3"],
    "Classroom 3": ["First Floor"]
}


def find_path(source, destination):
    """
    Find the shortest path from source to destination
    using Breadth-First Search (BFS).
    """

    if source not in BUILDING_MAP:
        return None

    if destination not in BUILDING_MAP:
        return None

    queue = deque([[source]])
    visited = set()

    while queue:

        path = queue.popleft()
        current_location = path[-1]

        if current_location == destination:
            return path

        if current_location in visited:
            continue

        visited.add(current_location)

        for next_location in BUILDING_MAP[current_location]:

            if next_location not in visited:

                new_path = path + [next_location]
                queue.append(new_path)

    return None


def display_path(path):
    """
    Display the navigation route.
    """

    if path is None:
        print("No route found.")
        return

    print("\nNavigation Route")
    print("----------------")

    for i, location in enumerate(path):

        if i == 0:
            print(f"Start: {location}")

        elif i == len(path) - 1:
            print(f"Destination: {location}")

        else:
            print(f"       ↓")
            print(f"       {location}")


def get_next_location(path, current_index):
    """
    Get the next location in the route.
    """

    if path is None:
        return None

    if current_index + 1 < len(path):
        return path[current_index + 1]

    return None


if __name__ == "__main__":

    print("Smart Indoor Path Planner")
    print("=========================")

    source = "Entrance"
    destination = "Lab 2"

    print(f"\nSource      : {source}")
    print(f"Destination : {destination}")

    path = find_path(source, destination)

    display_path(path)

    if path:

        print("\nStep-by-step navigation:")

        for i in range(len(path) - 1):

            current = path[i]
            next_location = path[i + 1]

            print(
                f"{i + 1}. "
                f"Move from {current} to {next_location}"
            )
