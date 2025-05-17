# 🧠 N-Queens Solver with GUI

This project is a visual and interactive implementation of the classic **N-Queens problem**, solved using two distinct approaches:

- ✅ Backtracking (exact and classical method)
- ✅ Genetic Algorithm (approximate, AI-inspired method)

Built with **Python** and a **Tkinter GUI** to allow users to choose the solving method and board size visually.

---

## 📌 What is the N-Queens Problem?

The **N-Queens** problem involves placing N queens on an N×N chessboard such that no two queens attack each other (no same row, column, or diagonal).

---

## 🚀 Features

- 🔁 Two solving methods: **Backtracking** and **Genetic Algorithm**
- 🖼️ GUI interface with chessboard display
- 🎛️ Algorithm selection dropdown
- 🎯 Automatic solution visualization
- 🐍 100% Python, no external libraries

---

## 🗂️ Project Structure

n-queens-solver/
├── solver/
│ ├── backtracking.py # Classical backtracking algorithm
│ └── genetic.py # Genetic algorithm implementation
├── gui/
│ └── main_gui.py # Tkinter GUI logic
├── main.py # Entry point to run the app
├── README.md # Project documentation

---

## 🧠 Algorithms Used

### 1. Backtracking
A recursive depth-first approach. It places queens column by column and backtracks when it encounters conflicts.

- Guarantees a solution if one exists.
- Time complexity: O(N!) in worst case.

### 2. Genetic Algorithm
Inspired by biological evolution:
- Each board is a chromosome.
- Fitness function rewards non-attacking pairs.
- Crossover and mutation generate new candidates.
- Faster for large N, but no guarantee of solution.

---

## 🖥️ GUI

Built using **Tkinter**. GUI allows:
- Entering N (board size)
- Choosing algorithm (Backtracking / Genetic)
- Seeing solution on the board with ♛ symbols

---

## 🛠️ How to Run

### 🔹 Requirements:
- Python 3.x

### 🔹 Run the app:
```bash
python main.py


📌 Notes
For small N (like 8), both algorithms work quickly.

For larger N (like 100), Genetic may return no solution on some runs (since it's approximate).

Backtracking is deterministic; Genetic is randomized.

🧾 Author
Babak Mirzaei
GitHub: @imbabakmirzaei

🧠 Want to Extend?
Add a third method (e.g., CSP with AC-3)

Display solve time in the GUI

Add animation for queen placement

