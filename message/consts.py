"""
Name:       consts.py

Usage:      from consts import <any const class>
"""


class PacketConsts:
    BYTE = 8

    CODE_TO_TYPE = {
        100: 'INIT',
        101: 'ACCEPT',
        102: 'DENY',
        103: 'READY',
        110: 'GUESS',
        111: 'RESPONSE',
        50: 'TERMINATE',
        99: 'ERROR'
    }

    TYPE_TO_CODE = {value: key for key, value in CODE_TO_TYPE.items()}

    PLAYERS = {
        0: 'SENDER',
        1: 'RECIPIENT'
    }

    RESPONSES = {
        0: 'MISS',
        1: 'HIT',
        2: 'SINK',
        3: 'WIN'
    }

    ERRORS = {
        0: 'INVALID TYPE',
        1: 'INVALID OFFER',
        2: 'INVALID COORDINATES',
        3: 'INVALID ANSWER'
    }
