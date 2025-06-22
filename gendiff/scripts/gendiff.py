import argparse
import json

parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '-format', type=str, metavar='FORMAT', help='set format of output')
args = parser.parse_args()

def generate_diff(filepath1, filepath2):
    with open(filepath1, 'r', encoding='utf-8') as file:
        json_file1 = json.load(file)
    with open(filepath2, 'r', encoding='utf-8') as file:
        json_file2 = json.load(file)
    
    all_keys = sorted(set(json_file1.keys()) | json_file2.keys())
    diff_result = ''
    
    for key in all_keys:
        if key in json_file2:
            if key in json_file1 and json_file2[key] == json_file1[key]:
                diff_result = diff_result + f'    {key}: {json_file2[key]}\n'
            elif key in json_file1 and json_file2[key] != json_file1[key]:
                diff_result = diff_result + f'  - {key}: {json_file1[key]}\n  + {key}: {json_file2[key]}\n'
        if key not in json_file2:
            diff_result = diff_result + f'  - {key}: {json_file1[key]}\n'
        if key not in json_file1:
            diff_result = diff_result + f'  + {key}: {json_file2[key]}\n'
    
    diff_result = '{\n' + diff_result + '}'
    print(json_file1)
    print(json_file2)

    return diff_result

def main():
    print("Lets's generete some difference!")
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)

if __name__ == "__main__":
    main()