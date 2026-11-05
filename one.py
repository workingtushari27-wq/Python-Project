# ===========================================================================================
# PS Number: 83
# Project Title: Bus Route Management System
# Name: Tushari Nagesh
# Email: tushari.nagesh@rungta.org
# Section: Btech CSE A2
# ===========================================================================================


from collections import deque  # Import deque for efficient queue implementation in BFS

# --------------------------------------------------------------------------------------------
# Function 1: Graph Data Structure Definition (Bus Network Mapping)
# --------------------------------------------------------------------------------------------
# Representing stops and distances (in km) as an adjacency list using nested dictionaries
graph = {
    'Durg': {'Bhilai': 10, 'Raipur': 40, 'Rajnandgaon': 45},
    'Bhilai': {'Durg': 10, 'Raipur': 30},
    'Raipur': {'Bhilai': 30, 'Bilaspur': 110, 'Dhamtari': 80, 'Durg': 40},
    'Bilaspur': {'Raipur': 110},
    'Dhamtari': {'Raipur': 80},
    'Rajnandgaon': {'Durg': 45},
    'Jagdalpur': {'Kondagaon': 75},
    'Kondagaon': {'Jagdalpur': 75}
}
# --------------------------------------------
# Constant value for fare rate per kilometer
# --------------------------------------------
FARE_PER_KM = 1.50

# ----------------------------------------------------------------------------------------------
# Function 2: Function to Show Direct Connections of a given Bus Stop
# ----------------------------------------------------------------------------------------------

def show_connections(stop_name):
    # --------------------------------------------------------
    # Check if the requested stop exists in our network graph
    # --------------------------------------------------------
    if stop_name not in graph:
        print(f"Stop '{stop_name}' not found.")
        return
    
    connections = []
    # ------------------------------------------------------------
    # Fetch all neighboring stops and their respective distances
    # ------------------------------------------------------------
    for neighbor, dist in graph[stop_name].items():
        connections.append(f"{neighbor} ({dist} km)")
    # --------------------------------------------
    # Print formatted list of direct connections
    # --------------------------------------------
    print(f"{stop_name} connects to: {', '.join(connections)}")

# ----------------------------------------------------------------------------------------------
# Function 3: Function to Find Route with Fewest Stops using BFS Algorithm
# ----------------------------------------------------------------------------------------------

def find_route(start, end):
    # ----------------------------------------------------------------
    # Boundary Condition: Case where source and destination are same
    # ----------------------------------------------------------------
    if start == end:
        if start in graph:
            print("Source and destination are the same. Distance: 0 km. Fare: Rs. 0.00")
        else:
            print(f"Stop '{start}' not found.")
        return
    # --------------------------------------
    # Invalid Stop / Missing Station Check
    # --------------------------------------
    if start not in graph or end not in graph:
        print(f"No route available between {start} and {end}.")
        return
    # -------------------------------------------------------------------------------
    # Initialize BFS Queue storing current path list and a visited set for tracking
    # -------------------------------------------------------------------------------
    queue = deque([[start]])
    visited = set([start])
    # ------------------------------
    # Standard BFs loop execution
    # ------------------------------
    while queue:
        path = queue.popleft()  # Get first path from queue
        node = path[-1]  # Get last node of current path
        # Target Destination Reached
        if node == end:
            # ---------------------------------------------
            # Calculate cumulative total distance of path
            # ---------------------------------------------
            total_distance = 0
            for i in range(len(path) - 1):
                total_distance += graph[path[i]][path[i+1]]
            # -----------------------------
            # Calculate total ticket fare
            # -----------------------------
            total_fare = total_distance * FARE_PER_KM
            # ---------------------------------------------------------------------
            # Print route, total stops count, total distance, and calculated fare
            # ---------------------------------------------------------------------
            print(f"Route: {' -> '.join(path)}")
            print(f"Stops: {len(path)} | Distance: {total_distance} km | Fare: Rs. {total_fare:.2f}")
            return
        # ------------------------------------
        # Traverse unvisited neighbor nodes
        # ------------------------------------
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    # ----------------------------------------------------------------
    # Triggered if target is unreachable (e.g., Jagdalpur from Durg)
    # ----------------------------------------------------------------
    print(f"No route available between {start} and {end}.")

# -----------------------------------------------------------------------------------------------------
# Function 4: Interactive command-line Menu System
# -----------------------------------------------------------------------------------------------------

def main():
    while True:
        print("\n--- Bus Route Management System ---")
        print("1. Show Connections")
        print("2. Find Route")
        print("3. Exit")
        choice = input("Enter choice (1-3): ").strip()

        if choice == '1':
            stop = input("Enter Stop Name: ").strip()
            show_connections(stop)
        elif choice == '2':
            start = input("From: ").strip()
            end = input("To: ").strip()
            find_route(start, end)
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice, try again.")
# -------------------------------------
# Entry point of the script execution
# -------------------------------------
if __name__ == "__main__":
    main()
    