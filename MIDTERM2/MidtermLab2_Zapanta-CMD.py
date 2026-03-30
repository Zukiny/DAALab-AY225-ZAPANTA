import difflib
import pandas as pd
import heapq
import tkinter as tk
from tkinter import filedialog
import re

def find_closest_node(user_input, nodes):
    user_input = user_input.lower()
    for node in nodes:
        if node.lower() == user_input:
            return node
    match = difflib.get_close_matches(user_input, nodes, n=1, cutoff=0.4)
    if match:
        print(f"Did you mean: {match[0]}?")
        return match[0]
    return None

def pick_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename(title="Select ANY data file", filetypes=[("All Files", "*.*")])

def load_graph(file_path):
    print("\nReading file...")
    try:
        df = pd.read_csv(file_path)
        print("Detected: CSV format")
    except:
        try:
            df = pd.read_csv(file_path, sep=None, engine="python")
            print("Detected: Flexible table format")
        except:
            df = None
    if df is None or df.empty:
        print("Fallback: Parsing raw text...")
        edges = []
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                parts = re.findall(r"[A-Za-z]+|\d+\.?\d*", line)
                if len(parts) >= 5:
                    edges.append({
                        "from": parts[0],
                        "to": parts[1],
                        "distance": float(parts[2]),
                        "time": float(parts[3]),
                        "fuel": float(parts[4])
                    })
        df = pd.DataFrame(edges)
    df.columns = df.columns.str.lower().str.strip()
    col_map = {}
    for col in df.columns:
        if "from" in col:
            col_map[col] = "from"
        elif "to" in col:
            col_map[col] = "to"
        elif "distance" in col or "dist" in col:
            col_map[col] = "distance"
        elif "time" in col:
            col_map[col] = "time"
        elif "fuel" in col:
            col_map[col] = "fuel"
    df = df.rename(columns=col_map)
    if not {"from", "to"}.issubset(df.columns):
        print("Trying column auto-detection...")
        df.columns = ["from", "to", "distance", "time", "fuel"][:len(df.columns)]
    print("\nLoaded Data Preview:")
    print(df.head())
    return df

def dijkstra(df, start, end, weight):
    adj = {}
    for _, row in df.iterrows():
        try:
            w = float(row[weight])
            adj.setdefault(row["from"], []).append((row["to"], w))
        except (ValueError, KeyError):
            continue
    all_nodes = set(df["from"]).union(df["to"])
    if start not in all_nodes or end not in all_nodes:
        return [], float("inf")
    dist = {node: float("inf") for node in all_nodes}
    prev = {node: None for node in all_nodes}
    dist[start] = 0
    heap = [(0, start)]
    visited = set()
    while heap:
        d, u = heapq.heappop(heap)
        if u in visited:
            continue
        visited.add(u)
        for v, w in adj.get(u, []):
            alt = d + w
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
                heapq.heappush(heap, (alt, v))
    path = []
    cur = end
    while cur is not None:
        path.append(cur)
        cur = prev.get(cur)
    path.reverse()
    if path[0] != start or dist[end] == float("inf"):
        return [], float("inf")
    return path, dist[end]

def main():
    print("\n=== Smart Network Path Calculator ===")
    file_path = pick_file()
    if not file_path:
        print("No file selected.")
        return
    df = load_graph(file_path)
    nodes = sorted(set(df["from"]).union(df["to"]))
    print("\nDetected Nodes:", nodes)
    print("\n1. Single Node")
    print("2. All Nodes")
    mode = input("Choose Node Calculation: ")
    print("\nOptimize by:")
    print("1. Distance")
    print("2. Time")
    print("3. Fuel")
    print("4. All (Distance, Time, Fuel)")
    choice = input("Choose Optimize Option: ")
    if choice == "4":
        weights_list = ["distance", "time", "fuel"]
    else:
        weight_map = {"1": "distance", "2": "time", "3": "fuel"}
        weight = weight_map.get(choice, "distance")
        weights_list = [weight]
        if weight not in df.columns:
            print(f"Error: '{weight}' column not found. Available: {list(df.columns)}")
            return
    valid_weights = [w for w in weights_list if w in df.columns]
    if not valid_weights:
        print("No valid weight columns available.")
        return
    is_all = len(valid_weights) > 1
    weight = valid_weights[0] if not is_all else None
    if mode == "1":
        user_start = input("Start node: ")
        start = find_closest_node(user_start, nodes)
        if not start:
            print("No matching start node found.")
            return
        print(f"\nPaths from {start}:")
        for end in nodes:
            if start == end:
                continue
            if is_all:
                print(f"\n  {start} -> {end}:")
                for w in valid_weights:
                    label = w.capitalize()
                    p, c = dijkstra(df, start, end, w)
                    if c == float("inf"):
                        print(f"    {label}: No path")
                    else:
                        if len(p) == 1:
                            print(f"    {label}: {p[0]} ({c:.2f})")
                        else:
                            print(f"    {label}: {' -> '.join(p)} ({c:.2f})")
            else:
                path, cost = dijkstra(df, start, end, weight)
                if cost == float("inf"):
                    print(f"{start} -> {end}: No path")
                else:
                    label = weight.capitalize()
                    if len(path) == 1:
                        print(f"{path[0]} ({label}: {cost:.2f})")
                    else:
                        print(f"{start} -> {end}: {' -> '.join(path)} ({label}: {cost:.2f})")
    else:
        for start in nodes:
            print(f"\n=== From {start} ===")
            for end in nodes:
                if start == end:
                    continue
                if is_all:
                    print(f"  {start} -> {end}:")
                    for w in valid_weights:
                        label = w.capitalize()
                        p, c = dijkstra(df, start, end, w)
                        if c == float("inf"):
                            print(f"    {label}: No path")
                        else:
                            if len(p) == 1:
                                print(f"    {label}: {p[0]} ({c:.2f})")
                            else:
                                print(f"    {label}: {' -> '.join(p)} ({c:.2f})")
                else:
                    path, cost = dijkstra(df, start, end, weight)
                    if cost == float("inf"):
                        print(f"  {start} -> {end}: No path")
                    else:
                        label = weight.capitalize()
                        if len(path) == 1:
                            print(f"  {path[0]} ({label}: {cost:.2f})")
                        else:
                            print(f"  {start} -> {end}: {' -> '.join(path)} ({label}: {cost:.2f})")

if __name__ == "__main__":
    main()
