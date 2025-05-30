# Implementation Details

This document outlines the technical implementation of the Dijkstra's Algorithm Visualizer.

## Code Structure

The application is organized as follows:

- **Main Components**:
  - Grid and Node representation
  - Dijkstra's algorithm implementation
  - Visualization and UI components
  - Event handling

## Key Classes

### Node Class

The `Node` class represents each cell in the grid and contains:

- Position information (row, col)
- Pixel coordinates (x, y)
- Color state (representing different states during visualization)
- Neighbor nodes
- Methods for changing states (make_start, make_end, make_barrier, etc.)
- Methods for checking states (is_start, is_end, is_barrier, etc.)

```python
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
```

### Button Class

The `Button` class provides UI controls:

- Position and size
- Text content
- Color states (normal and hover)
- Methods for drawing and detecting interactions

```python
class Button:
    def __init__(self, x, y, width, height, text, color, hover_color, text_color=BLACK):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.current_color = color
        self.font = pygame.font.SysFont('arial', 16)
```

## Algorithm Implementation

The Dijkstra's algorithm is implemented in the `dijkstra()` function with these key components:

1. **Priority Queue**: Maintains nodes to visit sorted by current distance
2. **Distance Dictionary**: Tracks the current shortest distance to each node
3. **Came From Dictionary**: Records the path for reconstruction
4. **Visualization Updates**: Updates the display during algorithm execution

The algorithm runs until:
- The end node is found (success)
- The queue is emptied without finding the end node (no path exists)

## Visualization Mechanics

The visualization works through:

1. **Color Coding**:
   - White: Unvisited nodes
   - Green: Nodes in the queue (frontier)
   - Red: Visited nodes
   - Yellow: Final path
   - Black: Barriers
   - Orange: Start node
   - Turquoise: End node

2. **Real-time Updates**:
   - The `draw()` function updates the display after each algorithm step
   - Node colors change to reflect the current state of the algorithm

## User Interaction

User interactions are handled through:

1. **Event Loop**:
   - Pygame's event system processes mouse and keyboard inputs
   - Button clicks are detected through collision detection
   - Grid cell interactions are managed through position calculations

2. **Button Actions**:
   - Start Algorithm: Initializes node neighbors and runs Dijkstra's algorithm
   - Clear Path: Resets nodes that are part of the path, visited, or in the frontier
   - Reset All: Creates a new grid, discarding all current state

## Technical Considerations

- **Performance**: The grid is limited to 30x30 for reasonable performance
- **Simplicity**: All edges have a weight of 1 for easier visualization
- **Extensibility**: The code structure allows for potential extensions like:
  - Different algorithms (A*, BFS, DFS)
  - Variable grid sizes
  - Weighted edges

## Dependencies

The application requires:
- Python 3.x
- Pygame library
- Standard Python libraries (queue, math, sys)