import argparse
parser = argparse.ArgumentParser(
    description='Compares two configuration files and shows a difference.'
)
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.parse_args()

def main():
    print("Lets's generete some difference!")

if __name__ == "__main__":
    main()