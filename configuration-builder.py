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
parser.add_argument('-y', '--yaml', help='Provides YAML file to fill Jinja2 template, default=dict.yml',default='dict.yml')
parser.add_argument('-t','--template' ,help='template file, default=./template.j2',default='./template.j2')
parser.add_argument('-b','--base' ,help='Base to construct filename, default=generated-conf-',default='generated-conf-')
parser.add_argument('-k','--key' ,help='Key used in YAML file, default=hostname',default='hostname')
# Manage All options and construct array
options = parser.parse_args()


print 'Start configuration building'
# YAML file.
with open( options.yaml ) as fh:
    data = yaml.load( fh.read() )

pprint( data )

# Jinja2 template file.
with open( options.template ) as t_fh:
    t_format = t_fh.read()

for device in data:
	hostname = device[ options.key ]
	print '  - Generate config for '+options.key
	print ''
	#pprint( device )
	template = Template( t_format )

	confFile = open( options.base + str(hostname) + '.conf','w')
	confFile.write( template.render( device ) )
	confFile.close()

print 'End of Script'