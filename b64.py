from base64 import b64encode, b64decode

flag = "fl4g{C0ngr4tss_Mo7h3r_fuck3r}"
flagencode = b64encode(flag.encode())
flagencode1 = b64encode(flagencode).decode()
output = str(flagencode1)
n = 1
while n != 20:
   fe = b64encode(output.encode())
   fe2= b64encode(fe).decode()
   output = output.replace(output,str(fe2))
   n += 1
print(output)
