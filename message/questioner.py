"""
Name:       questioner.py

Purpose:    Questions player for input to build the Battleship Protocol (BP) messages.

Usage:      from questioner import Questioner
"""


class OfferQuestioner:
	def __init__(self):
		self.accepted_input = ['y', 'n']

	def question(self):
		resp = input(f'Do you want to play?\n{self.accepted_input}: ')
		while resp not in self.accepted_input:
			resp = input(f'{self.accepted_input}: ')
		if resp == 'y':
			return 101
		return 102


class InitQuestioner:
	def __init__(self):
		self.accepted_input = ['y', 'n']

	def question(self):
		resp = input(f'Do you want to play first?\n{self.accepted_input}: ')
		while resp not in self.accepted_input:
			resp = input(f'{self.accepted_input}: ')
		if resp == 'y':
			return 0
		return 1


class GuessQuestioner:
	def __init__(self):
		self.accepted_input = [i for i in range(1, 11)]

	def question(self):
		print('Enter your guess:')
		x = input(f'X {self.accepted_input}: ')
		y = input(f'Y {self.accepted_input}: ')
		while (x not in self.accepted_input) or (y not in self.accepted_input):
			x = input(f'X {self.accepted_input}: ')
			y = input(f'Y {self.accepted_input}: ')
		return x, y