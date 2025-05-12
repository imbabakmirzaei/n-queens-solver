from solver.genetic import solve_genetic
from solver.backtracking import solve_nqueens as solve_backtracking


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

def on_solve(canvas, entry, algorithm_var):
    try:
        n = int(entry.get())
        algo = algorithm_var.get()

        if algo == "Backtracking":
            board = solve_backtracking(n)
        elif algo == "Genetic":
            result = solve_genetic(n)
            if result is None:
                board = None
            else:
                # تبدیل از لیست یک‌بعدی به ماتریس
                board = [[1 if result[j] == i else 0 for j in range(n)] for i in range(n)]
        else:
            board = None

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
    algorithm_var = tk.StringVar(value="Backtracking")
    algo_menu = tk.OptionMenu(root, algorithm_var, "Backtracking", "Genetic")
    algo_menu.pack()
    canvas.pack()

    btn = tk.Button(root, text="Solve", command=lambda: on_solve(canvas, entry, algorithm_var))
    btn.pack()

    root.mainloop()
