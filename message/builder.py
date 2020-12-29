"""
Name:       builder.py

Purpose:    Build a Battleship Protocol (BP) message out of the BP custom packets.

Usage:      from builder import <any builder>
"""
from scapy.layers.inet import TCP
from scapy.all import bind_layers

from packet import BP, InitPacket, GuessPacket, ResponsePacket, ErrorPacket
from consts import PacketConsts

BPPacket = TCP
# TODO: move this to more appropriate location when created
bind_layers(TCP, BP, sport=1234, dport=1234)


class GeneralMessageBuilder:
    """
    Builds a general BP message
    """
    @staticmethod
    def build(type: int) -> BPPacket:
        """
        :param type: The type of general message
        :return <BPPacket>:
        """
        return TCP() / BP(TYPE=type)


class InitMessageBuilder:
    """
    Builds an INIT BP message
    """
    def __init__(self):
        self.type = PacketConsts.MESSAGE_TO_CODE['INIT']

    def build(self, first_player=0) -> BPPacket:
        """
        :param <int> first_player: The player who will start the game.
        :return <BPPacket>:
        """
        packet = TCP() / BP(TYPE=self.type)
        init_packet = InitPacket(FIRST_PLAYER=first_player)
        return packet / init_packet


class GuessMessageBuilder:
    """
    Builds a GUESS BP message
    """
    def __init__(self):
        self.type = PacketConsts.MESSAGE_TO_CODE['GUESS']

    def build(self, x, y) -> BPPacket:
        """
        :param <int> x: The horizontal coordinate
        :param <int> y: The vertical coordinate
        :return <BPPacket>:
        """
        packet = TCP() / BP(TYPE=self.type)
        guess_packet = GuessPacket(X=x, Y=y)
        return packet / guess_packet


class ResponseMessageBuilder:
    """
    Builds a RESPONSE BP message
    """
    def __init__(self):
        self.type = PacketConsts.MESSAGE_TO_CODE['RESPONSE']

    def build(self, answer) -> BPPacket:
        """
        :param <int> answer: The type of answer
        :return <BPPacket>:
        """
        packet = TCP() / BP(TYPE=self.type)
        response_packet = ResponsePacket(ANSWER=answer)
        return packet / response_packet


class ErrorMessageBuilder:
    """
    Builds an ERROR BP message
    """
    def __init__(self):
        self.type = PacketConsts.MESSAGE_TO_CODE['ERROR']

    def build(self, error) -> BPPacket:
        """
        :param <int> error: The type of error
        :return <BPPacket>:
        """
        packet = TCP() / BP(TYPE=self.type)
        error_packet = ErrorPacket(ERROR=error)
        return packet / error_packet
