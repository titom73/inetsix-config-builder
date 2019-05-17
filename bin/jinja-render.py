#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import yaml
import sys
import os
import argparse
from glob import glob
from jinja2 import Template
from pprint import pprint

__author__ = "Thomas Grimonet"
__license__ = "GPL"
__version__ = "1.0.0"
__date__ = "15/05/2019"
__maintainer__ = "Thomas Grimonet"


def display_help():
    print("")


# Manage cmdLine parameters.
parser = argparse.ArgumentParser(description="Configuration Builder")
parser.add_argument('-y', '--yaml', help='Provides YAML file to fill Jinja2 template, default=dict.yml', default='dict.yml')
parser.add_argument('-t', '--template', help='template file, default=./template.j2', default='./template.j2')
parser.add_argument('-b', '--base', help='Base to construct filename, default=generated-conf-', default='generated-conf-')
parser.add_argument('-o', '--output', help='Directory to store configuration, default .', default=".")
parser.add_argument('-of', '--output_format', help='File extension, default: .conf', default="conf")
# Manage All options and construct array
options = parser.parse_args()

# Check if output directory is existing, else create it.
if os.path.exists(options.output) is False:
    os.makedirs(options.output)

print('Template rendering using Jinja and YAML')
# YAML file.
with open(options.yaml) as fh:
    data = yaml.load(fh.read())

# Jinja2 template file.
with open(options.template) as t_fh:
    t_format = t_fh.read()
print('* Generate config from template ' + options.template)
print('')
template = Template(t_format)
confFile = open(options.output + "/" + options.base + '.' + options.output_format, 'w')
confFile.write(template.render(data))
confFile.close()

print('End of Script')
