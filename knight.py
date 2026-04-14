import random

def solve_knights_tour():
    # Board setup
    N = 8
    dx = [2, 1, -1, -2, -2, -1, 1, 2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]
    files = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

    def to_coords(notation):
        try:
            f = files.index(notation[0].upper())
            r = 8 - int(notation[1:])
            return r, f
        except:
            return None

    print("--- Knight's Tour Solver ---")
    start_input = input("Enter Start Square (e.g., A1): ")
    end_input = input("Enter End Square (Move 64) (e.g., H8): ")

    start_pos = to_coords(start_input)
    end_pos = to_coords(end_input)

    if not start_pos or not end_pos or start_pos == end_pos:
        print("Invalid input coordinates.")
        return

    board = [[-1 for _ in range(N)] for _ in range(N)]
    
    def is_valid(r, c):
        return 0 <= r < N and 0 <= c < N and board[r][c] == -1

    def get_degree(r, c):
        count = 0
        for i in range(8):
            if is_valid(r + dx[i], c + dy[i]):
                count += 1
        return count

    def backtrack(r, c, move_count):
        # Base Case: Success
        if move_count == N * N:
            return r == end_pos[0] and c == end_pos[1]

        # Optimization: Don't step on the target square early
        if r == end_pos[0] and c == end_pos[1]:
            return False

        # Warnsdorff's Heuristic: Sort candidates by fewest onward moves
        candidates = []
        for i in range(8):
            nr, nc = r + dx[i], c + dy[i]
            if is_valid(nr, nc):
                candidates.append((nr, nc, get_degree(nr, nc)))
        
        # Sort by degree, then randomize ties to prevent getting stuck in loops
        candidates.sort(key=lambda x: (x[2], random.random()))

        for nr, nc, _ in candidates:
            board[nr][nc] = move_count + 1
            if backtrack(nr, nc, move_count + 1):
                return True
            board[nr][nc] = -1 # Backtrack
            
        return False

    # Initialize
    board[start_pos[0]][start_pos[1]] = 1
    print(f"\nSearching for path from {start_input} to {end_input}...")

    if backtrack(start_pos[0], start_pos[1], 1):
        print("\n✅ SUCCESS! Path found:")
        print_board(board)
        print_move_list(board, files)
    else:
        print("\n❌ FAILED: No valid 64-move path found between these squares.")

def print_board(board):
    print("\n   " + "   ".join(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))
    for i, row in enumerate(board):
        row_str = " ".join(f"{val:2}" for val in row)
        print(f"{8-i} [{row_str}]")

def print_move_list(board, files):
    moves = [None] * 64
    for r in range(8):
        for c in range(8):
            val = board[r][c]
            moves[val-1] = f"{files[c]}{8-r}"
    print("\nMove Sequence:")
    print(" -> ".join(moves))

if __name__ == "__main__":
    solve_knights_tour()