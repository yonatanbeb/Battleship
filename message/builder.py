"""
Name:       builder.py

Purpose:    Build a Battleship Protocol (BP) message out of the BP custom packets.

Usage:      from builder import <any builder>
"""
from packet import BP, InitPacket, GuessPacket, ResponsePacket, ErrorPacket
from consts import PacketConsts


class GeneralMessageBuilder:
    """
    Builds a general BP message
    """
    @staticmethod
    def build(type: int) -> BP:
        """
        :param type: The type of general message
        :return <BPPacket>:
        """
        return BP(TYPE=type)


class InitMessageBuilder:
    """
    Builds an INIT BP message
    """
    def __init__(self):
        self.type = PacketConsts.TYPE_TO_CODE['INIT']

    def build(self, first_player=0) -> BP:
        """
        :param <int> first_player: The player who will start the game.
        :return <BPPacket>:
        """
        packet = BP(TYPE=self.type)
        init_packet = InitPacket(FIRST_PLAYER=first_player)
        return packet / init_packet


class GuessMessageBuilder:
    """
    Builds a GUESS BP message
    """
    def __init__(self):
        self.type = PacketConsts.TYPE_TO_CODE['GUESS']

    def build(self, x, y) -> BP:
        """
        :param <int> x: The horizontal coordinate
        :param <int> y: The vertical coordinate
        :return <BPPacket>:
        """
        packet = BP(TYPE=self.type)
        guess_packet = GuessPacket(X=x, Y=y)
        return packet / guess_packet


class ResponseMessageBuilder:
    """
    Builds a RESPONSE BP message
    """
    def __init__(self):
        self.type = PacketConsts.TYPE_TO_CODE['RESPONSE']

    def build(self, answer) -> BP:
        """
        :param <int> answer: The type of answer
        :return <BPPacket>:
        """
        packet = BP(TYPE=self.type)
        response_packet = ResponsePacket(ANSWER=answer)
        return packet / response_packet


class ErrorMessageBuilder:
    """
    Builds an ERROR BP message
    """
    def __init__(self):
        self.type = PacketConsts.TYPE_TO_CODE['ERROR']

    def build(self, error) -> BP:
        """
        :param <int> error: The type of error
        :return <BPPacket>:
        """
        packet = BP(TYPE=self.type)
        error_packet = ErrorPacket(ERROR=error)
        return packet / error_packet
