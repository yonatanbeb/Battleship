import socket


class Waiter:
	def __init__(self, message_handler):
		self.message_handler = message_handler
		self.host = ''
		self.port = 1234

	def wait(self):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.bind((self.host, self.port))
			s.listen()
			return s.accept()

	def play(self):
		conn, addr = self.wait()
		with conn:
			while True:
				packet = conn.recv(1024)
				packet = self.message_handler.handle(packet)
				conn.sendall(packet)


class Initiator:
	def __init__(self, message_handler):
		self.message_handler = message_handler
		self.port = 1234

	def play(self, domain):
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((domain, self.port))
			while True:
				packet = self.message_handler.handle()
