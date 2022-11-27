#!/usr/bin/env python3
import sys
import os
import argparse
import json
from pathlib import Path


__VERSION__=""


'''
Making config path if needed and reading user templates.
'''
home_dir = os.path.expanduser( '~' )
config_dir=f"{home_dir}/.config/nf"


user_templates=[]
user_template_dir=f"{config_dir}/templates"
Path(user_template_dir).mkdir( 0o760, True, True )
temp = os.listdir(user_template_dir)
for i in temp:
    user_templates.append(i)


#/!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\
#!!! Do NOT modify manually, use build!!!
#!TEMPLATES
#!!! Do NOT modify manually, use build!!!
#\!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!/


'''
Load config
'''
if Path(f"{config_dir}/config.json").exists():
    with open(f"{config_dir}/config.json",'r',encoding='utf-8') as cfg:
        conf = json.load(cfg)
else:
    conf = {}


def save_config():
    if len(conf.keys()) > 0:
        with open(f"{config_dir}/config.json",'w',encoding='utf-8') as cfg:
            json.dump(conf, cfg)
    else:
        os.remove(f"{config_dir}/config.json")


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

  %(prog)s test.sh

'''
    )
def any_in(a,b):
    return len([x for x in a if x in b])>0

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

if any_in(["--list","-l"],sys.argv):
    print("User templates:")
    for i in user_templates:
        print(f"  - {i}")
    print("System templates:")
    for i in templates:
        print(f"  - {i}")
    sys.exit(0)


if "--upgrade" in sys.argv:
    print("Upgrading")
    upgrade()
    print("Upgrade finished")
    sys.exit(0)


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

parser.add_argument(
    '-t','--template',
    default=None,
    help='use this template'
    )


parser.add_argument(
    '-a','--add',
    action="store_true",
    help='add file as custom template.'
    )


parser.add_argument(
    '-r','--remove',
    action="store_true",
    help='remove custom temlate'
    )


parser.add_argument(
    '-l','--list',
    action="store_true",
    help='list templates'
    )


editor = parser.add_argument_group(
    'Editor',
    description="Use these if you want to open the file after it has been edited"
    )


editor.add_argument(
    '-e','--edit',
    help='open in editor',
    action='store_true'
    )


editor.add_argument(
    '--change-editor',
    help='change editor',
    action='store_true'
    )


parser.add_argument(
    'filename',
    help='filename'
    )


def list_editors():
    """check availiable editors."""
    import shutil
    #This line will get replaced by src/editors
    editors = [ "nano", "vi", "emacs", "gedit", "kwrite", "kate" ]
    ret = ["default"]
    for key in editors:
        if shutil.which(key):
            ret.append(key)
    return ret


if "--change-editor" in sys.argv:
    editors=list_editors()
    current = [0,conf["editor"]] if "editor" in conf else [0,"default"]
    print("Please select editor:\n")
    for i,editor in enumerate(editors):
        if editor == current[1]:
            current[0] = i
        printformat = editor if editor != current[1] else f"\033[93m*{editor}*\033[0m"
        print(f"  [{i}] {printformat} ")
    try:
        s = input(f"\n\nSelect [default={current[1]}]:\n")
        s = int(s) if s else -1
        if(s == -1 or s >= len(editors)):
            sys.exit(0)
        if s >= 0:
            if "editor" in conf and s == 0:
                print("remove")
                conf.pop("editor")
            else:
                conf["editor"] = editors[s]
            save_config()
    except KeyboardInterrupt:
        pass
    sys.exit(0)


args = parser.parse_args()


filename = args.filename


def list_tempaltes():
    ''' list templates'''
    print("templates")
    sys.exit(0)

def get_template(template):
    '''
    Check if template exsists in user templates,
    if not attempt to use built in template
    '''
    if template in user_templates:
        with open(f"{user_template_dir}/{template}",'r',encoding='utf-8') as file:
            return file.readlines()
    elif template in templates:
        return templates[template]
    else:
        if args.template:
            sys.exit("Template not found!")
        return [""]

def check_empty(filename):
    ''' Check if file exsists or is not empty '''
    if not Path(filename).exists():
        return False
    if os.path.getsize(filename) > 0:
        return True
    return False


if args.add:
    exists = Path(filename).exists()
    if exists:
        templatename = input("Enter name for template:\n")
        with open(filename,'r',encoding='utf-8') as file:
            text = file.readlines()
            with open(f"{user_template_dir}/{templatename}",'w',encoding='utf-8') as f:
                f.writelines(text)
        sys.exit(0)
    sys.exit("File not found.")
elif args.remove:
    templatename = f"{user_template_dir}/{filename}"
    exists = Path(templatename).exists()
    if exists:
        os.remove(templatename)
        print(f"Template {filename} removed.")
        sys.exit(0)
    sys.exit(f"No template named {filename}")

else:
    if check_empty(filename):
        sys.exit("File not empty")

    f_ext = Path(filename).suffix.strip('.') if not args.template else args.template
    content = get_template(f_ext)
    try:
        if args.dir:
            ''' create directory if needed'''
            dirname=os.path.dirname(filename)
            Path(dirname).mkdir(0o760, True, True )
        with open(filename, 'w', encoding='utf-8') as file:
            # Writing data to a file
            file.writelines(content)
            if args.x:
                chmod = os.system(f"chmod +x {filename}")

    except FileNotFoundError:
    	print("No such directory.")
    except PermissionError:
    	print("Permission denied")

#sys.exit(args)
if args.edit:
    if "editor" in conf:
        os.system(f"{conf['editor']} {filename}")
    else:
        os.system(f"/usr/bin/editor {filename} &> /dev/null &")
