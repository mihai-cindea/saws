# -*- coding: utf-8 -*-
import six
import shlex


def shlex_split(text):
    """
    Wrapper for shlex, because it does not seem to handle unicode in 2.6.
    :param text: string
    :return: list
    """
    if six.PY2:
        text = text.encode('utf-8')
    return shlex.split(text)
