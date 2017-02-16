import base64
import hashlib
import os
import json
from Crypto.Cipher import AES
from Crypto import Random
import sys

BS = 16
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS).encode('utf-8')
unpad = lambda s: s[:-ord(s[len(s)-1:])]
MODE = AES.MODE_CBC

class AESCipher:

	def __init__(self, key, iv, segment_size = 128):
		self.key = key
		self.iv = iv
		self.segment_size = segment_size


	def encrypt(self, enc):
		msg = enc.encode('utf-8')
		raw = pad(msg)
		cipher = AES.new(self.key, MODE, self.iv, segment_size=self.segment_size)
		after_cipher = cipher.encrypt(raw)
		return base64.b64encode(after_cipher).decode('utf-8')


	def decrypt(self, enc):
		msg = base64.b64decode(enc)
		cipher = AES.new(self.key, MODE, self.iv, segment_size=self.segment_size)
		dec = cipher.decrypt(msg)
		return unpad(dec).decode('utf-8')

	def decrypt_to_json(self, enc_data):
		enc_data = base64.b64decode(enc_data)
		cipher = AES.new(self.key, MODE, self.iv, segment_size=self.segment_size)
		dec = cipher.decrypt(enc_data)
		return json.dumps(dec.decode('utf-8'))