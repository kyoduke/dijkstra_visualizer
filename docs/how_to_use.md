# How to Use the Dijkstra's Algorithm Visualizer

This guide explains how to use the Dijkstra's Algorithm Visualizer application effectively.

## Starting the Application

1. Make sure you have Python and Pygame installed on your system
2. Run the application with the command: `python dijkstra_visualizer.py`
3. The application will open a window with a grid and control buttons at the bottom

## Interface Elements

The interface consists of:
- A grid area representing the coal mine
- Three control buttons at the bottom:
  - **Start Algorithm**: Begins the pathfinding visualization
  - **Clear Path**: Removes the visualized path but keeps barriers and start/end points
  - **Reset All**: Completely resets the grid to its initial state

## Basic Controls

### Mouse Controls

- **Left-click**:
  - First click: Place the start point (orange)
  - Second click: Place the end point (turquoise)
  - Subsequent clicks or dragging: Place barriers/walls (black)
- **Right-click**:
  - Remove any placed node (start, end, or barrier)

### Button Controls

- **Start Algorithm**: Click to begin the pathfinding visualization (only works when both start and end points are placed)
- **Clear Path**: Click to remove the visualized path but keep barriers and start/end points
- **Reset All**: Click to completely reset the grid

### Keyboard Shortcuts

- **Spacebar**: Equivalent to clicking the "Start Algorithm" button
- **C key**: Equivalent to clicking the "Reset All" button

## Step-by-Step Usage Guide

1. **Setup Phase**:
   - Left-click anywhere in the grid to place the start point (orange)
   - Left-click elsewhere to place the end point (turquoise)
   3. Add barriers (black) by left-clicking or dragging your mouse across any remaining cells
   - Right-click to remove any placed element if you want to make changes

2. **Visualization Phase**:
   - Click the "Start Algorithm" button or press the Spacebar
   - Watch as the algorithm explores the grid:
     - Green cells represent nodes in the frontier (to be explored)
     - Red cells represent nodes that have been visited
     - When the end is found, the optimal path appears in yellow

3. **Review and Modify**:
   - After visualization completes, you can:
     - Click "Clear Path" to remove the visualization but keep your barrier setup
     - Click "Reset All" to start completely fresh
     - Make modifications to existing barriers (if you didn't clear the path)

## Tips for Effective Use

- Create different barrier patterns by dragging the mouse to test the algorithm's behavior
- Try placing the start and end points at different distances
- Notice how the algorithm always finds the shortest path
- Observe how the exploration spreads out equally in all directions
- Create mazes with single-cell-width paths to see interesting pathfinding behaviors

## Limitations

- The grid size is fixed at 30x30 cells
- Diagonal movement is not supported in this implementation
- All steps have the same weight (cost of 1) in this implementation

## Next Steps

After understanding the basic visualization, consider exploring the [Implementation Details](implementation_details.md) and [Algorithm Explanation](algorithm_explanation.md) documents to learn more about how Dijkstra's algorithm works.