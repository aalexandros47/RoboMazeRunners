# RoboMazeRunners

Welcome to the `RoboMazeRunners` repository! This project houses a sophisticated simulation where our adept robots navigate through complex mazes using various search algorithms, both informed and uninformed. Strap yourself in for a whirlwind of pathfinding excitement!

## 🤖 About the Robot Navigation Problem

The core of this project is to solve the Robot Navigation problem. Here, our robots are placed on an N by M grid, peppered with walls and obstacles. The goal? Navigate through the grid to reach designated cells without bumping into any walls.

- **Grid Dimensions:** Variable (N x M)
- **Start Point:** Marked in red
- **End Points:** Marked in green
- **Obstacles:** Grey cells represent impassable walls

## 📚 Search Algorithms Implemented

We've implemented a variety of tree-based search algorithms to tackle this challenge:

- **DFS (Depth-First Search)**
- **BFS (Breadth-First Search)**
- **GBFS (Greedy Best-First Search)**
- **A* (A-Star Search)**
- **CUS1 and CUS2:** Custom search strategies developed in-house for optimal performance.

Each of these algorithms offers a unique approach to solving the navigation puzzle, providing valuable insights into the effectiveness of different search strategies.

## 🔧 How to Use

To dive into the maze with our robots, you'll need to run the program via command line. Here’s how you can execute the searches:

```bash
C:\file> python main.py method_name
```

Replace `<filename>` with the path to your maze file and `<method>` with the desired search algorithm (`DFS`, `BFS`, `GBFS`, `AS`, `CUS1`, or `CUS2` or `CUS3`).

## 📊 Output Format

When a goal is reached, the output will look like this:

```
filename method
goal number_of_nodes
path
```

If no goal is reachable, you'll see:

```
filename method
No goal is reachable; number_of_nodes
```

## 🚀 Get Started

Clone this repository and navigate into the project directory:

```bash
git clone https://github.com/aalexandros47/RoboMazeRunners.git
cd RoboMazeRunners
```

Then, follow the usage instructions above to run the different search algorithms.

## 📝 Note

This project is designed for educational purposes to illustrate the application of tree-based search algorithms in robot navigation scenarios.
