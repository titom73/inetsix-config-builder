#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
import argparse
from jinja2 import Environment, FileSystemLoader

__author__ = "Thomas Grimonet"
__license__ = "GPL"
__version__ = "1.0.0"
__date__ = "15/05/2019"
__maintainer__ = "Thomas Grimonet"


def display_help():
    print("")


if __name__ == '__main__':
    # Manage cmdLine parameters.
    parser = argparse.ArgumentParser(description="Configuration Builder")
    parser.add_argument('-y', '--yaml', help='Provides YAML file to fill Jinja2 template, default=dict.yml', default='dict.yml')
    parser.add_argument('-t', '--template', help='template file, default=./template.j2', default='./template.j2')
    parser.add_argument('-b', '--base', help='Base to construct filename, default=generated-conf-', default='generated-config')
    parser.add_argument('-o', '--output', help='Directory to store configuration, default .', default=".")
    parser.add_argument('-of', '--output_format', help='File extension, default: .conf', default="conf")
    # Manage All options and construct array
    options = parser.parse_args()

    print('Template rendering using Jinja and YAML')
    # Check if output directory is existing, else create it.
    if os.path.exists(options.output) is False:
        os.makedirs(options.output)
    # Capture our current directory
    WORKING_DIR = os.path.dirname(os.path.abspath(options.template))
    TEMPLATE_FILE = os.path.basename(options.template)
    print('* Template directory: ' + WORKING_DIR)
    print('* Template Filename: ' + TEMPLATE_FILE)

    # YAML file.
    with open(options.yaml, 'r') as stream:
        try:
            data = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    # pp = pprint.PrettyPrinter(indent=1)
    # pp.pprint(data)

    # Jinja2 template file.
    with open(options.template) as t_fh:
        print('* Opening template file')
        content = t_fh.read()

    print('* Generate config from template ' + options.template)
    env = Environment(loader=FileSystemLoader(WORKING_DIR), trim_blocks=True, lstrip_blocks=True)
    template = env.get_template(TEMPLATE_FILE)

    # Save output
    filename = options.output + "/" + options.base + '.' + options.output_format
    print('* Save output to ' + filename)
    with open(filename, 'w') as confFile:
        confFile.write(template.render(data))

    print('End of Script')
