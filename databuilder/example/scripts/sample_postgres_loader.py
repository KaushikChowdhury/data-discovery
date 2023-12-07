"""
This is an example scipt on how to load data to Neo4j and Elasticsearch without using Airflow DAG.
"""

import logging
from elasticsearch import Elasticsearch
from pyhocon import ConfigFactory

from databuilder.job.job import DefaultJob



