import shutil
from setuptools import setup

# Load list of requirements from req file
with open('requirements.txt') as f:
    REQUIRED_PACKAGES = f.read().splitlines()

# Load description from README file
with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

# Rename Scripts to sync with original name
shutil.copyfile('bin/jinja-render.py', 'bin/inetsix-jinja-render')

setup(
    name="inetsix-template-render",
    version='0.2',
    scripts=["bin/inetsix-jinja-render"],
    python_requires=">=2.7",
    install_requires=REQUIRED_PACKAGES,
    url="https://github.com/titom73/inetsix-config-builder",
    license="BSD",
    author="Thomas Grimonet",
    author_email="tom@inetsix.net",
    description="Tool to render JINJA2 templates",
    long_description=LONG_DESCRIPTION,
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ]
)
