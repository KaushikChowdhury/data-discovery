import abc

from pyhocon import ConfigFactory, ConfigTree  # noqa: F401


class Scoped(object, metaclass=abc.ABCMeta):
    _EMPTY_CONFIG = ConfigFactory.from_dict({})  # type: ConfigTree
    """
    An interface for class that works with scoped(nested) configs.
    """

    @abc.abstractmethod
    def init(self, conf: ConfigTree):
        """
        All scoped instance to be lazily initialized with conf.
        :param conf:
        :return: None
        """
        pass

    @abc.abstractmethod
    def get_scope(self) -> str:
        """
        Get a scope name.
        :return: scope name
        """
        return ''

    def close(self):
        """
        Close the instance.
        :return:
        """
        pass

    @classmethod
    def get_scoped_conf(cls, conf: ConfigTree, scope: str) -> ConfigTree:
        """
        Get a scoped config from conf.
        :param conf:
        :param scope:
        :return:
        """

        if not scope:
            return Scoped._EMPTY_CONFIG

        return conf.get_config(scope, Scoped._EMPTY_CONFIG)
