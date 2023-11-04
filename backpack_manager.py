import random

class Subject():
    """This class represents a subject. A subject has a name and weight."""
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
    """This class represents a day. A day has 7 subjects except Wednesday (4)."""

    schedule_list = []

    def __init__(self, subjects):
        self.subjects = subjects
        Day.schedule_list.append(self)


Monday = Day([Nd, Ch, Fr, En, Wi, Ge, Fr])
Tuesday = Day([Fy, Av, Bi, Gd, LO, Aa, MEV])
Wednesday = Day([St, Du, Nd, Ch, Fr, En, Wi])
Thursday = Day([Ge, Fy, Av, Bi, Gd, LO, Aa])
Friday = Day([MEV, St, Du, Nd, Ch, Fr, En])


class Folder():
    """This class represents a folder. A folder can have up to 4 subjects in it."""

    def __init__(self, subjects,):
        self.subjects = subjects
        self.total_weight = 0

        for subject in subjects:
            self.total_weight += subject.weight
        self.total_weight += 50

    def __str__(self):
        return str(self.subjects)


class Configuration():
    """This class represents a configuration"""

    def __init__(self, folders):
        self.folders = folders
        folder_sum_weight = 0
        folder_sum_total = []

        for day in Day.schedule_list:
            folder_sum_per_day = []

            for subject in day.subjects:
                for folder in folders:
                    if subject in folder:
                        if folder not in folder_sum_per_day:
                            folder_sum_per_day.append(folder)

            for folder in folder_sum_per_day:
                folder_sum_weight += folder.total_weight

            folder_sum_total.append(folder_sum_per_day)

        average_weight = folder_sum_weight / len(folder_sum_total)

    def __repr__(self):
        return " ".join(map(str, self.folders))

    average_weight = "Initialisation went wrong"


MAX_FOLDER_SIZE = 4
population = []


def mk_random_folder(subject_list):
    folder_size = random.randint(1, MAX_FOLDER_SIZE)

    folder_contents = []
    for i in range(1, folder_size):
        if len(subject_list) > 0:
            folder_contents.append(subject_list[0])
            subject_list.remove(subject_list[0])

    return Folder(folder_contents)


def is_config_valid(new_config):
    success = False

    for day in Day.schedule_list:
        folders_in_day = []

        for subject in day.subjects:
            # 'subject' will be studied in 'day'
            for folder in new_config.folders:
                if subject in folder.subjects:
                    if folder not in folders_in_day:
                        folders_in_day.append(folder)

        if len(folders_in_day) > 4:
            success = False
            break
        else:
            success = True
    return success


def mk_new_random_config(subject_list):
    subject_list_temp = list(subject_list)
    random.shuffle(subject_list_temp)

    new_config = Configuration([])
    while subject_list_temp:
        folder = mk_random_folder(subject_list_temp)
        new_config.folders.append(folder)
    return new_config


def add_random_configuration():
    folder_list = []
    success = False

    while success == False:
        new_config = mk_new_random_config(Subject.subject_list)
        success = is_config_valid(new_config)

        if success == True:
            # print(f"success is True {new_config}")
            for folder in new_config.folders:
                if folder == []:
                    new_config.folders.remove(folder)
            population.append(new_config)
        # else:
            # print(f"success is False {new_config}")


for i in range(1, 10):
    add_random_configuration()
print(population)

# def test_mk_random_folder():
#     subject_list = list(Subject.subject_list)
#     print(f"subject_list before {subject_list}")
#     random_folder = mk_random_folder(subject_list)
#     print(f"random_folder {random_folder}")
#     print(f"subject_list after {subject_list}")


# def test_is_config_valid():
#     subject_list = list(Subject.subject_list)
#     print(f"subject_list before {subject_list}")

#     random_config = mk_new_random_config(subject_list)
#     valid = is_config_valid(random_config)

#     print(f"subject_list after {subject_list}")
#     print(f"random_config {random_config}")
#     print(f"valid {valid}")


# test_is_config_valid()

# def mutate1(c):
#     while True:
#         op = random swap? move? move_to_new?

#         # swap
#         d1 = random
#         d2 = random
#         f1 = random
#         f2 = random
#         if f1 == f2:
#             continue

#         s1 = random
#         s2 = random
#         if s1 == s2:
#             continue

#         xxxx
#         validate
#     return cc

# for _ in range(100)



# while True:

print(population)