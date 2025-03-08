# 1. Read a CSV file and print its contents
import csv
with open("data.csv", mode="r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# 2. Count the number of words in a text file
def count_words(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        words = text.split()
        return len(words)

filename = "sample.txt"
print(f"Number of words: {count_words(filename)}")

# 3. Read JSON data from a file and convert it into a Python dictionary
import json
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)
    print(data) 
