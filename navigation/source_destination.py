# navigation/source_destination.py

from navigation.path_planner import BUILDING_MAP, find_path, display_path


def show_locations():
    """Display all available indoor locations."""

    print("\nAvailable Locations")
    print("-------------------")

    locations = list(BUILDING_MAP.keys())

    for number, location in enumerate(locations, start=1):
        print(f"{number}. {location}")

    return locations


def select_location(locations, message):
    """Ask the user to select a location."""

    while True:

        try:
            choice = int(input(f"\n{message}: "))

            if 1 <= choice <= len(locations):
                return locations[choice - 1]

            print("Invalid choice. Please select a valid number.")

        except ValueError:
            print("Please enter a number.")


def select_source_destination():
    """Select source and destination."""

    locations = show_locations()

    source = select_location(
        locations,
        "Select Source"
    )

    # Destination should be different from source
    while True:

        destination = select_location(
            locations,
            "Select Destination"
        )

        if destination != source:
            break

        print("Source and destination cannot be the same.")

    return source, destination


if __name__ == "__main__":

    print("===================================")
    print(" Smart Indoor Path Guidance System")
    print("===================================")

    source, destination = select_source_destination()

    print("\nSelected Locations")
    print("-------------------")
    print("Source      :", source)
    print("Destination :", destination)

    # Find route
    path = find_path(source, destination)

    # Display route
    display_path(path)
