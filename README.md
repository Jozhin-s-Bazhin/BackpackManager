# BackpackManager
A Python script that optimises the way subject are organised inside folders to reduce the weight and amount of folders you have to carry. 

## Setup and usage
- Install Python 3.11
- Clone the repo: `git clone github.com/Jozhin-s-Bazhin/BackpackManager`
- Edit `settings.txt` to your liking
- Run `python3 backpackmanager.py` to get the optimal configuration. This can take some time.

## Settings
### Subjects
Each line represents a subject. A subject has a name and weight. 
### Days
Each line represents a day. A day is nothing more than a list of subjects you defined above.
### Folder guidelines
This applies to all folders. 
- `weight`: The weight of an empty folder. 
- `max_folders`: This tells the algorithm how many folders it can put per day so they fit inside the backpack.
- `max_subjects`: This does the same as `max_folders`, but for subjects inside folders. 
### Advanced
These are settings for the genetic algorithm. You can play around with these to get better results or performance. I'd recommend to read the code to understand what these do.
- `population_size`: This changes how many configurations are used for calculations.
- `cycle_count`: How many times the population is run trought the optimisation algorithm.
- Note that the script seems to find the best weight pretty quickly and doesn't find anything better no matter how long it computes. I don't know if this is a bug or not, but I did observe similar behaviour when testing this with a completely random algorithm.
