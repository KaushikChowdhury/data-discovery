import abc
import logging

from collections import namedtuple
from pyhocon import ConfigTree, ConfigFactory
from databuilder import Scoped
from databuilder.extractor.base_extractor import Extractor
from databuilder.models.table_metadata import ColumnMetadata, TableMetadata

LOGGER = logging.getLogger(__name__)

TableKey = namedtuple('TableKey', ['schema_name', 'table_name'])

class BasePostgresMetadataExtractor:

    #config keys
    WHERE_CLAUSE_SUFFIX_KEY = 'where_clause_suffix'
    USE_CATALOG_AS_CLUSTER_NAME = 'use_catalog_as_cluster_name'
    CLUSTER_KEY = 'cluster_key'

    #default values
    DEFAULT_CLUSTER_NAME = 'master'

    DEFAULT_CONFIG = ConfigFactory.from_dict({
        WHERE_CLAUSE_SUFFIX_KEY: 'true',
        USE_CATALOG_AS_CLUSTER_NAME: True,
        CLUSTER_KEY: DEFAULT_CLUSTER_NAME
    })

    @abc.abstractmethod
    def get_sql_statements(self, use_catalog_as_cluster_name : bool, where_clause_suffix : str) -> any:
        """
        :return: Provides a record or None if no more record is available.
        """
        return None

    def init(self, conf: ConfigTree) -> None:
        conf= conf.with_fallback(BasePostgresMetadataExtractor.DEFAULT_CONFIG)


