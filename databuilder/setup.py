import os
from pathlib import Path
from setuptools import setup, find_packages

__version__ = '0.0.1'

requirements_path = Path(__file__).parent / 'requirements.txt'

with open(requirements_path) as f:
    requirements_ = f.read().splitlines()

all_deps = requirements_

setup(
    name = 'DataDiscovery',
    version = __version__,
    description = 'Data Discovery',
    author = 'Celebel Tech',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    install_requires=requirements_,
    python_requires='>=3.10',
    extras_require={
        'all': all_deps,
    },
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ],
)

