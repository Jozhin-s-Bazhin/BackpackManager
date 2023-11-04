FOLDER_WEIGHT = 50
MAX_FOLDERS_PER_DAY = 4
MAX_SUBJECTS_PER_FOLDER = 4


class Subject():
    """This class represents a subject - has a name and weight."""
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __repr__(self):
        return self.name
    

class Day():
    """This class represents a day - contains 7 subjects except Wednesday (4)."""

    schedule_list = []

    def __init__(self, subjects):
        self.subjects = subjects
        Day.schedule_list.append(self)

    def __repr__(self):
        return (self.schedule_list)
    

class Folder():
    """This class represents a folder - contains up to 4 subjects in it."""

    def __init__(self, subjects):
        self.subjects = subjects
        self.total_weight = 0
        self.is_folder_valid = False

        # Calculates if a folder has a valid amount of subjects
        if len(self.subjects) <= MAX_SUBJECTS_PER_FOLDER and len(self.subjects) >= 1:
            self.is_folder_valid = True

        # Calculates the total weight of a folder
            for subject in subjects:
                self.total_weight += subject.weight
            self.total_weight += FOLDER_WEIGHT
    
    def __str__(self):
        return(self.subjects)


class Configuration():
    """This class represents a configuration - contains a list of folders"""

    def __init__(self, folders):
        self.folders = folders

        # Makes a list of all folders used each day
        self.total_weight = 0
        self.is_configuration_valid = True
        self.subject_list = []

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

            for folder in self.folders:
                if len(folder.subjects) > 4:
                    self.is_configuration_valid = False

        for folder in self.folders:
            for subject in folder.subjects:
                self.subject_list.append(subject)            

    def __repr__(self):
        return("Folders: {}\nWeight: {:.1f}g.".format([folder.subjects for folder in self.folders], self.total_weight / 5))