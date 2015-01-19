import yaml
import sys
import os
import argparse
from glob import glob
from jinja2 import Template

def display_help():
    print ""

# Manage cmdLine parameters.
parser = argparse.ArgumentParser(description="Configuration Builder")
parser.add_argument('-v','--verbose' ,help='Increase Verbosity',action="store_true")
parser.add_argument('-y', '--yaml', help='Provides YAML file to fill Jinja2 template, default=dict.yml',default='dict.yml')
parser.add_argument('-t','--template' ,help='template file, default=./template.j2',default='./template.j2')
parser.add_argument('-o','--output' ,help='Base to construct filename, default=generated-conf-',default='generated-conf-')
#parser.add_argument('-dir','--directory' ,help='Directory to save configurations',default='./ouput')
# Manage All options and construct array
options = parser.parse_args()


print 'Start configuration builder'
# YAML file.
with open(options.yaml) as fh:
    data = yaml.load(fh.read())

# Jinja2 template file.
with open(options.template) as t_fh:
    t_format = t_fh.read()

for device in data:
    print '  - Generate config for '+str(device['mxRef'])
    template = Template(t_format)
    #print(template.render(data))
    confFile = open(options.output+str(device['mxRef'])+'.conf','w')
    confFile.write(template.render(device))
    confFile.close()

print 'End of Script'
