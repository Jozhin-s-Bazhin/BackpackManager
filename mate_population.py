import random
import classes
import schedule
import copy


def fix_configuration(configuration):
    """Removes duplicates and adds back missing subjects"""
    broken_folders = []
    duplicate_subjects = {}
    fixed_folders = []

    # Puts subjects into a list of lists instead of a list of folders to prevent weight errors (Please?)
    for folder in configuration.folders:
        new_folder = []
        for subject in folder.subjects:
            new_folder.append(subject)
        broken_folders.append(new_folder)

    # Makes a list of all subjects that later gets used to find duplicates
    for folder in broken_folders:
        for subject in folder:
            duplicate_subjects[subject.name] = False

    # Makes list of all missing subjects
    missing_subjects = [subject for subject in schedule.subjects if subject.name not in duplicate_subjects]

    # Adds back missing subjects
    for subject in missing_subjects:
        duplicate_subjects[subject.name] = False
        random_folder = random.randint(-1, len(broken_folders)-1)
        if random_folder == -1:
            broken_folders.append([subject])
        else:
            if len(broken_folders[random_folder]) < 4:
                broken_folders[random_folder].append(subject)
            else:
                broken_folders.append([subject])

    # Removes duplicates
    for folder in broken_folders:
        folder_subjects = []
        for subject in folder:
            if duplicate_subjects[subject.name] == False:
                folder_subjects.append(subject)
                duplicate_subjects[subject.name] = True
        if folder_subjects:
            fixed_folders.append(classes.Folder(folder_subjects))

    return(classes.Configuration(fixed_folders))


def mate_configurations(parent1, parent2):
    """Takes two parent configurations as arguments and returns two child configurations by randomly swapping the folders in them"""
    
    while True:
        child1 = copy.copy(parent1)
        child2 = copy.copy(parent2)
        
        for index1, folder1 in enumerate(child1.folders):
            if random.randint(0,1) == 1:
                index2 = random.randint(0, len(child2.folders)-1)
                folder1t = child1.folders[index1]
                child1.folders[index1] = child2.folders[index2]
                child2.folders[index2] = folder1t
        
        child1 = fix_configuration(child1)
        child2 = fix_configuration(child2)

        if child1.is_configuration_valid and child2.is_configuration_valid:
            return([child1, child2])


def mate_all_configs(population_slice):
    new_population = []

    if len(population_slice) % 2 != 0:
        del population_slice[-1]

    for parent1, parent2 in zip(population_slice[::2], population_slice[1::2]):
        for child in mate_configurations(parent1, parent2):
            new_population.append(child)

    return new_population