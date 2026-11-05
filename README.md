# --------------------------------------------
# Project Title: Bus Route Management System
# --------------------------------------------


# -------------------
## Project Overview
# -------------------
The **Bus Route Management System** is a Python console application that models a bus network graph to help users manage routes, check stop connections, and calculate the shortest paths (in terms of minimum stops using BFS) along with total distance and fare calculation between stops.

---

# -------------
## Objectives
# -------------
- Store bus stops and route distances in a nested dictionary (Graph structure).
- Display direct connections of any selected bus stop.
- Find the optimal route with the fewest stops using Breadth-First Search (BFS).
- Calculate total route distance and ticket fare based on distance (Rs. 1.50 per km).
- Support bidirectional routes and handle invalid/unconnected stops gracefully.

---

# ----------------------------
## Problem Statement Details
# ----------------------------
- **Language:** Python 3
- **Core Concepts:** Lists, Dictionaries, Graph Basics, BFS Algorithm
- **Fare Rate:** Rs. 1.50 per km
- **Default Distances (km):**
  - Durg-Bhilai: 10
  - Bhilai-Raipur: 30
  - Durg-Raipur: 40
  - Raipur-Bilaspur: 110
  - Raipur-Dhamtari: 80
  - Durg-Rajnandgaon: 45
  - Jagdalpur-Kondagaon: 75 *(Note: Roads work in both directions. Jagdalpur and Kondagaon are unconnected to the other stops).*

---

# -----------
## Features
# -----------
1. **Show Connections:** Displays all direct neighboring stops connected to a given bus stop along with distances.
2. **Find Route (BFS):** Calculates the path with the minimum number of intermediate stops between source and destination.
3. **Fare & Distance Calculation:** Displays total distance (km) and total fare (in Rs.).
4. **Input Validation:** Handles edge cases such as non-existent stops, disconnected routes, and identical source/destination.

---

# ---------------
## Requirements
# ---------------
- Python 3.x installed on system.

---

# --------------
### How to Run
# --------------
1. Clone or download this project folder.
2. Open terminal/command prompt inside the folder.
3. Run the script:
   ```bash
   python one.py

  ---

# -----------------
## Project Mentor
# -----------------
- **Mentored by:** [Mr. Satyaprakash Sethy](https://github.com/SATYAPRAKASHSETHY)
- **GitHub:** [@SATYAPRAKASHSETHY](https://github.com/SATYAPRAKASHSETHY)
- **Role:** Python Mentor / Technical Guide
-
