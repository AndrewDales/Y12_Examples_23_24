import json
import pickle
import csv


with open('scores.txt', 'r') as file:
    scores_from_text = file.readlines()

# Write a comma-separated variable (CSV) file
with open('scores.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    scores_from_csv = [row for row in reader]

# Write as a structured file
# Write to a JavaScript Object Notation File
with open('scores.json', 'r') as file:
    scores_from_json = json.load(file)

# Load from the pickled data - note that we are reading a binary file 'rb'
with open('scores_pickle.dat', 'rb') as file:
    scores_from_pickle = pickle.load(file)
