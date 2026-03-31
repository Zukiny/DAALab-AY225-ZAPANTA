# PathFinder - Route Optimization Tool

A Python-based GUI application that finds optimal routes between locations using Dijkstra's algorithm.

## Features

- **Multiple Optimization Modes**: Choose between Distance, Time, or Fuel consumption
- **Interactive Map**: Visual representation of the network with node and path highlighting
- **Route Animation**: Animated path visualization showing the optimal route
- **Real-time Results**: Displays distance (km), time (minutes), and fuel consumption (liters)

## Supported Locations

- NOVELETA
- IMUS
- BACOOR
- KAWIT
- DASMA
- INDANG
- SILANG
- GENTRI

## How to Use

1. Launch the application
2. Select a starting location from the "From" dropdown
3. Select a destination from the "To" dropdown
4. Choose an optimization mode (Distance, Time, or Fuel)
5. Click "FIND ROUTE" to calculate and visualize the optimal path
6. Click "RESET" to clear results and start over

## Requirements

- Python 3.x
- tkinter (usually included with Python)
- CSV file with network data (Database.csv)

## Data Format

The application expects a CSV file named `Database.csv` with the following columns:
- From Node
- To Node
- Distance (km)
- Time (mins)
- Fuel (Liters)

## Algorithm

The application uses **Dijkstra's Algorithm** to find the shortest path between two nodes based on the selected optimization criterion (distance, time, or fuel).

## GUI Design

- Modern dark theme with blue and orange accents
- Compact interface with real-time visualization
- Color-coded highlighting: Blue for selected nodes, Orange for optimal path
- Distance labels displayed on edges