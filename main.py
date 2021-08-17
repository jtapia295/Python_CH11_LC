# Import modules here. Use the 'as' keyword to rename 'print_all' as 'display_results'.
import averages
from display import print_all as display_results



# Candidate data:
astronauts = ['Fox','Turtle','Cat','Hippo','Dog']

test_titles = ['Math','Fitness','Coding','Nav','Communication']

scores = [[95, 86, 83, 81, 76],[79, 71, 79, 87, 72],[94, 87, 87, 83, 82],[99, 77, 91, 79, 80],[96, 95, 99, 82, 70]]

# User interface:
prompts = ['display all scores', 'average the scores for each test', 'average the scores for each astronaut','select the next spacewalker']

for index in range(len(prompts)):
  response = input('Would you like to {0}? Y/N: '.format(prompts[index]))
  if response.lower() == 'y':
    if index == 0:
      # Call 'display_results' here and pass in all necessary arguments.

    elif index == 1:
      for title_index in range(len(test_titles)):
        avg = # Call 'average_for_test' here. Pass in title_index and scores as arguments.
        print("{0} test average = {1}%".format(test_titles[title_index], avg))
    elif index == 2:
      for astronaut_index in range(len(astronauts)):
        avg = # Call 'average_for_student' here. Pass in astronaut_index and scores as arguments.
        print("{0}'s test average = {1}%".format(astronauts[astronaut_index], avg))
    else:
      walker = # Call 'random_from_list' to pick a spacewalker from the astronauts list.
      print(walker + " is the next spacewalker.")
  else:
    print("Option skipped.")