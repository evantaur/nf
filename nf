#!/usr/bin/env python3
import sys
from pathlib import Path

__VERSION__ = 0.02
user_help = f'''
Generates a new file with a shebang based on file extention.

Usage {sys.argv[0]} <inputfile>

eg:
{sys.argv[0]} python_project.py
or
{sys.argv[0]} {Path.home()}/python_project.py
'''

#check if input
if len(sys.argv) <= 1:
    sys.exit(user_help)

filename = sys.argv[1]



templates = {
  "py": [
    "#!/usr/bin/env python3\n"
  ],
  "sh": [
    "#!/bin/bash\n"
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
}
#check if file exsists and quit if it does.
if Path(filename).exists():
    sys.exit("File not empty")

f_ext = Path(filename).suffix.strip('.')
sb = [""] if f_ext not in templates else templates[f_ext]
try:
    with open(filename, 'w', encoding='utf-8') as file:
        # Writing data to a file
        file.writelines(sb)
        print(f"Wrote a new file to {filename}")
except FileNotFoundError:
	print("No such directory.")
