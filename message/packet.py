"""
Name:       packet.py

Purpose:    Classes of the Battleship Protocol (BP) custom packets.

Usage:      from packet import Message
"""
from scapy.all import Packet, BitField, BitEnumField

from consts import PacketConsts


class BP(Packet):
    """
    The Battleship Protocol packet.
    Specifies the type of packet over this one.
    fields:
        :type: a type of BP message.
            100 -   INIT        :   InitPacket
            101 -   ACCEPT      :
            102 -   DENY        :
            103 -   READY       :
            110 -   GUESS       :   GuessPacket
            111 -   RESPONSE    :   ResponsePacket
            50  -   TERMINATE   :
            99  -   ERROR       :   ErrorPacket
    *   if a class is specified after the colon (:), then the field also
        represents the type of packet over the BP packet.
    """
    fields_desc = [
        BitEnumField('TYPE', default=0, size=PacketConsts.BYTE, enum=PacketConsts.MESSAGE_TYPES)
    ]


class InitPacket(Packet):
    """
    The game initialization packet.
    Sent to initialize a game of Battleship.
    fields:
        first_player:
            0   -   SENDER      :   The sender will play first.
            1   -   RECIPIENT   :   The recipient will play first.
    *   The default is 0, meaning by default the initiator of the game begins.
    """
    fields_desc = [
        BitEnumField('FIRST_PLAYER', default=0, size=PacketConsts.BYTE, enum=PacketConsts.PLAYERS),
    ]


class GuessPacket(Packet):
    """
    The guess packet.
    Sent as the current playing player's turn.
    fields:
        X:
          (0-9)   -   horizontal coordinate
        Y:
          (0-9)   -   vertical coordinate
    """
    fields_desc = [
        BitField('X', default=0, size=PacketConsts.BYTE / 2),
        BitField('Y', default=0, size=PacketConsts.BYTE / 2),
    ]


class ResponsePacket(Packet):
    """
    The response packet.
    Sent by the recipient of a guess packet, after receiving it.
    fields:
        answer:
            0   -   'MISS'
            1   -   'HIT'
            2   -   'SINK'
            3   -   'WIN'
    """
    fields_desc = [
        BitEnumField('ANSWER', default=0, size=PacketConsts.BYTE, enum=PacketConsts.RESPONSES),
    ]


class ErrorPacket(Packet):
    """
    The error packet.
    Sent if the contents of a packet are invalid, or the order of the packets received is so.
    fields:
        error:
            0   -   'INVALID TYPE'
            1   -   'INVALID OFFER'
            2   -   'INVALID COORDINATES'
            3   -   'INVALID ANSWER'
    """
    fields_desc = [
        BitEnumField('ERROR', default=0, size=PacketConsts.BYTE, enum=PacketConsts.ERROR_TYPES),
    ]
