import csv
import os
from collections import Counter

# Specify the path to the CSV file
file_path = os.path.join(r'python-challenge/Starter_Code 2/PyPoll/Resources/election_data.csv','election_data.csv')

def analyze_election_data(file_path):
    # Rest of your code remains unchanged
    total_votes = 0
    candidates = Counter()
    with open(file_path, newline='') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')
        next(csvreader)  # Skip the header row
        for row in csvreader:
            candidate = row[2]
            total_votes += 1
            candidates.update([candidate])
    winner = candidates.most_common(1)[0][0]
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")
    with open("election_results.txt", "w") as text_file:
        text_file.write("Election Results\n")
        text_file.write("-------------------------\n")
        text_file.write(f"Total Votes: {total_votes}\n")
        text_file.write("-------------------------\n")
        for candidate, votes in candidates.items():
            percentage = (votes / total_votes) * 100
            text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
        text_file.write("-------------------------\n")
        text_file.write(f"Winner: {winner}\n")
        text_file.write("-------------------------\n")
# Specify the path to the CSV file
# file_path = "path/to/election_data.csv"
# Call the function with the file path
analyze_election_data(file_path)