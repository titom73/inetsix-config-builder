# Configuration Builder

Provide python script to massively generate configuration based on :
- Python
- Jinja2
- Yaml

## Description

Simple Script created to generate text document for many entries by using a template and YAML data modeling. It can be used for any kind of text file and it is not related to a specific vendor / language.

For the moment, one of the use case is to generate configuration for many devices based on a `JINJA2` template.

## Requirements

In order to run this script you must install following modules:

- argparse / optparse

	```pip install argparse```

- Jinja2

    ```pip install jinja2```

- Yaml:

    ```pip install yaml```

### Usage
Usage is like below:

    python configuration-builder.py -h
    usage: configuration-builder.py [-h] [-v] [-y YAML] [-t TEMPLATE] [-o OUTPUT]

    Configuration Builder

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         Increase Verbosity
      -y YAML, --yaml YAML  Provides YAML file to fill Jinja2 template,
                            default=dict.yml
      -t TEMPLATE, --template TEMPLATE
                            template file, default=./template.j2
      -o OUTPUT, --output OUTPUT
                            Base to construct filename, default=generated-conf-