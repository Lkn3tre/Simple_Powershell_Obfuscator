import base64
import argparse
import random
import pwn
def xor(encoded,key):
    x = [chr(ord(a) ^ key) for a in encoded]
    return ''.join(x)


parser = argparse.ArgumentParser()
parser.add_argument("-p","--path", help="powershell script path",type=str,dest='path',required=True)
parser.add_argument("-o","--output", help="Output of the obfuscate script",type=str,dest='output',required=True)
args = parser.parse_args()

path = args.path
output = args.output

file = open(path,'r')
content = file.read()
file.close()

print ("[*] Generation of encryption key")
key = random.randint(1,1000)
print ("[*] XORing")
encoded = xor(content, key)
print ("[*] Encode in Base64")
encoded = base64.b64encode(encoded.encode())
print ("[*] your encoded script: " + output)


with open("payload.ps1") as f:
    templateObfuscate = f.read()

templateObfuscate = templateObfuscate.replace("{{chunk}}", encoded.decode('utf-8'))
templateObfuscate = templateObfuscate.replace("{{key}}", str(key))

file = open(output,"w")
file.write(templateObfuscate)
file.close()
