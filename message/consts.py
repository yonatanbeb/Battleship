"""
Name:       consts.py

Usage:      from consts import <any const class>
"""


class PacketConsts:
    BYTE = 8

    MESSAGE_TYPES = {
        100: 'INIT',
        101: 'ACCEPT',
        102: 'DENY',
        103: 'READY',
        110: 'GUESS',
        111: 'RESPONSE',
        50: 'TERMINATE',
        99: 'ERROR'
    }

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

    ERROR_TYPES = {
        0: 'INVALID TYPE',
        1: 'INVALID OFFER',
        2: 'INVALID COORDINATES',
        3: 'INVALID ANSWER'
    }


class BuildConsts:
    MESSAGE_TYPES = {value: key for key, value in PacketConsts.MESSAGE_TYPES.items()}

    ERROR_TYPES = {value: key for key, value in PacketConsts.ERROR_TYPES.items()}

    GENERAL_MESSAGE_TYPES = {
        101: 'ACCEPT',
        102: 'DENY',
        103: 'READY',
        50: 'TERMINATE'
    }

    ACCEPTED_REPLY = {
        None: (100, 101),
        100: (101, 102, 99),
        101: (103, ),
        102: (),
        103: (103, 110),
        110: (111, 99),
        111: (110, 99),
        99:  (100, 101, 102, 103, 110, 111)
    }
