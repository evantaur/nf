#!/usr/bin/env python3 
'''
script to build nf

'''

import os
import sys
import json
import subprocess

print("Starting build")
templates = {}

print("Listing templates")
template_dir="./templates/"
temp = os.listdir(template_dir)
for i in temp:
    with open(f"{template_dir}{i}",'r',encoding='utf-8') as file:
        print(f"Adding template {i}")
        text = file.readlines()
        templates[i] = text


print("Reading src/main.py")
'''Read main.py to memory'''
with open('./src/main.py','r',encoding='utf-8') as file:
    data = file.readlines()

print("Reading version number")
with open('version','r',encoding='utf-8') as file:
    version = float(file.readlines()[0].strip())


'''Find indexes to replace'''
print("Building...")
VersionIndex = data.index('__VERSION__=""\n')
data[VersionIndex] = f"__VERSION__ = {version}\n"
TemplateIndex = data.index('#!TEMPLATES\n')-2
for i in range(4):
    data.pop(TemplateIndex)
data[TemplateIndex] = f"'''\nAutomatically generated templates.\n'''\ntemplates = {json.dumps(templates,indent=2)}\n"


def get_manual():
    nf_help = subprocess.Popen(['python3', 'nf',"--help"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    stdout,stderr = nf_help.communicate()
    return f"<pre>\n{stdout.decode()}\n</pre>"


def write():
    '''Write to file'''
    with open('nf', 'w', encoding='utf-8') as file:
        file.writelines(data)
    with open('USAGE.md', 'w', encoding='utf-8') as file:
        file.writelines(get_manual())

#        print("Updating version")
#    with open('version', 'w', encoding='utf-8') as file:
#        file.writelines(str(version))
        print("Build finished")
write()
