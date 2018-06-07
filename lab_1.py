import sys
import argparse
import genetic_algorithm as ga
import numpy as np
import time


def get_argument_value(argument, args_list):
    return args_list[args_list.index(argument) + 1]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ONEMAX genetic algorithm.')
    parser.add_argument('-question', help='Question number', type=int, required=True)
    parser.add_argument('-n', help='Bitstring length', type=int)
    parser.add_argument('-chi', help='Mutation rate', type=float)
    parser.add_argument('-k', help='Tournament size', type=int)
    parser.add_argument('-lambda', help='Population size(individuals)', type=int)
    parser.add_argument('-repetitions', help='The number of repetitions', type=int, default=1)
    parser.add_argument('-bits_x', help='Bitstring input for testing operators')
    parser.add_argument('-bits_y', help='Bitstring input for testing crossover operator (used together with bits_x)')
    parser.add_argument('-population',
                        help='String containing the population represented as bitstrings of length n separated by space')
    args = parser.parse_args()
    question = args.question
    start_time = time.time()

    if question == 1:
        for i in range(args.repetitions):
            print(ga.mutation_operator(args.bits_x, args.chi))
    elif question == 2:
        for i in range(args.repetitions):
            print(ga.crossover_operator(args.bits_x, args.bits_y))
    elif question == 3:
        print(ga.onemax(args.bits_x))
    elif question == 4:
        pop = np.array(args.population.split(' '))
        pop_fitness = np.array([ga.onemax(x) for x in pop])
        for i in range(args.repetitions):
            print(ga.tournament_selection(args.k, pop, pop_fitness))
    elif question == 5:
        lmbd = int(get_argument_value('-lambda', sys.argv[1:]))
        for i in range(args.repetitions):
            t, fbest, xbest = ga.genetic_algorithm(args.n, args.chi, args.k, lmbd)
            print(
                '{:>4}   {:>4}  {:>4}  {:>4}  {:>4}  {:>4}  {:>4}'.format(
                    args.n,
                    args.chi,
                    args.k,
                    lmbd,
                    t,
                    fbest,
                    xbest
                )
            )
    else:
        print('Incorrect question number.')
