# Floyd_Warshall_Negative_Cycle_Analysis# Floyd–Warshall Negative Cycle Analysis

## Description

An advanced Python implementation of the Floyd–Warshall algorithm that calculates all-pairs shortest paths in a weighted directed graph and detects negative-weight cycles.

The program uses dynamic programming, path reconstruction, reachability analysis, and negative-cycle impact classification to analyze graph connectivity.

## Features

- All-pairs shortest-path analysis
- Negative-weight edge support
- Negative-cycle detection
- Identification of source–destination pairs affected by negative cycles
- Shortest-path reconstruction
- Unreachable vertex detection
- Dynamic programming implementation
- Detailed terminal output

## Technologies

- Python 3
- Dynamic Programming
- Graph Theory
- Floyd–Warshall Algorithm

## Requirements

- Python 3.8 or later
- Visual Studio Code or another Python editor
- No external libraries required

## Folder Structure

```text
Floyd_Warshall_Negative_Cycle_Analysis/
│
├── floyd_warshall_negative_cycle.py
└── README.md
```

## How to Run

1. Open the project folder in Visual Studio Code.
2. Open the terminal.
3. Run the following command:

```bash
python floyd_warshall_negative_cycle.py
```

## Algorithm

1. Initialize the distance matrix using the graph's adjacency matrix.
2. Initialize the next-vertex matrix for reconstructing paths.
3. Consider each vertex as an intermediate vertex.
4. Update distances whenever a shorter route is found.
5. Detect negative-weight cycles by checking diagonal distances.
6. Identify source–destination pairs that can reach and leave a negative cycle.
7. Display the negative-cycle analysis and shortest-path report.

## Complexity

- **Time Complexity:** O(V³)
- **Space Complexity:** O(V²)

Here, V represents the number of vertices in the graph.

## Flowchart

```text
       Start
         |
         v
 Initialize Graph
         |
         v
 Initialize Distance
 and Next-Vertex Matrices
         |
         v
 Run Floyd–Warshall
         |
         v
 Detect Negative Cycles
         |
         v
 Identify Affected Pairs
         |
         v
 Display Analysis
 and Path Report
         |
         v
        Stop
```

## Applications

- Computer network routing analysis
- Transportation and road-network analysis
- Weighted graph optimization
- Negative-cycle detection in financial graph models
- Graph reachability and dependency analysis

## Note

The program uses zero-based vertex numbering. If a negative-weight cycle is reachable from a source and can reach a destination, that source–destination pair has no finite shortest-path distance.

The supplied example contains a negative-weight cycle, so all vertex pairs are affected.

## Author

Amrit Kumar Jena
