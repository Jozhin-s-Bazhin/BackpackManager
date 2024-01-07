import classes
import schedule
import random

def mk_random_folder(subject_list):
    """Creates a random folder using a list of subjects"""
    folder_size = random.randint(1, classes.MAX_SUBJECTS_PER_FOLDER)
    folder_subjects = []

    for i in range(folder_size):
        if len(subject_list) > 0:
            folder_subjects.append(subject_list[0])
            subject_list.remove(subject_list[0])

    return classes.Folder(folder_subjects)

def mk_random_configuration():
    """Creates a random valid configuration"""

    while True:
        subject_list_temp = schedule.subjects.copy()
        random.shuffle(subject_list_temp)
        folders_in_configuration = []

        while len(subject_list_temp) > 0:
            new_folder = mk_random_folder(subject_list_temp)

            subject_list_temp = [subject for subject in subject_list_temp if subject not in new_folder.subjects]
            folders_in_configuration.append(new_folder)

        cfg = classes.Configuration(folders_in_configuration)
        if cfg.is_configuration_valid:
            return cfg
        
def create_initial_population(POPULATION_SIZE):
    population = [mk_random_configuration() for i in range(POPULATION_SIZE)]
    return population