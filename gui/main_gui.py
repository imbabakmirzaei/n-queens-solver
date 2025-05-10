import tkinter as tk
from solver.backtracking import solve_nqueens

def draw_board(canvas, board, n):
    canvas.delete("all")
    size = 500
    cell_size = size // n
    for i in range(n):
        for j in range(n):
            color = "white" if (i + j) % 2 == 0 else "gray"
            canvas.create_rectangle(j*cell_size, i*cell_size, 
                                    (j+1)*cell_size, (i+1)*cell_size,
                                    fill=color)
            if board[i][j] == 1:
                canvas.create_text(j*cell_size + cell_size//2, 
                                   i*cell_size + cell_size//2, 
                                   text="♛", font=("Arial", cell_size//2), fill="red")

def on_solve(canvas, entry):
    try:
        n = int(entry.get())
        board = solve_nqueens(n)
        if board:
            draw_board(canvas, board, n)
        else:
            canvas.delete("all")
            canvas.create_text(250, 250, text="No solution", font=("Arial", 20), fill="red")
    except ValueError:
        pass

def run_gui():
    root = tk.Tk()
    root.title("N-Queens Solver")
    entry = tk.Entry(root)
    entry.pack()
    entry.insert(0, "8")

    canvas = tk.Canvas(root, width=500, height=500)
    canvas.pack()

    btn = tk.Button(root, text="Solve", command=lambda: on_solve(canvas, entry))
    btn.pack()

    root.mainloop()
