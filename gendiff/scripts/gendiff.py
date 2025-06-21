import argparse
import json
import os

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
# parser.add_argument('first_file')
# parser.add_argument('second_file')
parser.add_argument('-f', '-format', type=str, metavar='FORMAT', help='set format of output')
parser.parse_args()

def main():
    print("Lets's generete some difference!")
    filepath1 = '/home/atesinde/python-project-50/tests/file1.json'
    filepath2 = '/home/atesinde/python-project-50/tests/file2.json'
    with open(filepath1, 'r', encoding='utf-8') as file:
        json_file1 = json.load(file)
    with open(filepath2, 'r', encoding='utf-8') as file:
        json_file2 = json.load(file)
    print(json_file1)
    print(json_file2)

if __name__ == "__main__":
    main()