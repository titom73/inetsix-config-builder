# Configuration Builder

Provide python script to massively generate configuration based on :
- Python
- Jinja2
- Yaml

## Description

Scripts to gene
## Installation

Scripts can be installed with pip:

```shell
$ pip install git+https://github.com/titom73/inetsix-config-builder
```

### Usage
Usage is like below:

```shell
$ inetsix-jinja-render -h                                                                                                                                 tgrimonet@tgrimonet
    usage: inetsix-jinja-render [-h] [-y YAML] [-t TEMPLATE] [-b BASE] [-o OUTPUT]
                                [-of OUTPUT_FORMAT]

    Configuration Builder

    optional arguments:
    -h, --help            show this help message and exit
    -y YAML, --yaml YAML  Provides YAML file to fill Jinja2 template,
                            default=dict.yml
    -t TEMPLATE, --template TEMPLATE
                            template file, default=./template.j2
    -b BASE, --base BASE  Base to construct filename, default=generated-conf-
    -o OUTPUT, --output OUTPUT
                            Directory to store configuration, default .
    -of OUTPUT_FORMAT, --output_format OUTPUT_FORMAT
                            File extension, default: .conf
```