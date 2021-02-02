from base64 import b64encode, b64decode

flag = input("Enter Flag Format (flag{....}):")
ts = int(input("How many times (10,20,30):"))
flagencode = b64encode(flag.encode())
flagencode1 = b64encode(flagencode).decode()
output = str(flagencode1)
n = 1
while n != ts:
   fe = b64encode(output.encode())
   fe2= b64encode(fe).decode()
   output = output.replace(output,str(fe2))
   n += 1
print(output)
