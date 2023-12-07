import abc
from pyhocon import ConfigTree
from databuilder import Scoped


class Task(Scoped):
    """
    An absctract class that can run an abstrct task
    """

    @abc.abstractmethod
    def init(self, conf: ConfigTree):
        """
        Initialize task with conf.
        :param conf:
        :return:
        """
        pass

    @abc.abstractmethod
    def run(self):
        """
        Run the task.
        :return:
        """
        pass
