import fileinput
import glob

# concatenate all data in one file
file_list = glob.glob("data/*.jsonl")

with open('raw_dataset.jsonl', 'w') as file:
    input = fileinput.input(file_list)
    file.writelines(input)