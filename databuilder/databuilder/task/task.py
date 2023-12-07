import abc
from databuilder.task.base_task import Task


class DefaultTask(Task):
    """
    A default task expencing to extract, transform, load
    """

    def __init__(self):
        pass

    def init(self, conf):
        pass
