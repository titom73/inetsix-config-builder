![GitHub](https://img.shields.io/github/license/titom73/inetsix-config-builder.svg) [![Build Status](https://travis-ci.org/titom73/inetsix-config-builder.svg?branch=master)](https://travis-ci.org/titom73/inetsix-config-builder)  ![GitHub repo size](https://img.shields.io/github/repo-size/titom73/inetsix-config-builder.svg)  ![GitHub top language](https://img.shields.io/github/languages/top/titom73/inetsix-config-builder.svg)  ![Libraries.io dependency status for GitHub repo](https://img.shields.io/librariesio/github/titom73/inetsix-config-builder.svg)

# Configuration Builder

Provide python script to render templates based on :
- Python 2.7 & 3.x
- Jinja2
- Yaml

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