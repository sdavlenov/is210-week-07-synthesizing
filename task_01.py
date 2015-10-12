#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task 01"""

def get_matches(players):
    """Function that creates all possible matches.

    Arg:
        players(list): a list of players

    Returns:
        a created list of tuples that are the matches.

    Examples:
        >>> import task_01
        >>> task_01.get_matches(['sal', 'pitkin', 'pat'])
        [('sal', 'pitkin'), ('sal', 'pat'), ('pitkin', 'pat')]
    """

    result = []
    for i, player1 in enumerate(players):
        for player2 in players[i + 1:]:
            result.append((player1, player2))
    return result
