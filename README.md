# COS30019 - Introduction to AI 

This repository contains the code and reports for two projects completed as part of the COS30019 - Introduction to AI course. The projects focus on different aspects of AI: tree-based search algorithms and propositional logic inference engines. Below are the details for each project.

---

## Project 1: Tree-Based Search

### Summary
This project involves implementing various tree-based search algorithms to solve the Robot Navigation problem. Both informed and uninformed search methods are required.

### Implementation
The implementation uses Python and includes the following search algorithms:
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Greedy Best-First Search (GBFS)
- A* Search (AS)
- Custom Uninformed Search Strategy (CUS1)
- Custom Informed Search Strategy (CUS2)

### The Robot Navigation Problem
The environment is represented as an NxM grid with walls. The robot must navigate from a start cell to one of the goal cells, avoiding obstacles.

### File Format
- **Grid Size:** `[N, M]` where N is the number of rows and M is the number of columns.
- **Initial State:** `(x1, y1)` coordinates of the robot.
- **Goal States:** `(xG1, yG1) | (xG2, yG2) | ...` coordinates of the goal cells.
- **Walls:** `(x, y, w, h)` where (x, y) is the top-left corner, w is the width, and h is the height.

### Command Line Operation
The program operates from the command line:
```sh
python search.py <filename> <method>
```
- `<filename>` is the text file containing the problem configuration.
- `<method>` is one of `DFS`, `BFS`, `GBFS`, `AS`, `CUS1`, or `CUS2`.

---

## Project 2: Inference Engine

### Summary
This project involves implementing an inference engine for propositional logic using Truth Table (TT) checking, Forward Chaining (FC), and Backward Chaining (BC) algorithms.

### Implementation
The implementation uses Python and supports the following:
- TT, FC, and BC algorithms for inference.
- The engine takes a Horn-form Knowledge Base (KB) and a query (q) to determine entailment.

### File Format
- **Knowledge Base:** Follows the keyword `TELL` and consists of Horn clauses separated by semicolons.
- **Query:** Follows the keyword `ASK` and is a single proposition symbol.

### Command Line Operation
The program operates from the command line:
```sh
python iengine.py <filename> <method>
```
- `<filename>` is the text file containing the KB and query.
- `<method>` is one of `TT`, `FC`, or `BC`.

### Output
- `YES` or `NO` based on whether the query is entailed by the KB.
- Additional information such as the number of models (TT) or entailed symbols (FC, BC).

### Report
The report includes:
- Instructions on using the program
- Introduction to propositional logic and inference methods
- Implementation details with diagrams and pseudocode
- Testing results
- Features, bugs, and missing functionalities
- Research initiatives and optimizations

---

## Getting Started

### Prerequisites
- Python 3.x

### Installation
Clone the repository:
```sh
git clone https://github.com/aalexandros47/RoboMazeRunners.git
cd Portfolio_Website
```

### Running the Programs
For Project 1:
```sh
python search.py <filename> <method>
```
For Project 2:
```sh
python iengine.py <filename> <method>
```

### Authors
- [Arnob Ghosh](mailto:arnobg108@gmail.com)

---

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
