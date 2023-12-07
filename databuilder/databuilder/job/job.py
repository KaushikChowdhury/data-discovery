import logging

from pyhocon import ConfigTree
from databuilder.job.base_job import Job
from databuilder.task.base_task import Task

LOGGER = logging.getLogger(__name__)


class DefaultJob(Job):
    """
    A default job that runs a task.
    """

    def __init__(self, conf: ConfigTree, task: Task) -> None:
        self._conf = conf
        self._task = task

    def init(self, conf: ConfigTree):
        pass

    def launch(self):
        LOGGER.info('Starting the job')
        self._task.init(self._conf)
        self._task.run()
        self._task.close()
        LOGGER.info('Finish the job')
