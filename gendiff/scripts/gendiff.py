import argparse

from gendiff.parser import file_parser


def generate_diff(data_file1, data_file2):
    all_keys = sorted(set(data_file1.keys()) | data_file2.keys())
    diff_result = ''
    
    for key in all_keys:
        if key in data_file2:
            if key in data_file1 and data_file2[key] == data_file1[key]:
                diff_result = diff_result + f'    {key}: {data_file2[key]}\n'
            elif key in data_file1 and data_file2[key] != data_file1[key]:
                diff_result = diff_result + \
                f'  - {key}: {data_file1[key]}\n  + {key}: {data_file2[key]}\n'
        if key not in data_file2:
            diff_result = diff_result + f'  - {key}: {data_file1[key]}\n'
        if key not in data_file1:
            diff_result = diff_result + f'  + {key}: {data_file2[key]}\n'
    
    diff_result = '{\n' + diff_result + '}'
    print(data_file1)
    print(data_file2)

    return diff_result


def main():
    parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '-format', type=str, metavar='FORMAT',
                    help='set format of output')
    args = parser.parse_args()
    print("Lets's generete some difference!")
    data_file1 = file_parser(args.first_file)
    data_file2 = file_parser(args.second_file)
    diff = generate_diff(data_file1, data_file2)
    print(diff)


if __name__ == "__main__":
    main()