import cmd

from player import Waiter, Initiator


class BattleshipShell(cmd.Cmd):
	intro = 'Welcome to Battleship!'
	prompt = '>> '

	def do_wait(self, arg):
		pass
		# Waiter().play()

	def do_init(self, arg):
		pass
		# Initiator().play()


if __name__ == '__main__':
	BattleshipShell().cmdloop()
