#!/usr/bin/env python3 
'''
script to build nf

'''

import os
import sys
import json

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
VersionIndex = data.index('__VERSION__=""\n')
TemplateIndex = data.index('#!TEMPLATES\n')

print("Building...")
data[VersionIndex] = f"__VERSION__ = {version}"
data[TemplateIndex] = f"templates = {json.dumps(templates,indent=2)}"




def write():
    '''Write to file'''
    with open('nf', 'w', encoding='utf-8') as file:
        file.writelines(data)
#        print("Updating version")
#    with open('version', 'w', encoding='utf-8') as file:
#        file.writelines(str(version))
        print("Build finished")
write()
