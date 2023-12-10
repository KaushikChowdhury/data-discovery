import importlib

from pyhocon import ConfigFactory, ConfigTree
from sqlalchemy import create_engine

from databuilder import Scoped
from databuilder.extractor.base_extractor import Extractor


class SQLAlchemyExtractor(Extractor):
    """
    An extractor that extracts records using SQLAlchemy. Databases that support
    SQLAlchemy can be done using this extractor.
    """
    CONN_STRING = 'conn_string'
    EXTRACT_SQL = 'extract_sql'
    CONNECT_ARGS = 'connect_args'

    def init(self, conf: ConfigTree) -> None:
        self.conf = conf
        print(f"conf: {conf}")

        self.connection = self._get_connection()
        self.extract_sql = conf.get_string(SQLAlchemyExtractor.EXTRACT_SQL)

    def _get_connection(self):
        """
        Create an sql connection
        """
        connect_args = {
            k: v

            for k, v in self.conf.get_config(
                self.CONNECT_ARGS,
            ).items()
        }

        engine = create_engine(self.conf.get_string(self.CONN_STRING),
                               connect_args=connect_args)
        conn = engine.connect()
        return conn

    def _execute_query(self):
        results = self.connection.execute(self.extract_sql)
        self.iter = iter(results)
