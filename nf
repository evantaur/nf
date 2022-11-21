#!/usr/bin/env python3
import sys
import os
import argparse
from pathlib import Path


__VERSION__ = 0.05

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

def upgrade():
    filepath = os.path.realpath(__file__)
    if not os.access(filepath, os.W_OK):
        sys.exit("Permission denied!")
    try:
        r.urlretrieve('https://raw.githubusercontent.com/evantaur/nf/main/nf', filepath)
        sys.exit("Upgrade complete")
    except PermissionError:
        sys.exit("Permission denied!")

try:
    import urllib.request as r
    filepath = os.path.realpath(__file__)
    if os.access(filepath, os.W_OK):
       parser.add_argument(
            '--upgrade',
            help='Upgrade script',
            action="store_true"
        )

except ModuleNotFoundError:
    pass

if "--upgrade" in sys.argv:
    upgrade()
    sys.exit("upgrading")

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
templates = {
  "py": [
    "#!/usr/bin/env python3\n"
  ],
  "sh": [
    "#!/bin/bash\n"
  ],
  "rs": [
    "//\n",
    "//\n",
    "//\n",
    "fn main() {\n",
    "\n",
    "}\n"
  ],
  "json": [
    "{}\n"
  ],
  "php": [
    "<?php\n",
    "\n",
    "?>\n"
  ],
  "pl": [
    "#!/usr/bin/perl\n"
  ],
  "c": [
    "// \n",
    "//\n",
    "//\n",
    "\n",
    "#include <stdio.h>\n",
    "  \n",
    "int main()\n",
    "{\n",
    "\n",
    "}\n"
  ]
}#!!! Do NOT modify manually, use build!!!
#\!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/





def check_empty(filename):
    ''' Check if file exsists or is not empty '''
    if not Path(filename).exists():
        return False
    if os.path.getsize(filename) > 0:
        return True
    return False

if check_empty(filename):
    sys.exit("File not empty")

f_ext = Path(filename).suffix.strip('.') if not args.template else args.template
sb = [""] if f_ext not in templates else templates[f_ext]
try:
    with open(filename, 'w', encoding='utf-8') as file:
        # Writing data to a file
        file.writelines(sb)
        if args.x:
            chmod = os.system(f"chmod +x {filename}")

except FileNotFoundError:
	print("No such directory.")
