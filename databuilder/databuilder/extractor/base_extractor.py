import abc
from pyhocon import ConfigTree
from databuilder import Scoped


class Extractor(Scoped):
    """
    An extractor extracts record from external data source
    """

    @abc.abstractmethod
    def init(self, conf: ConfigTree) -> any:
        """
        Initialize extractor with conf.
        :param conf:
        :return:
        """
        pass

    @abc.abstractmethod
    def extract(self) -> any:
        """
        Extract records.
        :return:
        """
        return None
