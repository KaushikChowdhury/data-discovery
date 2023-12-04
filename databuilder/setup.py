import os
from pathlib import Path
from setuptools import setup, find_packages

__version__ = '0.0.1'

requirements_path = Path(__file__).parent / 'requirements.txt'

with open(requirements_path) as f:
    requirements_ = f.read().splitlines()


if __name__=="__main__":
    print(requirements_)
