# Configuration Builder

Provide python script to massively generate configuration based on :
- Python
- Jinja2
- Yaml

## Description

Simple Script created to count how many times objects are used in a SRX configuration. Goal is to identifiy which object can be deleted to clean up configuration.

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