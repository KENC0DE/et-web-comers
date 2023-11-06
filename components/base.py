#!/usr/bin/python3
"""
    Base module: Ground for future modules.
"""


from uuid import uuid4


class Base:
    """Base class: where common attributes and methodes is defined.
    """

    id = ""

    def __init__(self):
        """initialize requiremnts
        """
        self.id = uuid4()
