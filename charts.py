import sys
import argparse
import matplotlib.pyplot as plt


def plot_data(file_name, title, xlabel, ylabel):
    with open(file_name, 'r') as input_file:
        lines = input_file.readlines()
        labels = []
        values = []
        for line in lines:
            split = line[:len(line) - 1].split(',')
            labels.append(split[0])
            values.append([int(x) for x in split[1:]])
        plt.boxplot(values, labels=labels)
        plt.ylabel(ylabel)
        plt.xlabel(xlabel)
        # plt.grid(color='b', linestyle='-', linewidth=0.5)
        plt.title(title)
        plt.show()


parser = argparse.ArgumentParser(description='Genetic algorithm experiment.')
parser.add_argument('-experiment', help='Experiment number', type=int, required=True)

args = parser.parse_args()
experiment = args.experiment

if experiment == 1:
    plot_data('runtime_mutation.csv', 'Runtime vs mutation rate', 'Mutation rate', 'Runtime')
elif experiment == 2:
    plot_data('runtime_population_size.csv', 'Runtime(generations) vs population size', 'Population size',
              'Runtime(generations)')
elif experiment == 3:
    plot_data('runtime_problem_size.csv', 'Runtime vs problem size', 'Problem size', 'Runtime')
elif experiment == 4:
    plot_data('runtime_tournament_size.csv', 'Runtime vs tournament size', 'Tournament size', 'Runtime')
