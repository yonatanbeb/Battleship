"""
Name:       parser.py

Purpose:    Parse Battleship Protocol (BP) messages.

Usage:      from parser import MessageParser
"""
from scapy.all import Packet, raw

from packet import BP, InitPacket, GuessPacket, ResponsePacket, ErrorPacket
from consts import BuildConsts


PACKET_TYPES = {
	100: InitPacket,
	110: GuessPacket,
	111: ResponsePacket,
	99: ErrorPacket
}


class MessageParser:
	@staticmethod
	def parse(message: bytes) -> Packet:
		packet = BP(message)
		if packet.TYPE in BuildConsts.GENERAL_MESSAGE_TYPES:
			return packet
		else:
			return PACKET_TYPES[packet.TYPE](raw(packet.payload))

	@staticmethod
	def parse_type(message: bytes) -> int:
		packet = BP(message)
		return packet.TYPE
