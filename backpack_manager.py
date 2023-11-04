### BACKPACK MANAGER ###

# Tired of carrying unnecessary weight? Let BackpackManager™ take the job and make the perfect configuration of folders to minimise your back pain!


# Data structure: There are 4 classes, Subject() which represents one subject you need to carry and has a name and weight, Day() which represents a day with a list of subjects you need to bring that day,
# Folder() which represents a folder you carry one or more subjects in with its own weight and the weight of all the subjects in it, Configuration() which represents a certain combination of folders that should achieve a minimal average weight with a list of folders




# Initialising the classes and variables used for the optimisation algorithm

import random

FOLDER_WEIGHT = 50
MAX_FOLDERS_PER_DAY = 4
MAX_SUBJECTS_PER_FOLDER = 4
INITIAL_POPULATION = 1000


class Subject():
    """This class represents a subject - has a name and weight."""
    subject_list = []

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        Subject.subject_list.append(self)

    def __repr__(self):
        return self.name


Aa = Subject("Aa", 30)
Nd = Subject("Nd", 120)
Ch = Subject("Ch", 60)
Fr = Subject("Fr", 120)
En = Subject("En", 60)
Wi = Subject("Wi", 150)
Ge = Subject("Ge", 60)
Fy = Subject("Fy", 60)
Av = Subject("Av", 30)
Bi = Subject("Bi", 60)
Gd = Subject("Gd", 60)
LO = Subject("LO", 60)
MEV = Subject("MEV", 30)
St = Subject("St", 30)
Du = Subject("Du", 30)


class Day():
    """This class represents a day - contains 7 subjects except Wednesday (4)."""

    schedule_list = []

    def __init__(self, subjects):
        self.subjects = subjects
        Day.schedule_list.append(self)

    def __repr__(self):
        return (self.schedule_list)


Monday = Day([Nd, Ch, Fr, En, Wi, Ge, Fr])
Tuesday = Day([Fy, Av, Bi, Gd, LO, Aa, MEV])
Wednesday = Day([St, Du, Nd, Ch])
Thursday = Day([Ge, Fy, Av, Bi, Gd, LO, Aa])
Friday = Day([MEV, St, Du, Nd, Ch, Fr, En])


class Folder():
    """This class represents a folder - contains up to 4 subjects in it."""

    def __init__(self, subjects):
        self.subjects = subjects
        self.total_weight = 0
        self.is_folder_valid = False

        # Calculates if a folder has a valid amount of subjects
        if len(self.subjects) > MAX_SUBJECTS_PER_FOLDER and len(self.subjects) >= 1:
            self.is_folder_valid = True

        # Calculates the total weight of a folder
        for subject in subjects:
            self.total_weight += subject.weight
        self.total_weight += FOLDER_WEIGHT

    def __str__(self):
        return str(self.subjects)


class Configuration():
    """This class represents a configuration - contains a list of folders"""

    def __init__(self, folders):
        self.folders = folders

        # Makes a list of all folders used each day
        self.total_weight = 0
        self.is_configuration_valid = True

        for day in Day.schedule_list:
            folders_in_day = []
            for subject in day.subjects:

                for folder in self.folders:
                    if subject in folder.subjects:
                        if folder not in folders_in_day:
                            folders_in_day.append(folder)

            # Calculates weight per week
            for folder in folders_in_day:
                self.total_weight += folder.total_weight

            # Calculates if configuration is valid
            if len(folders_in_day) > MAX_FOLDERS_PER_DAY:
                self.is_configuration_valid = False

    def __repr__(self):
        return (str("Folders: {}, Valid: {}, Total weight: {}".format(self.folders, self.is_configuration_valid, self.total_weight)))


# Test for Configuration() class, self.folders, self.is_configuration_valid and self.total_weight parameters

# test_config = Configuration([[Aa, Nd], [Ch, Fy], [Av, Bi, Gd, LO], [MEV, St, Du], [Fr], [En], [Wi]])
# print(test_config)



# Creating initial population

def mk_random_folder(subject_list):
    while True:
        subjects_in_folder = []
        for i in range(random.randint(1, MAX_SUBJECTS_PER_FOLDER)):
            if len(subject_list) > 0:
                subjects_in_folder.append(subject_list[0])

def mk_random_configuration(subject_list):
    while True:
        folder_list = []
        while True: 
            subject_list_random = random.sample(subject_list)
            new_folder = mk_random_folder(subject_list_random)
            subject_list_random = [subject for subject in subject_list_random if subject not in new_folder]

            folder_list.append(new_folder)
            if subject_list_random <= 0:
                break
        if Configuration(folder_list).is_configuration_valid:
            return Configuration(folder_list)

population = []
for i in range(INITIAL_POPULATION+1):
    new_configuration = mk_random_configuration(Subject.subject_list)
    population.append(new_configuration)

print(population)



# Genetic algorythm used to get the most optimal answer

while True:
    for i in range(1, 1000+1):
        pass