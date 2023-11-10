#!/usr/bin/python3
"""
    Base module: Ground for future modules.
"""


from uuid import uuid4
import json



class Base:
    """Base class: where common attributes and methodes is defined.
    """

    def __init__(self, arg=None, *args, **kwarg):
        """initialize requiremnts
            arg: single arguments passed to the class.
            args: list passed to the class.
            kwargs: dictionary passed to the class.
        """
        if kwarg and kwarg != {}:
            for attr, val in kwarg.items():
                setattr(self, attr, val)
        else:
            self.id = uuid4()
            self.name = arg
