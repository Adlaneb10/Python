from cryptography.fernet import Fernet

print("Hello mate")
store = input("What is your name?\n")

print("Welcome", store)

password = ""

print("Create a password")
password = str(input())

key = Fernet.password()
encoded = Fernet(key)
encrypt_msg = encrypt_type.encrypt(b"Hello World")

print(encrypt_msg)
