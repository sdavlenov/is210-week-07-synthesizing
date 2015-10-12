#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 02"""


import authentication
import getpass


def login(username, maxattempts=3):
    """ This function authenticates users using the getpass and authenticate
    modules.

    Args:
        username (str): A username.
        maxattempts (int): Max number of allowed attemps.  Default = 3.

    Returns:
        True or False.

    """
    authenticated = False
    attempt = 0
    warning = 'Incorrect username or password.  You have {} attempts left.'

    while not authenticated and attempt < maxattempts:
        mypass = getpass.getpass('Please enter your password:')

        if authentication.authenticate(username, mypass) is True:
            authenticated = True

        else:
            attempt += 1
            print warning.format(maxattempts - attempt)
    return authenticated
