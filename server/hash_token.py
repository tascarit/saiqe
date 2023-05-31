from cryptography.fernet import Fernet

def on_encrypt(xf):
	salt = Fernet(b'K9DYf-cxPFpxUYYYkq2oFeUsUmkABveKXU87ZS0pkG8=')
	token = str(salt.encrypt(str(xf).encode('utf-8')))

	return token

def on_decrypt(salt_key):
	salt = Fernet(b'K9DYf-cxPFpxUYYYkq2oFeUsUmkABveKXU87ZS0pkG8=')
	xf = str(salt.decrypt(salt_key).decode('utf-8'))

	return xf