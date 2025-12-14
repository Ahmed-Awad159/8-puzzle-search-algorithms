# 8-Puzzle AI Project

## 📌 Description
This project solves the classic **8-Puzzle problem** using different search algorithms.
The main goal is to compare the performance of **uninformed** and **informed** search strategies
based on execution time and number of expanded nodes.

---

## 🧠 Algorithms Implemented
The following search algorithms are implemented and evaluated:

- Breadth-First Search (BFS)
- Depth-First Search (DFS)
- Uniform-Cost Search (UCS)
- Iterative Deepening Search (IDS)
- A* Search
- Hill Climbing

---

## 📂 Project Structure

```

8-puzzle-ai/
│
├── algorithms/ # Search algorithms implementations
│ ├── BFS.py
│ ├── DFS.py
│ ├── UCS.py
│ ├── IDS.py
│ ├── A_Star.py
│ └── Hill_Climbing.py
│
├── puzzle/ # Puzzle logic and state representation
│ ├── state.py
│ └── puzzle.py
│
├── utils/ # Heuristics and performance metrics
│ ├── heuristics.py
│ └── metrics.py
│
├── experiments/ # Scripts to run and compare algorithms
│ └── run_all.py
│
├── report/ # Project report and charts
│ └── Report File
│
├── main.py # Project entry point
├── README.md

```

## Run the project:
python main.py

## To run all algorithms and compare their performance:
python experiments/run_all.py

## 👥 Team Members & Contributions

Member 1: Ahmed Ashraf Elsayed Kamal

Member 2: Ahmed Awad Hassan Mohamed

Member 3: Omar Hany Fathy Ali

Member 4: Donia Sameh Fathi Abdel Shafi

## 📊 Output

For each algorithm, the following metrics are collected:

- Time Complexity
- Space Complexity
- Solution Optimality
- Path Cost

These results are used for comparison and analysis in the final report.

## 📦 Requirements

- Python 3.x

---