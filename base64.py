from base64 import b64encode, b64decode

msg = "kaito"
encode1 = b64encode(msg.encode())
ms = str(encode1)
n = 1
while n != 10:
    proc1 = str(b64encode(ms.encode()))
    ms = ms.replace(ms, proc1)
    n = n + 1
print(ms)
