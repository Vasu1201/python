n = str(input("Enter Any String:"))
def encode(str):
      passkey=7777
      crypt=" "
      for i in str:
            crypt=crypt+chr(ord(i)^passkey)
      return crypt
print(encode(n))
print(encode(encode(n)))



