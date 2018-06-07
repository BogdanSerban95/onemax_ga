import random
import numpy as np


def onemax(bits_x):
    res = 0
    for bit in bits_x:
        res += int(bit)
    return res


def genetic_algorithm(n, chi, k, lmbd):
    t = 0
    fbest = 0
    xbest = ''
    steps = 0

    pop, pop_fitness = generate_initial_population(n, lmbd)

    while True:
        fbest, xbest = find_best(pop, pop_fitness)
        if fbest == n:
            break

        if steps == 1000:
            break

        new_pop = np.array([])
        new_pop_fitness = np.array([])
        for i in range(lmbd):
            x = tournament_selection(k, pop, pop_fitness)
            y = tournament_selection(k, pop, pop_fitness)

            new_individual = crossover_operator(
                mutation_operator(x, chi),
                mutation_operator(y, chi)
            )
            new_pop = np.append(new_pop, new_individual)
            new_pop_fitness = np.append(new_pop_fitness, onemax(new_individual))

        pop = new_pop
        pop_fitness = new_pop_fitness
        steps += 1

    return steps, fbest, xbest


def generate_initial_population(n, lmbd):
    pop = np.array([])
    fitness = np.array([])
    max_num = 2 ** n - 1

    for i in range(lmbd):
        num = random.randint(0, max_num)
        bits = bin(num)[2:].zfill(n)
        pop = np.append(pop, bits)
        fitness = np.append(fitness, onemax(bits))
    return pop, fitness


def find_best(pop_arr, pop_fitness):
    max_idx = np.argmax(pop_fitness)
    return pop_fitness[max_idx], pop_arr[max_idx]


def mutation_operator(bits_x, chy):
    mutation_rate = chy / len(bits_x)
    y = ''
    for bit in bits_x:
        prob = random.uniform(1, 0)
        y += bit_not(bit) if prob < mutation_rate else bit
    return y


def bit_not(bit):
    return '0' if bit == '1' else '1'


def tournament_selection(k, pop, pop_fitness):
    ind = np.random.randint(0, len(pop) - 1, k)
    scores = pop_fitness[ind]

    winners = scores == max(scores)
    winner_pos = ind[winners][random.randint(0, len(scores[winners]) - 1)]
    return pop[winner_pos]


def crossover_operator(bits_x, bits_y):
    z = ''
    for i in range(0, len(bits_x)):
        z += str(random.randint(0, 1) if bits_x[i] != bits_y[i] else bits_x[i])

    return z
