import yaml
import sys
import os
import argparse
from glob import glob
from jinja2 import Template
from pprint import pprint

def display_help():
    print ""

# Manage cmdLine parameters.
parser = argparse.ArgumentParser(description="Configuration Builder")
parser.add_argument('-v','--verbose' ,help='Increase Verbosity',action="store_true")
parser.add_argument('-s', '--source', help='Provides YAML file to fill Jinja2 template, default=dict.yml',default='dict.yml')
parser.add_argument('-t','--template' ,help='template file, default=./template.j2',default='./template.j2')
parser.add_argument('-b','--base' ,help='Base to construct filename, default=generated-conf-',default='generated-conf-')
parser.add_argument('-k','--key' ,help='Key used in YAML file, default=hostname',default='hostname')
parser.add_argument('-o','--output', help='Directory to store configuration', default="configuration_output/")
parser.add_argument('-of','--output_format', help='File extension', default="conf")
# Manage All options and construct array
options = parser.parse_args()

# Check if output directory is existing, else create it.
if os.path.exists(options.output) is False:
        os.makedirs(options.output)

print 'Start configuration building'
# YAML file.
for file in os.listdir(options.source):
    with open( options.source+"/"+file ) as fh:
        data = yaml.load( fh.read() )
    #pprint( data )
    # Jinja2 template file.
    with open( options.template ) as t_fh:
        t_format = t_fh.read()

    for device in data:
    	hostname = device[ options.key ]
    	print '  - Generate config for '+ hostname
    	print ''
    	#pprint( device )
    	template = Template( t_format )

    	confFile = open( options.output+"/"+options.base + str(hostname) + '.' + options.output_format,'w')
    	confFile.write( template.render( device ) )
    	confFile.close()

print 'End of Script'
