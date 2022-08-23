from os import getcwd
from time import time
from pathlib import Path
from requests import get

class Kwelo:
	def __init__(self):
		self.api = "https://api.kwelo.com/v1"
		self.headers = {
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
		}

	def save_file(
			self,
			content: bytes,
			location: str = getcwd()):
		with open(
			Path(location).joinpath(f"{time() * 1000}.jpg"),
		mode="wb+",
		) as file:
			file.write(content)
			file.close()
		return True

	def get_self_ip_address(self):
		return get(
			f"{self.api}/network/ip-address/my?format=json",
			headers=self.headers).json()

	def get_ip_address_location(self, ip_address: str):
		return get(
			f"{self.api}/network/ip-address/location/{ip_address}?format=json",
			headers=self.headers).json()

	def get_identicon(self, name: str):
		return self.save_file(get(
			f"{self.api}/media/identicon/{name}",
			headers=self.headers).content)
