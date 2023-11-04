import initial_population
import mate_population


POPULATION_SIZE = 100
CYCLE_COUNT = 25

def find_best_config():
    population = initial_population.create_initial_population(POPULATION_SIZE)

    for i in range(CYCLE_COUNT):
        new_population = []

        new_population = mate_population.mate_all_configs(population)
        population = population + new_population
        population.sort(key=lambda configuration: configuration.total_weight)
        population = population[:len(population)//2]

    best_configuration = population[0]
    
    return best_configuration