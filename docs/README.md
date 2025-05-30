# Dijkstra's Algorithm Visualizer

This documentation provides an overview of the Dijkstra's Algorithm Visualizer application. This tool visualizes Dijkstra's pathfinding algorithm in the context of a coal mine, represented as a 2D grid.

## Table of Contents

1. [Introduction](introduction.md)
2. [How to Use](how_to_use.md)
3. [Implementation Details](implementation_details.md)
4. [Algorithm Explanation](algorithm_explanation.md)

## Quick Start

1. Run the application by executing `python dijkstra_visualizer.py`
2. Read the welcome screen instructions and click "Start Application" to begin
3. Use left-click to place:
   - First click: Start point (orange)
   - Second click: End point (turquoise)
   - Subsequent clicks or dragging: Barriers/walls (black)
4. Use right-click to remove any placed node
5. Click the "Start Algorithm" button or press the Spacebar to start the visualization
6. Click "Clear Path" to clear the path but keep barriers and start/end points
7. Click "Reset All" or press 'C' to completely reset the grid
8. Press 'Escape' to return to the welcome screen

## Color Legend

- **Orange**: Start point
- **Turquoise**: End point
- **Black**: Barriers/Walls
- **Red**: Visited nodes
- **Green**: Nodes in the queue
- **Yellow**: Final path
- **White**: Unvisited nodes

For more detailed information, please see the documentation files linked in the Table of Contents.