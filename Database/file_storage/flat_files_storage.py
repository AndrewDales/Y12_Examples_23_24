import json
import pickle
import csv

game_scores = {101: {'first_name': 'Kiran',
                     'last_name': 'Shah',
                     'game_scores': {
                         'Pong': 23,
                         'Pac Man': 97,
                         'Hangman': 15,
                     },
                     },
               102: {'first_name': 'Lolly',
                     'last_name': 'Leitch',
                     'game_scores': {
                         'Pong': 43,
                         'Pac Man': 56,
                         'Hangman': 24,
                     },
                     },
               103: {'first_name': 'Lilly',
                     'last_name': 'Clark',
                     'game_scores': {
                         'Pong': 97,
                         'Pac Man': 26,
                         'Hangman': 4,
                     },
                     },
               104: {'first_name': 'Jenny',
                     'last_name': 'Hillman',
                     'game_scores': {
                         'Pong': 43,
                         'Pac Man': 1298,
                         'Hangman': 21,
                     },
                     },
               105: {'first_name': 'Albert',
                     'last_name': 'Ainger',
                     'game_scores': {
                         'Pong': 4,
                         'Pac Man': 18,
                         'Hangman': 210,
                     },
                     },
               }
# Flat file storage

# Write as a text file
with open('scores.txt', 'w') as file:
    for key, value in game_scores.items():
        file.write(f'{key}, {repr(value)}\n')

# Write a comma-separated variable (CSV) file
with open('scores.csv', 'w', newline='') as file:
    headers = game_scores[101].keys()
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    # flat_data = [f'{key}, {repr(value)}' for key, value in game_scores.items()]
    for item_dict in game_scores.values():
        writer.writerow(item_dict)

# Write as a structured file
# Write to a JavaScript Object Notation File
json_game_scores = json.dumps(game_scores)
with open('scores.json', 'w') as file:
    file.write(json_game_scores)

# Pickle the game_scores object - we will write the pickle file to a binary file ('wb'), this
# is not human readable.
with open('scores_pickle.dat', 'wb') as file:
    pickle.dump(game_scores, file)
