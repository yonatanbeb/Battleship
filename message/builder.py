"""
Name:       builder.py

Purpose:    Build a Battleship Protocol (BP) message out of the BP custom packets.

Usage:      from builder import <any builder>
"""
from scapy.all import raw
from packet import BP, InitPacket, GuessPacket, ResponsePacket, ErrorPacket
from consts import PacketConsts, BuildConsts


class GeneralMessageBuilder:
    """
    Builds a general BP message
    """
    def build(self, type: int) -> BP:
        """
        :param type: The type of general message
        :return <BPPacket>:
        """
        if not self.valid(type):
            raise ValueError
        return BP(TYPE=type)

    @staticmethod
    def valid(type: int):
        return type in BuildConsts.GENERAL_MESSAGE_TYPES


class InitMessageBuilder:
    """
    Builds an INIT BP message
    """
    def __init__(self):
        self.type = BuildConsts.MESSAGE_TYPES['INIT']

    def build(self, first_player=0) -> BP:
        """
        :param <int> first_player: The player who will start the game.
        :return <BPPacket>:
        *   Error handling is implemented by the opponent   *
        """
        packet = BP(TYPE=self.type)
        init_packet = InitPacket(FIRST_PLAYER=first_player)
        return packet / init_packet


class GuessMessageBuilder:
    """
    Builds a GUESS BP message
    """
    def __init__(self):
        self.type = BuildConsts.MESSAGE_TYPES['GUESS']

    def build(self, x: int, y: int) -> BP:
        """
        :param <int> x: The horizontal coordinate
        :param <int> y: The vertical coordinate
        :return <BPPacket>:
        *   Error handling is implemented by the opponent   *
        """
        packet = BP(TYPE=self.type)
        guess_packet = GuessPacket(X=x, Y=y)
        return packet / guess_packet


class ResponseMessageBuilder:
    """
    Builds a RESPONSE BP message
    """
    def __init__(self):
        self.type = BuildConsts.MESSAGE_TYPES['RESPONSE']

    def build(self, answer: int) -> BP:
        """
        :param <int> answer: The type of answer
        :return <BPPacket>:
        *   Error handling is implemented by the opponent   *
        """
        packet = BP(TYPE=self.type)
        response_packet = ResponsePacket(ANSWER=answer)
        return packet / response_packet


class ErrorMessageBuilder:
    """
    Builds an ERROR BP message
    """
    def __init__(self):
        self.type = BuildConsts.MESSAGE_TYPES['ERROR']

    def build(self, error: int) -> BP:
        """
        :param <int> error: The type of error
        :return <BPPacket>:
        """
        if not self.valid(error):
            raise ValueError
        packet = BP(TYPE=self.type)
        error_packet = ErrorPacket(ERROR=error)
        return packet / error_packet

    @staticmethod
    def valid(error: int):
        return error in PacketConsts.ERROR_TYPES


class MessageBuilder:
    """
    Builder Composite
    """
    def __init__(self, general_builder, init_builder, guess_builder, response_builder, error_builder, board):
        self.general_builder = general_builder
        self.init_builder = init_builder
        self.guess_builder = guess_builder
        self.response_builder = response_builder
        self.error_builder = error_builder
        self._previous_message = None
        self.board = board

    def build(self, message=None) -> BP:
        """
        Create a BP message according to the given message, <message>, and the message <previous_message>.
        :return:
        """
        if (not self._previous_message) and (not message):
            message = self.init_builder.build()
            return raw(message)


