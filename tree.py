import argparse
import os
from termcolor import colored

parser = argparse.ArgumentParser()
parser.add_argument("path", help="prints the tree starting from the path (green for folders, blue for files)")
args = parser.parse_args()
indent = ""
tree = {}

def list_files(startpath):
    for root, _dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print(colored(f'{indent}{os.path.basename(root)}/', color='green'))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(colored(f'{subindent}{f}', color='blue'))

if os.path.exists(args.path):
    list_files(args.path)
else:
    print("Path that you provided doesn't exist.")
