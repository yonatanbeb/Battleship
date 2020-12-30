import socket

from message.builder import MessageBuilder


class Waiter:
	def __init__(self, message_builder: MessageBuilder):
		self.message_builder = message_builder
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
				message = conn.recv(1024)
				response = self.message_builder.build(message)
				if not response:
					continue
				conn.sendall(response)


class Initiator:
	def __init__(self, message_builder: MessageBuilder):
		self.message_builder = message_builder
		self.port = 1234

	def play(self):
		domain = self.get_opponent_domain()
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.connect((domain, self.port))
			init = self.message_builder.build()
			s.sendall(init)
			while True:
				message = s.recv(1024)
				response = self.message_builder.build(message)
				if not response:
					continue
				s.sendall(response)

	@staticmethod
	def get_opponent_domain():
		while True:
			try:
				domain = input('Enter your opponents domain name or IP address: ')
				domain = socket.gethostbyname(domain)
				return domain
			except socket.gaierror:
				print('Invalid domain name or IP address.')

