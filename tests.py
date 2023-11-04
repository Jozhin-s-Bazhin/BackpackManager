import algorithm
import backpackmanager
import classes
import initial_population
import mate_population
import schedule


# Mating test
example = initial_population.create_initial_population(algorithm.POPULATION_SIZE)
print(example[0])
mated = mate_population.mate_all_configs(example)
print(mated[0])