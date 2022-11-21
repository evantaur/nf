#!/usr/bin/env python3
import sys
import os
import argparse
from pathlib import Path

__VERSION__=""

'''
ARGPARSE
'''
parser = argparse.ArgumentParser(
    description="Creates a new file with a template based on the file extension or template switch",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog=f'''
Examples:

  # Creates a new file called test.sh
  # with a shebang #!/bin/bash

  {sys.argv[0]} test.sh

'''
    )


parser.add_argument(
    '-d', '--dir',
    help='Create directory structure if needed',
    action="store_true"
    )


parser.add_argument(
    '-v', '--version',
    help='Show version and exit',
    action='version',
    version=f"%(prog)s version {__VERSION__}"
    )


parser.add_argument(
    '-x',
    help='Give execute permission (chmod +x)',
    action="store_true"
    )

parser.add_argument('-t','--template',default=None, help='use this template')


parser.add_argument('filename', help='filename')


args = parser.parse_args()


filename = args.filename


#/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\
#!!! Do NOT modify manually, use build!!!
#!TEMPLATES
#!!! Do NOT modify manually, use build!!!
#\!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/







#check if file exsists and quit if it does.
if Path(filename).exists():
    sys.exit("File not empty")

f_ext = Path(filename).suffix.strip('.') if not args.template else args.template
sb = [""] if f_ext not in templates else templates[f_ext]
try:
    with open(filename, 'w', encoding='utf-8') as file:
        # Writing data to a file
        file.writelines(sb)
        print(f"Wrote a new file to {filename}")
        if args.x:
            chmod = os.system(f"chmod +x {filename}")

except FileNotFoundError:
	print("No such directory.")
