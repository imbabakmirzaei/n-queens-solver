import random

def fitness(board):
    n = len(board)
    non_attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] != board[j] and abs(board[i] - board[j]) != j - i:
                non_attacking += 1
    return non_attacking

def create_board(n):
    return [random.randint(0, n - 1) for _ in range(n)]

def crossover(parent1, parent2):
    n = len(parent1)
    point = random.randint(1, n - 2)
    return parent1[:point] + parent2[point:]

def mutate(board, rate=0.1):
    n = len(board)
    for i in range(n):
        if random.random() < rate:
            board[i] = random.randint(0, n - 1)
    return board

def solve_genetic(n, population_size=100, generations=1000):
    population = [create_board(n) for _ in range(population_size)]

    for gen in range(generations):
        population.sort(key=fitness, reverse=True)
        if fitness(population[0]) == (n * (n - 1)) // 2:
            return population[0]

        next_gen = population[:10]
        while len(next_gen) < population_size:
            p1, p2 = random.choices(population[:50], k=2)
            child = mutate(crossover(p1, p2))
            next_gen.append(child)

        population = next_gen
    return None
