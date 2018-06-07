import genetic_algorithm as ga
import numpy as np
import argparse
import sys


parser = argparse.ArgumentParser(description='Genetic algorithm experiment.')
parser.add_argument('-experiment', help='Experiment number', type=int, required=True)
parser.add_argument('-start', type=float)
parser.add_argument('-end', type=float)

args = parser.parse_args()
experiment = args.experiment

if experiment == 1:
    # Experiment 1 runtime vs mutation rate
    with open('runtime_mutation_{}_{}.csv'.format(args.start, args.end), 'w') as out_file_1:
        print('Starting Experiment 1...')
        results = []
        chis = np.arange(args.start, args.end, 0.2)
        for chi in chis:
            print('Chi: {}'.format(chi))
            res = [str(chi)]
            for j in range(100):
                if (j + 1) % 10 == 0:
                    print('Step: {}'.format(j + 1))
                t, fbest, xbest = ga.genetic_algorithm(200, chi, 4, 100)
                res.append(str(t * 100))
            results.append(res)
            out_file_1.write(','.join(res) + '\n')
    print('Experiment 1 completed!')
elif experiment == 2:
    # Experiment 2 runtime vs problem size
    with open('runtime_problem_size.csv', 'w') as out_file_1:
        print('Starting Experiment 2...')
        results = []
        n_values = np.arange(20, 200, 10)
        for n in n_values:
            print('N: {}'.format(n))
            res = [str(n)]
            for j in range(100):
                if (j + 1) % 10 == 0:
                    print('Step: {}'.format(j + 1))
                t, fbest, xbest = ga.genetic_algorithm(int(n), 0.6, 4, 100)
                res.append(str(t * 100))
            results.append(res)
            out_file_1.write(','.join(res) + '\n')
    print('Experiment 2 completed!')
elif experiment == 3:
    # Experiment 3 runtime vs population size
    with open('runtime_population_size.csv', 'w') as out_file_1:
        print('Starting Experiment 3...')
        results = []
        lambda_values = np.arange(50, 1001, 50)
        for lmbd in lambda_values:
            print('Lambda: {}'.format(lmbd))
            res = [str(lmbd)]
            for j in range(100):
                if (j + 1) % 10 == 0:
                    print('Step: {}'.format(j + 1))
                t, fbest, xbest = ga.genetic_algorithm(200, 0.6, 4, lmbd)
                res.append(str(t * lmbd))
            results.append(res)
            out_file_1.write(','.join(res) + '\n')
    print('Experiment 3 completed!')
elif experiment == 4:
    # Experiment 4 runtime vs tournament size
    with open('runtime_tournament_size.csv', 'w') as out_file_1:
        print('Starting Experiment 4...')
        results = []
        for size in range(2, 6):
            print('Size: {}'.format(size))
            res = [str(size)]
            for j in range(100):
                if (j + 1) % 10 == 0:
                    print('Step: {}'.format(j + 1))
                t, fbest, xbest = ga.genetic_algorithm(200, 0.6, size, 100)
                res.append(str(t * 100))
            results.append(res)
            out_file_1.write(','.join(res) + '\n')
    print('Experiment 4 completed!')