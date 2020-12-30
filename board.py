"""
Name:       board.py

Purpose:    Implement a class representing the Battleship board.

Usage:      from board import BattleshipBoard
"""


class BattleshipBoard:
	def __init__(self):
		self.hits = 0
		self.ships = {
			'carrier': [],
			'battleship': [],
			'destroyer': [],
			'submarine': [],
			'patrol_boat': []
		}
		self.ship_sizes = {
			'carrier': 5,
			'battleship': 4,
			'destroyer': 3,
			'submarine': 3,
			'patrol_boat': 2
		}
		self.setup()
		self.opponent_guesses = []

	def setup(self):
		print('Setup:\n------')
		for ship in self.ships:
			self.place_ship(ship, self.ship_sizes[ship])

	def place_ship(self, name, size):
		print(f'\tSetup the {name} (size {size}) ship:')
		while True:
			axis = input('Select the axis (h=horizontal, v=vertical):\n\t')
			start = input('Select the starting coordinate in the following format: X Y\n\t')
			try:
				x, y = start.split()
				x = int(x) - 1
				y = int(y) - 1
				break
			except ValueError:
				print('The starting coordinate must be two integers in the following format: X Y')
		self.ships[name] = [(x, y + i) for i in range(size)] if axis == 'h' \
			else [(x + i, y) for i in range(size)]

	def answer(self, x: int, y: int) -> int:
		if not self.valid_guess(x, y):
			return -1
		self.opponent_guesses.append((x, y))
		hit_ship = self.is_hit((x, y))
		if hit_ship:
			if self.is_sink(hit_ship):
				if self.is_win():
					return 3
				return 2
			return 1
		return 0

	def valid_guess(self, x, y):
		return (0 <= x <= 9) and (0 <= y <= 9) and ((x, y) not in self.opponent_guesses)

	def is_hit(self, coordinate):
		for ship in self.ships:
			ship_coordinates = self.ships[ship]
			if coordinate in ship_coordinates:
				index = ship_coordinates.index(coordinate)
				ship_coordinates[index] = False
				return ship
		return False

	def is_sink(self, ship):
		if not any(self.ships[ship]):
			self.ships.pop(ship)
			return True
		return False

	def is_win(self):
		if not self.ships:
			return True
		return False

	def print_board(self):
		board = [[0 for _ in range(10)] for _ in range(10)]
		for ship in self.ships:
			ship_coordinates = self.ships[ship]
			for coordinate in ship_coordinates:
				(x, y) = coordinate
				board[x][y] = 'S'
		for row in board:
			print(row)
