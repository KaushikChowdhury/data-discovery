import abc
from pyhocon import ConfigFactory, ConfigTree  # noqa: F401
from databuilder import Scoped
from databuilder.utils.closer import Closer


class Job(Scoped):
    """
    A databuilder job that represents single unit of work
    """
    closer = Closer()

    @abc.abstractmethod
    def init(self, conf: ConfigTree):
        """
        Initialize job with conf.
        :param conf:
        :return:
        """
        pass

    @abc.abstractmethod
    def launch(self):
        """
        Launch the job.
        :return:
        """
        pass
