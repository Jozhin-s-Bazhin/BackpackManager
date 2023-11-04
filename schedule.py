import classes
import yaml
import os


file_path = os.path.join(os.getcwd(), "settings.txt")
with open(file_path) as file:
    data1 = yaml.safe_load(file)

subject_data = data1["subjects"]
days_data = data1["days"]


subjects = [classes.Subject(subject["name"], subject["weight"]) for subject in subject_data]


schedule = []

for day in days_data:
    day_subjects = []

    for subject_str in day["subjects"]:
        for subject_obj in subjects:
            if subject_obj.name == subject_str:
                day_subjects.append(subject_obj)

    schedule.append(classes.Day(day_subjects))